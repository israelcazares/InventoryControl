#!/bin/bash


cd /home/ubuntu/proveedores


echo "Eliminando archivos anteriores"
#rm -f almacenamiento.csv
#rm -f desktop.csv
#rm -f gabinetes.csv
#rm -f gamers.csv
#rm -f laptops.csv
#rm -f monitores.csv
#rm -f tablets.csv
#rm -f televisiones.csv

#rm -f ingram/ingram_almacenamiento.csv
#rm -f ingram/ingram_desktop.csv
#rm -f ingram/ingram_gabinetes.csv
#rm -f ingram/ingram_gamers.csv
#rm -f ingram/ingram_laptops.csv
#rm -f ingram/ingram_monitores.csv
#rm -f ingram/ingram_tablets.csv
#rm -f ingram/ingram_televisiones.csv

#rm -f cva/cva_almacenamiento.xml
#rm -f cva/cva_almacenamiento.csv

#rm -f pch/pch_desktop.csv
#rm -f pch/pch_gabinetes.csv
#rm -f pch/pch_gamers.csv
#rm -f pch/pch_laptops.csv
#rm -f pch/pch_monitores.csv
#rm -f pch/pch_tablets.csv
#rm -f pch/pch_televisiones.csv


echo "Obteniendo Productos de Almacenamiento de Ingram"
./ingram/ingram_productos.py -c 'Discos duros1'
./ingram/ingram_productos.py -c 'Discos duros2'
./ingram/ingram_productos.py -c 'Discos duros3'
./ingram/ingram_productos.py -c 'Memorias1'
./ingram/ingram_productos.py -c 'Memorias2'
./ingram/ingram_productos.py -c 'Memorias3'
./ingram/ingram_productos.py -c 'Monitores'
./ingram/ingram_productos.py -c 'Cables y adaptadores'
./ingram/ingram_productos.py -c 'Dispositivo de entrada'
./ingram/ingram_productos.py -c 'Telecomunicaciones1'
./ingram/ingram_productos.py -c 'Telecomunicaciones2'
./ingram/ingram_productos.py -c 'Software'
./ingram/ingram_productos.py -c 'Gamer'
./ingram/ingram_productos.py -c 'Impresion y copiado1'
./ingram/ingram_productos.py -c 'Impresion y copiado2'
./ingram/ingram_productos.py -c 'Impresion y copiado3'
./ingram/ingram_productos.py -c 'Laptop1'
./ingram/ingram_productos.py -c 'Laptop2'
./ingram/ingram_productos.py -c 'PC'
./ingram/ingram_productos.py -c 'All in one'
./ingram/ingram_productos.py -c 'Tablets'
./ingram/ingram_productos.py -c 'Pantallas1'
./ingram/ingram_productos.py -c 'Pantallas2'
./ingram/ingram_productos.py -c 'TV'
./ingram/ingram_productos.py -c 'Camaras'
./ingram/ingram_productos.py -c 'Audio'
./ingram/ingram_productos.py -c 'Video'
./ingram/ingram_productos.py -c 'No break-Reguladores'
./ingram/ingram_productos.py -c 'Punto de Venta'
./ingram/ingram_productos.py -c 'Sistemas Vigilancia'
./ingram/ingram_productos.py -c 'Hogar'
./ingram/ingram_productos.py -c 'Oficina'
./ingram/ingram_productos.py -c 'Apple'


echo "Obteniendo Valor de Dolar de CVA"
./cva/cva_dolar.py

echo "Obteniendo Productos de Almacenamiento de CVA"
#./cva/cva_almacenamiento.py


echo "Obteniendo Valor de Dolar de PCH"
./pch/pch_dolar.py

echo "Obteniendo productos de PCH"
./pch/pch_productos.py -c 'Discos duros1'
./pch/pch_productos.py -c 'Discos duros2'
./pch/pch_productos.py -c 'Memorias'
./pch/pch_productos.py -c 'Monitores'
./pch/pch_productos.py -c 'Cables y adaptadores1'
./pch/pch_productos.py -c 'Cables y adaptadores2'
./pch/pch_productos.py -c 'Cables y adaptadores3'
./pch/pch_productos.py -c 'Cables y adaptadores4'
./pch/pch_productos.py -c 'Dispositivo de entrada1'
./pch/pch_productos.py -c 'Dispositivo de entrada2'
./pch/pch_productos.py -c 'Telecomunicaciones'
./pch/pch_productos.py -c 'Software'
./pch/pch_productos.py -c 'Gamer'
./pch/pch_productos.py -c 'Impresion y copiado1'
./pch/pch_productos.py -c 'Impresion y copiado2'
./pch/pch_productos.py -c 'Laptop1'
./pch/pch_productos.py -c 'Laptop2'
./pch/pch_productos.py -c 'PC1'
./pch/pch_productos.py -c 'PC2'
./pch/pch_productos.py -c 'Tablets'
./pch/pch_productos.py -c 'All in one'
./pch/pch_productos.py -c 'Pantallas'
./pch/pch_productos.py -c 'Camaras1'
./pch/pch_productos.py -c 'Camaras2'
./pch/pch_productos.py -c 'Camaras3'
./pch/pch_productos.py -c 'Camaras4'
./pch/pch_productos.py -c 'Audio1'
./pch/pch_productos.py -c 'Audio2'
./pch/pch_productos.py -c 'Audio3'
./pch/pch_productos.py -c 'Audio4'
./pch/pch_productos.py -c 'Audio5'
./pch/pch_productos.py -c 'Audio6'
./pch/pch_productos.py -c 'Audio7'
./pch/pch_productos.py -c 'No break-Reguladores1'
./pch/pch_productos.py -c 'No break-Reguladores2'
./pch/pch_productos.py -c 'No break-Reguladores3'
./pch/pch_productos.py -c 'No break-Reguladores4'
./pch/pch_productos.py -c 'No break-Reguladores5'
./pch/pch_productos.py -c 'No break-Reguladores6'
./pch/pch_productos.py -c 'Punto de Venta1'
./pch/pch_productos.py -c 'Punto de Venta2'
./pch/pch_productos.py -c 'Punto de Venta3'
./pch/pch_productos.py -c 'Punto de Venta4'
./pch/pch_productos.py -c 'Punto de Venta5'
./pch/pch_productos.py -c 'Punto de Venta6'
./pch/pch_productos.py -c 'Punto de Venta7'
./pch/pch_productos.py -c 'Punto de Venta8'
./pch/pch_productos.py -c 'Sistemas Vigilancia1'
./pch/pch_productos.py -c 'Sistemas Vigilancia2'
./pch/pch_productos.py -c 'Sistemas Vigilancia3'
./pch/pch_productos.py -c 'Sistemas Vigilancia4'
./pch/pch_productos.py -c 'Sistemas Vigilancia5'
./pch/pch_productos.py -c 'Sistemas Vigilancia6'
./pch/pch_productos.py -c 'Sistemas Vigilancia7'
./pch/pch_productos.py -c 'Hogar'
./pch/pch_productos.py -c 'Oficina1'
./pch/pch_productos.py -c 'Oficina2'
./pch/pch_productos.py -c 'Oficina3'
./pch/pch_productos.py -c 'Oficina4'
./pch/pch_productos.py -c 'Oficina5'
./pch/pch_productos.py -c 'Oficina6'
./pch/pch_productos.py -c 'Oficina7'
./pch/pch_productos.py -c 'Oficina8'
./pch/pch_productos.py -c 'Drones1'
./pch/pch_productos.py -c 'Drones2'


echo "Obteniendo productos de CVA"
./cva/cva_productos.py -c 'Discos duros1'
./cva/cva_productos.py -c 'Discos duros2'
./cva/cva_productos.py -c 'Discos duros3'
./cva/cva_productos.py -c 'Memorias1'
./cva/cva_productos.py -c 'Memorias2'
./cva/cva_productos.py -c 'Memorias3'
./cva/cva_productos.py -c 'Memorias4'
./cva/cva_productos.py -c 'Memorias5'
./cva/cva_productos.py -c 'Memorias6'
./cva/cva_productos.py -c 'Memorias7'
./cva/cva_productos.py -c 'Memorias8'
./cva/cva_productos.py -c 'Memorias9'
./cva/cva_productos.py -c 'Memorias10'
./cva/cva_productos.py -c 'Memorias11'
./cva/cva_productos.py -c 'Memorias12'
./cva/cva_productos.py -c 'Memorias13'
./cva/cva_productos.py -c 'Monitores1'
./cva/cva_productos.py -c 'Monitores2'
./cva/cva_productos.py -c 'Monitores3'
./cva/cva_productos.py -c 'Cables y adaptadores1'
./cva/cva_productos.py -c 'Cables y adaptadores2'
./cva/cva_productos.py -c 'Cables y adaptadores3'
./cva/cva_productos.py -c 'Cables y adaptadores4'
./cva/cva_productos.py -c 'Cables y adaptadores5'
./cva/cva_productos.py -c 'Cables y adaptadores6'
./cva/cva_productos.py -c 'Cables y adaptadores7'
./cva/cva_productos.py -c 'Cables y adaptadores8'
./cva/cva_productos.py -c 'Cables y adaptadores9'
./cva/cva_productos.py -c 'Dispositivo de entrada1'
./cva/cva_productos.py -c 'Dispositivo de entrada2'
./cva/cva_productos.py -c 'Dispositivo de entrada3'
./cva/cva_productos.py -c 'Dispositivo de entrada4'
./cva/cva_productos.py -c 'Dispositivo de entrada5'
./cva/cva_productos.py -c 'Dispositivo de entrada6'
./cva/cva_productos.py -c 'Dispositivo de entrada7'
./cva/cva_productos.py -c 'Dispositivo de entrada8'
./cva/cva_productos.py -c 'Dispositivo de entrada9'
./cva/cva_productos.py -c 'Dispositivo de entrada10'
./cva/cva_productos.py -c 'Dispositivo de entrada11'
./cva/cva_productos.py -c 'Dispositivo de entrada12'
./cva/cva_productos.py -c 'Telecomunicaciones1'
./cva/cva_productos.py -c 'Telecomunicaciones2'
./cva/cva_productos.py -c 'Telecomunicaciones3'
./cva/cva_productos.py -c 'Telecomunicaciones4'
./cva/cva_productos.py -c 'Telecomunicaciones5'
./cva/cva_productos.py -c 'Telecomunicaciones6'
./cva/cva_productos.py -c 'Software1'
./cva/cva_productos.py -c 'Software2'
./cva/cva_productos.py -c 'Gamer'
./cva/cva_productos.py -c 'Impresion y copiado1'
./cva/cva_productos.py -c 'Impresion y copiado2'
./cva/cva_productos.py -c 'Impresion y copiado3'
./cva/cva_productos.py -c 'Impresion y copiado4'
./cva/cva_productos.py -c 'Impresion y copiado5'
./cva/cva_productos.py -c 'Impresion y copiado6'
./cva/cva_productos.py -c 'Impresion y copiado7'
./cva/cva_productos.py -c 'Impresion y copiado8'
./cva/cva_productos.py -c 'Impresion y copiado9'
./cva/cva_productos.py -c 'Impresion y copiado10'
./cva/cva_productos.py -c 'Impresion y copiado11'
./cva/cva_productos.py -c 'Laptop1'
./cva/cva_productos.py -c 'Laptop2'
./cva/cva_productos.py -c 'Laptop3'
./cva/cva_productos.py -c 'Laptop4'
./cva/cva_productos.py -c 'Laptop5'
./cva/cva_productos.py -c 'Laptop6'
./cva/cva_productos.py -c 'PC1'
./cva/cva_productos.py -c 'PC2'
./cva/cva_productos.py -c 'PC3'
./cva/cva_productos.py -c 'PC4'
./cva/cva_productos.py -c 'PC5'
./cva/cva_productos.py -c 'PC6'
./cva/cva_productos.py -c 'Tablets1'
./cva/cva_productos.py -c 'Tablets2'
./cva/cva_productos.py -c 'Tablets3'
./cva/cva_productos.py -c 'Tablets4'
./cva/cva_productos.py -c 'Pantallas1'
./cva/cva_productos.py -c 'Pantallas2'
./cva/cva_productos.py -c 'Pantallas3'
./cva/cva_productos.py -c 'TV1'
./cva/cva_productos.py -c 'TV2'
./cva/cva_productos.py -c 'Camaras1'
./cva/cva_productos.py -c 'Camaras2'
./cva/cva_productos.py -c 'Camaras3'
./cva/cva_productos.py -c 'Camaras4'
./cva/cva_productos.py -c 'Camaras5'
./cva/cva_productos.py -c 'Audio1'
./cva/cva_productos.py -c 'Audio2'
./cva/cva_productos.py -c 'Audio3'
./cva/cva_productos.py -c 'Audio4'
./cva/cva_productos.py -c 'Audio5'
./cva/cva_productos.py -c 'Audio6'
./cva/cva_productos.py -c 'Audio7'
./cva/cva_productos.py -c 'Audio8'
./cva/cva_productos.py -c 'Video'
./cva/cva_productos.py -c 'No break-Reguladores1'
./cva/cva_productos.py -c 'No break-Reguladores2'
./cva/cva_productos.py -c 'No break-Reguladores3'
./cva/cva_productos.py -c 'No break-Reguladores4'
./cva/cva_productos.py -c 'No break-Reguladores5'
./cva/cva_productos.py -c 'No break-Reguladores6'
./cva/cva_productos.py -c 'No break-Reguladores7'
./cva/cva_productos.py -c 'No break-Reguladores8'
./cva/cva_productos.py -c 'No break-Reguladores9'
./cva/cva_productos.py -c 'Punto de Venta'
./cva/cva_productos.py -c 'Hogar'
./cva/cva_productos.py -c 'Oficina1'
./cva/cva_productos.py -c 'Oficina2'
./cva/cva_productos.py -c 'Oficina3'
./cva/cva_productos.py -c 'Oficina4'
./cva/cva_productos.py -c 'Oficina5'
./cva/cva_productos.py -c 'Oficina6'
./cva/cva_productos.py -c 'Oficina7'
./cva/cva_productos.py -c 'Oficina8'
./cva/cva_productos.py -c 'Oficina9'
./cva/cva_productos.py -c 'Oficina10'
./cva/cva_productos.py -c 'Oficina11'
./cva/cva_productos.py -c 'Oficina12'
./cva/cva_productos.py -c 'Oficina13'
./cva/cva_productos.py -c 'Oficina14'
./cva/cva_productos.py -c 'Oficina15'
./cva/cva_productos.py -c 'Oficina16'
./cva/cva_productos.py -c 'Oficina17'
./cva/cva_productos.py -c 'Oficina18'
./cva/cva_productos.py -c 'Oficina19'
./cva/cva_productos.py -c 'Drones'

echo "Integrando archivos csv"
./integra.py



echo "Enviando archivos csv por ftp"
HOST='homestore.com'
USER='admin'
PASSWD='password'

ftp -n -v $HOST << EOT
ascii
user $USER $PASSWD
prompt
passive
cd web/homestore.com/public_html/wp-content/uploads/wpallimport/files
put DiscosDuros.csv
put Memorias.csv
put Monitores.csv
put CablesAdaptadores.csv
put DispositivosEntrada.csv
put Telecomunicaciones.csv
put Software.csv
put Gamer.csv
put ImpresionCopiado.csv
put Laptops.csv
put PC.csv
put AllInOne.csv
put Tablets.csv
put Pantallas.csv
put TV.csv
put Camaras.csv
put Audio.csv
put Video.csv
put NoBreak-Reguladores.csv
put PuntoVenta.csv
put SistemasVigilancia.csv
put Hogar.csv
put Oficina.csv
put Apple.csv
bye
EOT

# Eliminar productos antes de importar
#ssh 

echo 'Disparando porcesos de importación'
wget -q -O /dev/null "http://homestore.com/wp-cron.php?import_key=QUIS83j&import_id=19&action=trigger"