#!/usr/bin/env python
# -*- coding: utf-8 -*-
from scrapy import Spider 
from selenium import webdriver
import base64
from scrapy.exporters import CsvItemExporter
from datetime import datetime
from scrapy.crawler import CrawlerProcess
from scrapy import signals
from scrapy.exporters import JsonLinesItemExporter
import os.path
from pyvirtualdisplay import Display
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
from optparse import OptionParser
from optparse import OptionGroup
import time
import fileinput
import sys
import re
import config

systemTime = datetime.now()

def all_words(needle, haystack):
            return set(needle).issubset(set(haystack))

class ProductSpider(Spider):
	name = "ingramSpider"
	start_urls = ['ServiceURL']
	key = config.key_ingram
	categorias = config.categorias
	categorias_web = config.categorias_web
	
	def __init__(self, **kw):
		self.driver = webdriver.Chrome()
		self.categoria = kw.get('categoria')
		self.page = kw.get('pagina')
	
	def replace_dolar(self, dolar):
		ruta = os.path.dirname(os.path.realpath(__file__))
		f=fileinput.FileInput('%s/config.py'%(ruta), inplace=True)
		for line in f:
			line = re.sub(r'dolar_ingram=\d+\.*\d*','dolar_ingram={0}'.format(dolar),line.strip("\r\n"))
			print line

	def parse(self, response):
		print 'Inicio'
		self.driver.set_window_size(1280, 720)
		
		# Cargar login y acceder a la pagina ###########################
		self.driver.get('ServiceURL')
		
		try:
			self.login()
			print "First login"
		except:
			print "Exception Alert"
			self.login()
		
		self.driver.save_screenshot('afterLogin.png')
		
		# Cargar Categoria #############################################
		timeout = 30 # seconds
		WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located((By.ID, 'aspnetForm')))
		if self.categoria in self.categorias:
			print "url categoria %s" % self.categorias[self.categoria]
			self.driver.get(self.categorias[self.categoria])
		else:
			print "No se encontro la categoria (%s)" % self.categoria
			return
		
		# Cambiar a paginado de 50 items ###############################
		try:
			WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located((By.ID, 'ctl00_ContentPlaceHolder1_ddlResultsPerPage')))
			print "Page is ready!"
			#self.driver.save_screenshot('categoria.png')
			
			select = Select(self.driver.find_element_by_id('ctl00_ContentPlaceHolder1_ddlResultsPerPage'))
			select.select_by_value('50') #.click()
			
		except TimeoutException:
		    print "Loading took too much time!"
		    #self.driver.save_screenshot('error_categoria.png')
		
		# Paginar para obtener los datos ###############################
		page = self.page
		sku = ''
		reintento = 1
		
		if page > 1:
			try:
				WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located((By.ID, 'ctl00_ContentPlaceHolder1_ddlResultsPerPage')))
				self.driver.execute_script("DoCallback2('Jump%d')" % page)
			except TimeoutException:
				print "No pudo inicializar la pagina inicial: %d" % page
				return
		
		winOrigen = self.driver.current_window_handle
		winProduct = None
		
		for handle in self.driver.window_handles:
			print handle
		
		dolar_flag = True
		while True:
			try:
				WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located((By.ID, 'ctl00_ContentPlaceHolder1_ddlResultsPerPage')))
				
				#self.driver.save_screenshot('page_%d.png' % page)
				
				data = self.driver.execute_script('return ctl00_ContentPlaceHolder1_grdSearchRes.Data;')
				
				print '--------------------------------------------------'
				print 'Procesando pagina %d' % page
				print '--------------------------------------------------'
				print "sku: %s - %s" % (sku, data[0][0])
				if sku == data[0][0]:
					print 'Se detecto final de paginas condicion mismo SKU que pagina anterior'
					break;
				
				for row in data:
					try:
						print "ServiceURL" + row[0]
						
						if winProduct == None:
							self.driver.execute_script("$(window.open('ServiceURL" + row[0] + "'))")
							winProduct = self.driver.window_handles[-1]
							self.driver.switch_to.window(winProduct)
						else:
							self.driver.switch_to.window(winProduct);
							self.driver.get("ServiceURL" + row[0])
						
						reintento_interno = 0
						while reintento_interno < 3:
							try:
								WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located((By.ID, 'ctl00_ContentPlaceHolder1_lblHeight')))
								break
							except TimeoutException:
								print "No se pudo cargar pagina ServiceURL" + row[0]
								print "Reintentando"
								reintento_interno = reintento_interno + 1
						
						if reintento_interno == 10:
							print "Dandose por vencido con ServiceURL" + row[0]
							continue
						
						Upc = self.driver.find_element_by_id('ctl00_ContentPlaceHolder1_lblUpc').text
						try:
							dolar = re.search(r': \$(.+) MXP', self.driver.find_element_by_id('ctl00_lblDolar').text).group(1)
						except AttributeError:
							dolar = ''
						
						if dolar_flag == True and dolar != '':
							print 'Dolar'
							print dolar
							self.replace_dolar(dolar)
							dolar_flag = False
						
						almacenes = self.driver.execute_script("return ctl00_ContentPlaceHolder1_grdShipFrom.Data;")
						
						try:
							tab = self.driver.find_element_by_id('ctl00_ContentPlaceHolder1_TabStrip1_6')
							tab.click()
						except:
							print "No se pudo obtener datos de volumen ServiceURL" + row[0]
							continue
							
						
						detalleProducto = self.driver.execute_script('return ctl00_ContentPlaceHolder1_grdDetInfo.Data;')
						dictProducto = {}
						
						for item in detalleProducto:
							dictProducto[item[2]] = item[3]
						
						height_a = self.driver.find_element_by_id('ctl00_ContentPlaceHolder1_lblHeight').text
						height = height_a.replace(" cms","",4)

						width_a = self.driver.find_element_by_id('ctl00_ContentPlaceHolder1_lblWidth').text
						width = width_a.replace(" cms","",4)

						length_a = self.driver.find_element_by_id('ctl00_ContentPlaceHolder1_lblLength').text
						length = length_a.replace(" cms","",4)

						weight_a = self.driver.find_element_by_id('ctl00_ContentPlaceHolder1_lblWeight').text
						weight = weight_a.replace(" grs","",4)
						
						try:
							img1 = self.driver.find_element_by_xpath('//*[@id="photo-zone"]/img[2]')
							thumb = img1.get_attribute('src')
						except:
							thumb = ''

						try:
							img2 = self.driver.find_element_by_xpath('//*[@id="photo-zone"]/img[2]')
							largeTmp = img2.get_attribute('src')
							largeImg = largeTmp.replace("/200", "/300")

						except:
							largeImg = ''
						
						try:
							subCategoria = re.search(r'Subcategor.*a:  (.+)', self.driver.find_element_by_id('ctl00_ContentPlaceHolder1_trPrice').text).group(1)
						except:
							subCategoria = ''
						
						try:
							if self.driver.find_element_by_xpath('//tr[@id="ctl00_ContentPlaceHolder1_trPrice"]//a[@href="/Ingrammicromx/CustomHTML.aspx?id=BKORDRONLY"]'):
								backOrder = 'Si'
							else:
								backOrder = 'No'
						except:
							backOrder = 'No'
						
						try:
							if self.driver.find_element_by_xpath('//tr[@id="ctl00_ContentPlaceHolder1_trPrice"]//img[@src="/IMStoresContent/Shared/Images_Icons/button_special_es-MX_TM01.gif"]'):
								oferta = 'Si'
							else:
								oferta = 'No'
						except:
							oferta = 'No'
						
						inventario = 0
						for almacen in almacenes:
							if almacen[1] == 'Mexico DF':
								inventario = almacen[2]
						
						importe = round(float(row[18]), 2)
						delta = config.delta
						iva = round(importe * 0.16, 2)
						subtotal = round(importe + iva, 2)
						margen = round(subtotal * delta / 100, 2)
						precioFinal = round(subtotal + margen, 2)
						

						if row[13] > 0 and thumb != '' and largeImg != '':
							yield {
							'SKU': row[1],
							'SKU_Proveedor': row[0],
							'Proveedor': 'Ingram',
							'PartNumber': row[1],
							'BrandName': row[7],
							'DescriptionLong': row[11],
							'DescriptionShort': row[11],
							'Categoria': self.categorias_web[self.categoria]['Categoria'],
							'SubCategoria': self.categorias_web[self.categoria]['SubCategoria'],
							'PriceFinal': precioFinal,
							'Stock': row[13],
							'Dolar': dolar,
							'Height': height,
							'Width': width,
							'Lenght': length,
							'Weight': weight,
							'thumb': thumb,
							'largeImg': largeImg
							}
						
					except Exception, e:
						print 'Error al cargar página de producto ignorando'
						print str(e)
				
				sku = data[0][0]
				page = page + 1
				reintento = 1
				
				self.driver.switch_to.window(winOrigen);
				self.driver.execute_script("DoCallback2('Jump%d')" % page)
			except Exception, e:
				print "No se pudo procesar la pagina %d" % page
				#print str(e)
				print "Reintento No. %d" % reintento
				if reintento > 2:
					print "Dandose por vencido demasiados reintentos"
					break
				
				reintento = reintento + 1
				self.driver.switch_to.window(winOrigen);
				self.driver.execute_script("DoCallback2('Jump%d')" % page)
		
		self.driver.close()
		
	def login(self):
		keyData = base64.b64decode(self.key).split(':')
		
		user = self.driver.find_element_by_name('UserName')
		user.send_keys(keyData[0])
		
		passwd = self.driver.find_element_by_name('txtPassword')
		passwd.send_keys(keyData[1])

		cerrar = self.driver.find_element_by_xpath('//a[contains(@onclick, "eplHideLayer")]')
		print 'Cerrar'
		print cerrar.text
		cerrar.click()
		self.driver.save_screenshot('login.png')
		
		button = self.driver.find_element_by_name('LoginButton')
		button.click()

class CsvExportPipeline(object):

	def __init__(self):
		self.filesCSV = {}
		self.filesJSON = {}
	
	@classmethod
	def from_crawler(cls, crawler):
		pipeline = cls()
		crawler.signals.connect(pipeline.spider_opened, signals.spider_opened)
		crawler.signals.connect(pipeline.spider_closed, signals.spider_closed)
		return pipeline
	
	def spider_opened(self, spider):
		ruta = os.path.dirname(os.path.realpath(__file__))
		fileCSV = open('%s/ingram_%s.csv' % (ruta, spider.categoria), 'w+b')
		#fileJSON = open('%s/%s_%s.json' % (ruta, spider.name, systemTime.strftime('%d_%m_%Y_%H_%M_%S')), 'w+b')
		self.filesCSV[spider] = fileCSV
		#self.filesJSON[spider] = fileJSON
		self.exporterCSV = CsvItemExporter(fileCSV)
		#self.exporterJSON = JsonLinesItemExporter(fileJSON)
		self.exporterCSV.start_exporting()
		#self.exporterJSON.start_exporting()
	
	def spider_closed(self, spider):
		self.exporterCSV.finish_exporting()
		#self.exporterJSON.finish_exporting()
		fileCSV = self.filesCSV.pop(spider)
		#fileJSON = self.filesJSON.pop(spider)
		fileCSV.close()
		#fileJSON.close()
	
	def process_item(self, item, spider):
		self.exporterCSV.export_item(item)
		#self.exporterJSON.export_item(item)
		return item
	
class CustomOptionParser(OptionParser):
	def format_epilog(self, formatter):
		return self.epilog

def main():
	prog = os.path.basename(sys.argv[0])
	usage = "Como usar: %prog [options]"
	epilog = "\nEjemplo de uso:\n  Para correr el proceso en la categoria de Computadoras\n    %s -c Computadoras\n    %s --categoria=Computadoras\n  Si queremos que inicie en la pagina 10 de la categoria Computadoras\n    %s -c Computadoras -p 10\n    %s --categoria=Computadoras --pagina=10\n\n" % (prog, prog, prog, prog)
	
	parser = CustomOptionParser(usage, add_help_option=False, epilog=epilog)
	parser.add_option("-h", "--help", action="help", help="Muestra esta ayuda y termina la ejecucion")
	parser.add_option("-c", "--categoria", type="string", help="Para enviar la categoria a procesar, este dato es requerido")
	parser.add_option("-p", "--pagina", type="int", default=1, help="Para iniciar el proceso en una pagina determinada")
	parser.add_option("-l", "--lista", action="store_true", default=False, help="Para mostrar el listado de las categorias")
	
	(options, args) = parser.parse_args()
	
	if options.lista:
		categorias = [
			'Discos Duros1', 'Discos Duros2', 'Discos Duros3', 	'Memorias1',
			'Memorias2', 'Memorias3', 'Monitores', 'Cables y Adaptadores',
			'Dispositivos de Entrada', 'Telecomunicaciones1', 'Telecomunicaciones2',
			'Software', 'Gamer', 'Impresion y Copiado1', 'Impresion y Copiado2',
			'Impresion y Copiado3', 'Laptop1', 'Laptop2', 'PC', 'AllInOne',
			'Tablets', 'Pantallas1', 'Pantallas2', 'TV', 'Camaras', 'Audio',
			'Video', 'No Break/Reguladores', 'Punto de Venta', 'Sistemas de Vigilancia',
			'Hogar', 'Oficina', 'Apple'
		]
		print '\n'.join(categorias)
		return
	
	if options.categoria == None:
		parser.error('El parametro categoria es requerido ejecute %s -h para ver todas las opciones' % prog)
	else:
		categoria = options.categoria
	print "Categoria: %s" % categoria
	pagina = options.pagina
	
        display = Display(visible=0, size=(1200, 720))
        display.start()
	
	# set up crawler
	settings = {'LOG_ENABLED': False, 'ITEM_PIPELINES':{'ingram_productos.CsvExportPipeline': 100}, 'USER_AGENT': 'Mozilla/5.0 (Windows NT 6.3; rv:36.0) Gecko/20100101 Firefox/36.0'}
	crawler = CrawlerProcess(settings)
	
	# schedule spider
	crawler.crawl(ProductSpider, categoria=categoria, pagina=pagina)
	
	# start engine scrapy/twisted
	print "STARTING ENGINE"
	crawler.start()
	print "ENGINE STOPPED"
	display.stop()
 
 
if __name__ == '__main__':
	main()

