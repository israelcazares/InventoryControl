#!/usr/bin/env python
# -*- coding: utf-8 -*-

import httplib
from urlparse import urlparse

import pandas as pd
import xml.etree.cElementTree as ET
import os.path
import base64
from optparse import OptionParser
from optparse import OptionGroup
import sys

import config

ruta = os.path.dirname(os.path.realpath(__file__))

def get_soap(url):
	u = urlparse(url)
	keyData = base64.b64decode(config.key_pch_servicio).split(':')
	method = 'ObtenerListaArticulos'
	data = '<?xml version="1.0" encoding="UTF-8"?><SOAP-ENV:Envelope xmlns:SOAP-ENV="http://schemas.xmlsoap.org/soap/envelope/" xmlns:ns1="http://{0}/" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:SOAP-ENC="http://schemas.xmlsoap.org/soap/encoding/" SOAP-ENV:encodingStyle="http://schemas.xmlsoap.org/soap/encoding/"><SOAP-ENV:Body><ns1:{1}><cliente xsi:type="xsd:int">{2}</cliente><llave xsi:type="xsd:string">{3}</llave></ns1:{1}></SOAP-ENV:Body></SOAP-ENV:Envelope>'.format(u.hostname, method, keyData[0], keyData[1])
	httpClient = httplib.HTTPConnection(u.hostname, u.port)
	httpClient.connect()
	httpClient.request('POST', u.path, data, {
		'Host': u.hostname,
		'Content-Type': 'text/xml; charset=utf-8',
		'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:49.0) Gecko/20100101 Firefox/49.0',
		'SOAPAction': 'http://{0}/{1}/{2}'.format(u.hostname, u.path, method)
	})
	response = httpClient.getresponse()
	
	xml = ''
	if response.status == httplib.OK:
		xml = response.read()
	else:
		print 'Error: Sin respuesta del servidor'
	
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

def iter_xml(articulos, categoria):
	for item in articulos.iterfind('.//datos/item'):
		row={}
		row['SKU'] = item.find('skuFabricante').text

		cat = item.find('seccion').text
		subcat = item.find('linea').text
		if subcat == None:
			subcat = ''
		
		if not ((cat == config.categorias_pch[categoria]['Categoria'] or config.categorias_pch[categoria]['Categoria'] == '') and (subcat == config.categorias_pch[categoria]['SubCategoria'] or config.categorias_pch[categoria]['SubCategoria'] == '')):
			continue

		row['Categoria'] = config.categorias_pch_web[categoria]['Categoria']
		row['SubCategoria'] = config.categorias_pch_web[categoria]['SubCategoria']

		producto = get_producto(row['SKU'])
		print producto
		if producto == None:
			continue

		row['SKU_Proveedor'] = item.find('sku').text
		row['Proveedor'] = 'PCH'
		row['PartNumber'] = row['SKU']
		row['BrandName'] = item.find('marca').text
		
		ficha_tecnica = producto['DescriptionLong'] #item.find('descripcion').text
		ficha_comercial = ''
		
		if ficha_tecnica == None or ficha_comercial == None:
			continue
		
		row['DescriptionLong'] = ficha_tecnica #u"{0}\n{0}".format(ficha_tecnica, ficha_comercial)
		row['DescriptionShort'] = item.find('descripcion').text
		
		importe = round(float(item.find('precio').text), 2)
		moneda = item.find('moneda').text

		if moneda == 'USD':
			importe = importe * config.dolar_pch

		iva = round(importe * 0.16, 2)
		subtotal = round(importe + iva, 2)
		margen = round(subtotal * config.delta / 100, 2)
		precioFinal = round(subtotal + margen, 2)

		row['PriceFinal'] = precioFinal
		row['Stock'] = item.find('.//existencia').text
		row['Dolar'] = config.dolar_pch
		row['Height'] = producto['Height'] #item.find('alto').text
		row['Width'] = producto['Width'] #item.find('ancho').text
		row['Lenght'] = producto['Lenght'] #item.find('largo').text
		row['Weight'] = producto['Weight'] #item.find('peso').text
		row['thumb'] = producto['thumb']
		row['largeImg'] = producto['largeImg']

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

	xml=get_soap('ServiceURL')
	
	# Convertir xml a pandas
	etree = ET.fromstring(xml)
	df = pd.DataFrame(list(iter_xml(etree, categoria)))
	
	if not df.empty:
		df.set_index('SKU', inplace=True)
		df.to_csv('{0}/pch_{1}.csv'.format(ruta, categoria), encoding='utf-8')


if __name__ == '__main__':
	main()


