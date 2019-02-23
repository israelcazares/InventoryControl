#!/usr/bin/env python
# -*- coding: utf-8 -*-

import httplib
from urlparse import urlparse

import pandas as pd
import xml.etree.cElementTree as ET
import os.path
from optparse import OptionParser
from optparse import OptionGroup

import config

def get_xml(url):
	u = urlparse(url)
	httpClient = httplib.HTTPConnection(u.hostname, u.port)
	httpClient.connect()
	httpClient.request('GET', u.path+'?'+u.query, None)
	response = httpClient.getresponse()
	
	xml = ''
	if response.status == httplib.OK:
		xml = response.read()
	else:
		print 'Error:${alignr} Sin respuesta del servidor'
	
	return xml

def get_producto(sku):
	try:
		df = pd.read_hdf('{0}/productos.h5'.format(ruta), 'productos', where=u'SKU="{0}"'.format(sku))
		lista = df.to_dict(orient='records')
		if len(lista) > 0:
			row = lista[0]
			return row
		else:
			return None
	except:
		return None

def iter_xml(articulos):
	for item in articulos.iterfind('.//item'):
		row={}
		row['SKU'] = item.find('codigo_fabricante').text
		row['SKU_Proveedor'] = item.find('clave').text
		row['Proveedor'] = 'CVA'
		row['PartNumber'] = row['SKU']
		row['BrandName'] = item.find('marca').text
		
		ficha_tecnica = item.find('ficha_tecnica').text
		ficha_comercial = item.find('ficha_comercial').text
		
		#if ficha_tecnica == None or ficha_comercial == None:
		#	continue
		
		cat = item.find('grupo').text
		subcat = item.find('subgrupo').text
		
		if subcat == None:
			subcat = ''
		
		if not ((cat == config.categorias_cva[categoria]['Categoria'] or config.categorias_cva[categoria]['Categoria'] == '') and (subcat == config.categorias_cva[categoria]['SubCategoria'] or config.categorias_cva[categoria]['SubCategoria'] == '')):
			continue

		producto = get_producto(row['SKU'])
		print producto
		if producto == None:
			continue

		row['DescriptionLong'] = u"{0}\n{0}".format(ficha_tecnica, ficha_comercial)
		row['DescriptionShort'] = item.find('descripcion').text
		row['Category'] = config.categoria_cva_web[categoria]['Categoria']
		row['SubCat'] = config.categorias_cva_web[categoria]['SubCategoria']

		importe = round(float(item.find('precio').text), 2)
		moneda = item.find('moneda').text

		if moneda == 'Dolar':
			importe = importe * config.dolar_cva

		iva = round(importe * 0.16, 2)
		subtotal = round(importe + iva, 2)
		margen = round(subtotal * config.delta / 100, 2)
		precioFinal = round(subtotal + margen, 2)

		row['PriceFinal'] = precioFinal
		row['Stock'] = item.find('disponible').text
		row['Dolar'] = config.dolar_cva
		row['Height'] = producto['Height']
		row['Width'] = producto['Width']
		row['Lenght'] = producto['Lenght']
		row['Weight'] = producto['Weight']
		row['thumb'] = item.find('imagen').text
		row['largeImg'] = item.find('imagen').text

		yield row

class CustomOptionParser(OptionParser):
	def format_epilog(self, formatter):
		return self.epilog

def main():
	prog = os.path.basename(sys.argv[0])
	usage = "Como usar: %prog [options]"
	epilog = "\nEjemplo de uso:\n  Para correr el proceso en la categoria de Monitores\n    %s -c Monitores\n    %s --categoria=Computadoras\n\n" % (prog, prog)
	
	parser = CustomOptionParser(usage, add_help_option=False, epilog=epilog)
	parser.add_option("-h", "--help", action="help", help="Muestra esta ayuda y termina la ejecucion")
	parser.add_option("-c", "--categoria", type="string", help="Para enviar la categoria a procesar, este dato es requerido")
	
	(options, args) = parser.parse_args()
	
	if options.categoria == None:
		parser.error('El parametro categoria es requerido ejecute %s -h para ver todas las opciones' % prog)
	else:
		categoria = options.categoria
	print "Categoria: %s" % categoria

	xml=get_xml('ServiceURL')
	ruta = os.path.dirname(os.path.realpath(__file__))
	#xml_file = open('{0}/cva_{1}.xml'.format(ruta, categoria), 'w')
	#xml_file.write(xml)
	#xml_file.close()

	# Convertir xml a pandas
	etree = ET.fromstring(xml)
	df = pd.DataFrame(list(iter_xml(etree)))
	df.set_index('SKU', inplace=True)
	
	df.to_csv('{0}/cva_{1}.csv'.format(ruta, categoria), encoding='utf-8')

if __name__ == '__main__':
	main()

