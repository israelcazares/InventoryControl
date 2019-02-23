#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pandas as pd
import os.path

ruta = os.path.dirname(os.path.realpath(__file__))

df = None

try:
	df_tmp = pd.read_csv('{0}/ingram/ingram_Discos duros1.csv'.format(ruta), index_col=False)
	if not df_tmp.empty:
		df = df_tmp
except:
	pass

try:
	df_tmp = pd.read_csv('{0}/ingram/ingram_Discos duros2.csv'.format(ruta), index_col=False)
	if not df_tmp.empty:
		df = df.append(df_tmp)
except:
	pass

try:
	df_tmp = pd.read_csv('{0}/ingram/ingram_Discos duros3.csv'.format(ruta), index_col=False)
	if not df_tmp.empty:
		df = df.append(df_tmp)
except:
	pass

try:
	df_tmp = pd.read_csv('{0}/pch/pch_Discos duros1.csv'.format(ruta), index_col=False)
	if not df_tmp.empty:
		df = df.append(df_tmp)
except:
	pass

try:
	df_tmp = pd.read_csv('{0}/pch/pch_Discos duros2.csv'.format(ruta), index_col=False)
	if not df_tmp.empty:
		df = df.append(df_tmp)
except:
	pass

if df != None:
	df = df.sort(['SKU', 'PriceFinal'], ascending=True).groupby('SKU', as_index=False).first()
	
	df.set_index('SKU', inplace=True)
	df.to_csv('{0}/DiscosDuros.csv'.format(ruta))

########################################################

df = None

try:
	df_tmp = pd.read_csv('{0}/ingram/ingram_Memorias1.csv'.format(ruta), index_col=False)
	if not df_tmp.empty:
		df = df_tmp
except:
	pass

try:
	df_tmp = pd.read_csv('{0}/ingram/ingram_Memorias2.csv'.format(ruta), index_col=False)
	if not df_tmp.empty:
		df = df.append(df_tmp)
except:
	pass

try:
	df_tmp = pd.read_csv('{0}/ingram/ingram_Memorias3.csv'.format(ruta), index_col=False)
	if not df_tmp.empty:
		df = df.append(df_tmp)
except:
	pass

try:
	df_tmp = pd.read_csv('{0}/pch/pch_Memorias.csv'.format(ruta), index_col=False)
	if not df_tmp.empty:
		df = df.append(df_tmp)
except:
	pass

if df != None:
	df = df.sort(['SKU', 'PriceFinal'], ascending=True).groupby('SKU', as_index=False).first()
	
	df.set_index('SKU', inplace=True)
	df.to_csv('{0}/Memorias.csv'.format(ruta))

########################################################

df = None

try:
	df_tmp = pd.read_csv('{0}/ingram/ingram_Monitores.csv'.format(ruta), index_col=False)
	if not df_tmp.empty:
		df = df_tmp
except:
	pass

try:
	df_tmp = pd.read_csv('{0}/pch/pch_Monitores.csv'.format(ruta), index_col=False)
	if not df_tmp.empty:
		df = df.append(df_tmp)
except:
	pass

if df != None:
	df = df.sort(['SKU', 'PriceFinal'], ascending=True).groupby('SKU', as_index=False).first()
	
	df.set_index('SKU', inplace=True)
	df.to_csv('{0}/Monitores.csv'.format(ruta))

########################################################

df = None

try:
	df_tmp = pd.read_csv('{0}/ingram/ingram_Cables y adaptadores.csv'.format(ruta), index_col=False)
	if not df_tmp.empty:
		df = df_tmp
except:
	pass

try:
	df_tmp = pd.read_csv('{0}/pch/pch_Cables y adaptadores1.csv'.format(ruta), index_col=False)
	if not df_tmp.empty:
		df = df.append(df_tmp)
except:
	pass

try:
	df_tmp = pd.read_csv('{0}/pch/pch_Cables y adaptadores2.csv'.format(ruta), index_col=False)
	if not df_tmp.empty:
		df = df.append(df_tmp)
except:
	pass

try:
	df_tmp = pd.read_csv('{0}/pch/pch_Cables y adaptadores3.csv'.format(ruta), index_col=False)
	if not df_tmp.empty:
		df = df.append(df_tmp)
except:
	pass

try:
	df_tmp = pd.read_csv('{0}/pch/pch_Cables y adaptadores4.csv'.format(ruta), index_col=False)
	if not df_tmp.empty:
		df = df.append(df_tmp)
except:
	pass

if df != None:
	df = df.sort(['SKU', 'PriceFinal'], ascending=True).groupby('SKU', as_index=False).first()
	
	df.set_index('SKU', inplace=True)
	df.to_csv('{0}/CablesAdaptadores.csv'.format(ruta))

########################################################

df = None

try:
	df_tmp = pd.read_csv('{0}/ingram/ingram_Dispositivo de entrada.csv'.format(ruta), index_col=False)
	if not df_tmp.empty:
		df = df_tmp
except:
	pass

try:
	df_tmp = pd.read_csv('{0}/pch/pch_Dispositivo de entrada1.csv'.format(ruta), index_col=False)
	if not df_tmp.empty:
		df = df.append(df_tmp)
except:
	pass

try:
	df_tmp = pd.read_csv('{0}/pch/pch_Dispositivo de entrada2.csv'.format(ruta), index_col=False)
	if not df_tmp.empty:
		df = df.append(df_tmp)
except:
	pass

if df != None:
	df = df.sort(['SKU', 'PriceFinal'], ascending=True).groupby('SKU', as_index=False).first()
	
	df.set_index('SKU', inplace=True)
	df.to_csv('{0}/DispositivosEntrada.csv'.format(ruta))

########################################################

df = None

try:
	df_tmp = pd.read_csv('{0}/ingram/ingram_Telecomunicaciones1.csv'.format(ruta), index_col=False)
	if not df_tmp.empty:
		df = df_tmp
except:
	pass

try:
	df_tmp = pd.read_csv('{0}/ingram/ingram_Telecomunicaciones2.csv'.format(ruta), index_col=False)
	if not df_tmp.empty:
		df = df.append(df_tmp)
except:
	pass

try:
	df_tmp = pd.read_csv('{0}/pch/pch_Telecomunicaciones.csv'.format(ruta), index_col=False)
	if not df_tmp.empty:
		df = df.append(df_tmp)
except:
	pass

if df != None:
	df = df.sort(['SKU', 'PriceFinal'], ascending=True).groupby('SKU', as_index=False).first()
	
	df.set_index('SKU', inplace=True)
	df.to_csv('{0}/Telecomunicaciones.csv'.format(ruta))

########################################################

df = None

try:
	df_tmp = pd.read_csv('{0}/ingram/ingram_Software.csv'.format(ruta), index_col=False)
	if not df_tmp.empty:
		df = df_tmp
except:
	pass

try:
	df_tmp = pd.read_csv('{0}/pch/pch_Software.csv'.format(ruta), index_col=False)
	if not df_tmp.empty:
		df = df.append(df_tmp)
except:
	pass

if df != None:
	df = df.sort(['SKU', 'PriceFinal'], ascending=True).groupby('SKU', as_index=False).first()
	
	df.set_index('SKU', inplace=True)
	df.to_csv('{0}/Software.csv'.format(ruta))

########################################################

df = None

try:
	df_tmp = pd.read_csv('{0}/ingram/ingram_Gamer.csv'.format(ruta), index_col=False)
	if not df_tmp.empty:
		df = df_tmp
except:
	pass

try:
	df_tmp = pd.read_csv('{0}/pch/pch_Gamer.csv'.format(ruta), index_col=False)
	if not df_tmp.empty:
		df = df.append(df_tmp)
except:
	pass

if df != None:
	df = df.sort(['SKU', 'PriceFinal'], ascending=True).groupby('SKU', as_index=False).first()
	
	df.set_index('SKU', inplace=True)
	df.to_csv('{0}/Gamer.csv'.format(ruta))

########################################################

df = None

try:
	df_tmp = pd.read_csv('{0}/ingram/ingram_Impresion y copiado1.csv'.format(ruta), index_col=False)
	if not df_tmp.empty:
		df = df_tmp
except:
	pass

try:
	df_tmp = pd.read_csv('{0}/ingram/ingram_Impresion y copiado2.csv'.format(ruta), index_col=False)
	if not df_tmp.empty:
		df = df.append(df_tmp)
except:
	pass

try:
	df_tmp = pd.read_csv('{0}/ingram/ingram_Impresion y copiado3.csv'.format(ruta), index_col=False)
	if not df_tmp.empty:
		df = df.append(df_tmp)
except:
	pass

try:
	df_tmp = pd.read_csv('{0}/pch/pch_Impresion y copiado1.csv'.format(ruta), index_col=False)
	if not df_tmp.empty:
		df = df.append(df_tmp)
except:
	pass

try:
	df_tmp = pd.read_csv('{0}/pch/pch_Impresion y copiado2.csv'.format(ruta), index_col=False)
	if not df_tmp.empty:
		df = df.append(df_tmp)
except:
	pass

if df != None:
	df = df.sort(['SKU', 'PriceFinal'], ascending=True).groupby('SKU', as_index=False).first()
	
	df.set_index('SKU', inplace=True)
	df.to_csv('{0}/ImpresionCopiado.csv'.format(ruta))

########################################################

df = None

try:
	df_tmp = pd.read_csv('{0}/ingram/ingram_Laptop1.csv'.format(ruta), index_col=False)
	if not df_tmp.empty:
		df = df_tmp
except:
	pass

try:
	df_tmp = pd.read_csv('{0}/ingram/ingram_Laptop2.csv'.format(ruta), index_col=False)
	if not df_tmp.empty:
		df = df.append(df_tmp)
except:
	pass

try:
	df_tmp = pd.read_csv('{0}/pch/pch_Laptop1.csv'.format(ruta), index_col=False)
	if not df_tmp.empty:
		df = df.append(df_tmp)
except:
	pass

try:
	df_tmp = pd.read_csv('{0}/pch/pch_Laptop2.csv'.format(ruta), index_col=False)
	if not df_tmp.empty:
		df = df.append(df_tmp)
except:
	pass

if df != None:
	df = df.sort(['SKU', 'PriceFinal'], ascending=True).groupby('SKU', as_index=False).first()
	
	df.set_index('SKU', inplace=True)
	df.to_csv('{0}/Laptops.csv'.format(ruta))

########################################################

df = None

try:
	df_tmp = pd.read_csv('{0}/ingram/ingram_PC.csv'.format(ruta), index_col=False)
	if not df_tmp.empty:
		df = df_tmp
except:
	pass

try:
	df_tmp = pd.read_csv('{0}/pch/pch_PC1.csv'.format(ruta), index_col=False)
	if not df_tmp.empty:
		df = df.append(df_tmp)
except:
	pass

try:
	df_tmp = pd.read_csv('{0}/pch/pch_PC2.csv'.format(ruta), index_col=False)
	if not df_tmp.empty:
		df = df.append(df_tmp)
except:
	pass

if df != None:
	df = df.sort(['SKU', 'PriceFinal'], ascending=True).groupby('SKU', as_index=False).first()
	
	df.set_index('SKU', inplace=True)
	df.to_csv('{0}/PC.csv'.format(ruta))

########################################################

df = None

try:
	df_tmp = pd.read_csv('{0}/ingram/ingram_All in one.csv'.format(ruta), index_col=False)
	if not df_tmp.empty:
		df = df_tmp
except:
	pass

try:
	df_tmp = pd.read_csv('{0}/pch/pch_All in one.csv'.format(ruta), index_col=False)
	if not df_tmp.empty:
		df = df.append(df_tmp)
except:
	pass

if df != None:
	df = df.sort(['SKU', 'PriceFinal'], ascending=True).groupby('SKU', as_index=False).first()
	
	df.set_index('SKU', inplace=True)
	df.to_csv('{0}/AllInOne.csv'.format(ruta))

########################################################

df = None

try:
	df_tmp = pd.read_csv('{0}/ingram/ingram_Tablets.csv'.format(ruta), index_col=False)
	if not df_tmp.empty:
		df = df_tmp
except:
	pass

if df != None:
	df = df.sort(['SKU', 'PriceFinal'], ascending=True).groupby('SKU', as_index=False).first()
	
	df.set_index('SKU', inplace=True)
	df.to_csv('{0}/Tablets.csv'.format(ruta))

########################################################

df = None

try:
	df_tmp = pd.read_csv('{0}/ingram/ingram_Pantallas1.csv'.format(ruta), index_col=False)
	if not df_tmp.empty:
		df = df_tmp
except:
	pass

try:
	df_tmp = pd.read_csv('{0}/ingram/ingram_Pantallas2.csv'.format(ruta), index_col=False)
	if not df_tmp.empty:
		df = df.append(df_tmp)
except:
	pass

try:
	df_tmp = pd.read_csv('{0}/pch/pch_Pantallas.csv'.format(ruta), index_col=False)
	if not df_tmp.empty:
		df = df.append(df_tmp)
except:
	pass

if df != None:
	df = df.sort(['SKU', 'PriceFinal'], ascending=True).groupby('SKU', as_index=False).first()
	
	df.set_index('SKU', inplace=True)
	df.to_csv('{0}/Pantallas.csv'.format(ruta))

########################################################

df = None

try:
	df_tmp = pd.read_csv('{0}/ingram/ingram_TV.csv'.format(ruta), index_col=False)
	if not df_tmp.empty:
		df = df_tmp
except:
	pass

if df != None:
	df = df.sort(['SKU', 'PriceFinal'], ascending=True).groupby('SKU', as_index=False).first()
	
	df.set_index('SKU', inplace=True)
	df.to_csv('{0}/TV.csv'.format(ruta))

########################################################

df = None

try:
	df_tmp = pd.read_csv('{0}/ingram/ingram_Camaras.csv'.format(ruta), index_col=False)
	if not df_tmp.empty:
		df = df_tmp
except:
	pass

try:
	df_tmp = pd.read_csv('{0}/pch/pch_Camaras1.csv'.format(ruta), index_col=False)
	if not df_tmp.empty:
		df = df.append(df_tmp)
except:
	pass

try:
	df_tmp = pd.read_csv('{0}/pch/pch_Camaras2.csv'.format(ruta), index_col=False)
	if not df_tmp.empty:
		df = df.append(df_tmp)
except:
	pass

try:
	df_tmp = pd.read_csv('{0}/pch/pch_Camaras3.csv'.format(ruta), index_col=False)
	if not df_tmp.empty:
		df = df.append(df_tmp)
except:
	pass

try:
	df_tmp = pd.read_csv('{0}/pch/pch_Camaras4.csv'.format(ruta), index_col=False)
	if not df_tmp.empty:
		df = df.append(df_tmp)
except:
	pass

if df != None:
	df = df.sort(['SKU', 'PriceFinal'], ascending=True).groupby('SKU', as_index=False).first()
	
	df.set_index('SKU', inplace=True)
	df.to_csv('{0}/Camaras.csv'.format(ruta))

########################################################

df = None

try:
	df_tmp = pd.read_csv('{0}/ingram/ingram_Audio.csv'.format(ruta), index_col=False)
	if not df_tmp.empty:
		df = df_tmp
except:
	pass

try:
	df_tmp = pd.read_csv('{0}/pch/pch_Audio1.csv'.format(ruta), index_col=False)
	if not df_tmp.empty:
		df = df.append(df_tmp)
except:
	pass

try:
	df_tmp = pd.read_csv('{0}/pch/pch_Audio2.csv'.format(ruta), index_col=False)
	if not df_tmp.empty:
		df = df.append(df_tmp)
except:
	pass

try:
	df_tmp = pd.read_csv('{0}/pch/pch_Audio3.csv'.format(ruta), index_col=False)
	if not df_tmp.empty:
		df = df.append(df_tmp)
except:
	pass

try:
	df_tmp = pd.read_csv('{0}/pch/pch_Audio4.csv'.format(ruta), index_col=False)
	if not df_tmp.empty:
		df = df.append(df_tmp)
except:
	pass

try:
	df_tmp = pd.read_csv('{0}/pch/pch_Audio5.csv'.format(ruta), index_col=False)
	if not df_tmp.empty:
		df = df.append(df_tmp)
except:
	pass

try:
	df_tmp = pd.read_csv('{0}/pch/pch_Audio6.csv'.format(ruta), index_col=False)
	if not df_tmp.empty:
		df = df.append(df_tmp)
except:
	pass

try:
	df_tmp = pd.read_csv('{0}/pch/pch_Audio7.csv'.format(ruta), index_col=False)
	if not df_tmp.empty:
		df = df.append(df_tmp)
except:
	pass

if df != None:
	df = df.sort(['SKU', 'PriceFinal'], ascending=True).groupby('SKU', as_index=False).first()
	
	df.set_index('SKU', inplace=True)
	df.to_csv('{0}/Audio.csv'.format(ruta))

########################################################

df = None

try:
	df_tmp = pd.read_csv('{0}/ingram/ingram_Video.csv'.format(ruta), index_col=False)
	if not df_tmp.empty:
		df = df_tmp
except:
	pass

if df != None:
	df = df.sort(['SKU', 'PriceFinal'], ascending=True).groupby('SKU', as_index=False).first()
	
	df.set_index('SKU', inplace=True)
	df.to_csv('{0}/Video.csv'.format(ruta))

########################################################

df = None

try:
	df_tmp = pd.read_csv('{0}/ingram/ingram_No break-Reguladores.csv'.format(ruta), index_col=False)
	if not df_tmp.empty:
		df = df_tmp
except:
	pass

try:
	df_tmp = pd.read_csv('{0}/pch/pch_No break-Reguladores1.csv'.format(ruta), index_col=False)
	if not df_tmp.empty:
		df = df.append(df_tmp)
except:
	pass

try:
	df_tmp = pd.read_csv('{0}/pch/pch_No break-Reguladores2.csv'.format(ruta), index_col=False)
	if not df_tmp.empty:
		df = df.append(df_tmp)
except:
	pass

try:
	df_tmp = pd.read_csv('{0}/pch/pch_No break-Reguladores3.csv'.format(ruta), index_col=False)
	if not df_tmp.empty:
		df = df.append(df_tmp)
except:
	pass

try:
	df_tmp = pd.read_csv('{0}/pch/pch_No break-Reguladores4.csv'.format(ruta), index_col=False)
	if not df_tmp.empty:
		df = df.append(df_tmp)
except:
	pass

try:
	df_tmp = pd.read_csv('{0}/pch/pch_No break-Reguladores5.csv'.format(ruta), index_col=False)
	if not df_tmp.empty:
		df = df.append(df_tmp)
except:
	pass

try:
	df_tmp = pd.read_csv('{0}/pch/pch_No break-Reguladores6.csv'.format(ruta), index_col=False)
	if not df_tmp.empty:
		df = df.append(df_tmp)
except:
	pass

if df != None:
	df = df.sort(['SKU', 'PriceFinal'], ascending=True).groupby('SKU', as_index=False).first()
	
	df.set_index('SKU', inplace=True)
	df.to_csv('{0}/NoBreak-Reguladores.csv'.format(ruta))

########################################################

df = None

try:
	df_tmp = pd.read_csv('{0}/ingram/ingram_Punto de Venta.csv'.format(ruta), index_col=False)
	if not df_tmp.empty:
		df = df_tmp
except:
	pass

try:
	df_tmp = pd.read_csv('{0}/pch/pch_Punto de Venta1.csv'.format(ruta), index_col=False)
	if not df_tmp.empty:
		df = df.append(df_tmp)
except:
	pass

try:
	df_tmp = pd.read_csv('{0}/pch/pch_Punto de Venta2.csv'.format(ruta), index_col=False)
	if not df_tmp.empty:
		df = df.append(df_tmp)
except:
	pass

try:
	df_tmp = pd.read_csv('{0}/pch/pch_Punto de Venta3.csv'.format(ruta), index_col=False)
	if not df_tmp.empty:
		df = df.append(df_tmp)
except:
	pass

try:
	df_tmp = pd.read_csv('{0}/pch/pch_Punto de Venta4.csv'.format(ruta), index_col=False)
	if not df_tmp.empty:
		df = df.append(df_tmp)
except:
	pass

try:
	df_tmp = pd.read_csv('{0}/pch/pch_Punto de Venta5.csv'.format(ruta), index_col=False)
	if not df_tmp.empty:
		df = df.append(df_tmp)
except:
	pass

try:
	df_tmp = pd.read_csv('{0}/pch/pch_Punto de Venta6.csv'.format(ruta), index_col=False)
	if not df_tmp.empty:
		df = df.append(df_tmp)
except:
	pass

try:
	df_tmp = pd.read_csv('{0}/pch/pch_Punto de Venta7.csv'.format(ruta), index_col=False)
	if not df_tmp.empty:
		df = df.append(df_tmp)
except:
	pass

try:
	df_tmp = pd.read_csv('{0}/pch/pch_Punto de Venta8.csv'.format(ruta), index_col=False)
	if not df_tmp.empty:
		df = df.append(df_tmp)
except:
	pass

if df != None:
	df = df.sort(['SKU', 'PriceFinal'], ascending=True).groupby('SKU', as_index=False).first()
	
	df.set_index('SKU', inplace=True)
	df.to_csv('{0}/PuntoVenta.csv'.format(ruta))

########################################################

df = None

try:
	df_tmp = pd.read_csv('{0}/ingram/ingram_Sistemas Vigilancia.csv'.format(ruta), index_col=False)
	if not df_tmp.empty:
		df = df_tmp
except:
	pass

try:
	df_tmp = pd.read_csv('{0}/pch/pch_Sistemas Vigilancia1.csv'.format(ruta), index_col=False)
	if not df_tmp.empty:
		df = df.append(df_tmp)
except:
	pass

try:
	df_tmp = pd.read_csv('{0}/pch/pch_Sistemas Vigilancia2.csv'.format(ruta), index_col=False)
	if not df_tmp.empty:
		df = df.append(df_tmp)
except:
	pass

try:
	df_tmp = pd.read_csv('{0}/pch/pch_Sistemas Vigilancia3.csv'.format(ruta), index_col=False)
	if not df_tmp.empty:
		df = df.append(df_tmp)
except:
	pass

try:
	df_tmp = pd.read_csv('{0}/pch/pch_Sistemas Vigilancia4.csv'.format(ruta), index_col=False)
	if not df_tmp.empty:
		df = df.append(df_tmp)
except:
	pass

try:
	df_tmp = pd.read_csv('{0}/pch/pch_Sistemas Vigilancia5.csv'.format(ruta), index_col=False)
	if not df_tmp.empty:
		df = df.append(df_tmp)
except:
	pass

try:
	df_tmp = pd.read_csv('{0}/pch/pch_Sistemas Vigilancia6.csv'.format(ruta), index_col=False)
	if not df_tmp.empty:
		df = df.append(df_tmp)
except:
	pass

try:
	df_tmp = pd.read_csv('{0}/pch/pch_Sistemas Vigilancia7.csv'.format(ruta), index_col=False)
	if not df_tmp.empty:
		df = df.append(df_tmp)
except:
	pass

if df != None:
	df = df.sort(['SKU', 'PriceFinal'], ascending=True).groupby('SKU', as_index=False).first()
	
	df.set_index('SKU', inplace=True)
	df.to_csv('{0}/SistemasVigilancia.csv'.format(ruta))

########################################################

df = None

try:
	df_tmp = pd.read_csv('{0}/ingram/ingram_Hogar.csv'.format(ruta), index_col=False)
	if not df_tmp.empty:
		df = df_tmp
except:
	pass

try:
	df_tmp = pd.read_csv('{0}/pch/pch_Hogar.csv'.format(ruta), index_col=False)
	if not df_tmp.empty:
		df = df.append(df_tmp)
except:
	pass

if df != None:
	df = df.sort(['SKU', 'PriceFinal'], ascending=True).groupby('SKU', as_index=False).first()
	
	df.set_index('SKU', inplace=True)
	df.to_csv('{0}/Hogar.csv'.format(ruta))

########################################################

df = None

try:
	df_tmp = pd.read_csv('{0}/ingram/ingram_Oficina.csv'.format(ruta), index_col=False)
	if not df_tmp.empty:
		df = df_tmp
except:
	pass

if df != None:
	df = df.sort(['SKU', 'PriceFinal'], ascending=True).groupby('SKU', as_index=False).first()
	
	df.set_index('SKU', inplace=True)
	df.to_csv('{0}/Oficina.csv'.format(ruta))

########################################################

df = None

try:
	df_tmp = pd.read_csv('{0}/ingram/ingram_Apple.csv'.format(ruta), index_col=False)
	if not df_tmp.empty:
		df = df_tmp
except:
	pass

if df != None:
	df = df.sort(['SKU', 'PriceFinal'], ascending=True).groupby('SKU', as_index=False).first()
	
	df.set_index('SKU', inplace=True)
	df.to_csv('{0}/Apple.csv'.format(ruta))

########################################################

df = None

try:
	df_tmp = pd.read_csv('{0}/pch/pch_Drones1.csv'.format(ruta), index_col=False)
	if not df_tmp.empty:
		df = df_tmp
except:
	pass

try:
	df_tmp = pd.read_csv('{0}/pch/pch_Drones2.csv'.format(ruta), index_col=False)
	if not df_tmp.empty:
		df = df.append(df_tmp)
except:
	pass

if df != None:
	df = df.sort(['SKU', 'PriceFinal'], ascending=True).groupby('SKU', as_index=False).first()
	
	df.set_index('SKU', inplace=True)
	df.to_csv('{0}/Drones.csv'.format(ruta))

########################################################

