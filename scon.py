#-----------------------------------------------------------------------------
# Name:        serial.py
# Purpose:	   Conexion serial
# 
# Contribute:  https://github.com/jonalvarezg/pyserial-conection.git
#
# Author:      Juan David Corrales- Jonathan Alvarez
#
# Created:     18/09/2012
# Copyright:   (c) Juan David Corrales - Jonathan Alvarez 2012
# Licence:     Free share
#-----------------------------------------------------------------------------

import serial
import sys
import binascii

# ---------------
# IMG TO BINARY
# ---------------

def img2bin( imgpath ) :
	try:
	    fin = open(imgpath, "rb")
	    data = fin.read()
	    fin.close()
	except IOError:
	    print("Image file %s not found" % imageFile)
	else :
		# convert every byte of data to the corresponding 2-digit hexadecimal
		hex_str = str(binascii.hexlify(data))
		# now create a list of 2-digit hexadecimals
		hex_list = []
		bin_list = []
		for ix in range(2, len(hex_str)-1, 2):
		    hex = hex_str[ix]+hex_str[ix+1]
		    hex_list.append(hex)
		    bin_list.append(bin(int(hex, 16))[2:])
		#print(bin_list)
		bin_str = "".join(bin_list)
		return bin_list

# ---------------
# SERIAL CONECTION
# ---------------
debug = True

ser = serial.Serial('COM1')
ser.baudrate = 9600
ser.bytesize = serial.EIGHTBITS
ser.parity = serial.PARITY_NONE
ser.stopbits = serial.STOPBITS_ONE
ser.xonxoff = False

if not ser.isOpen():
	ser.open()

if len(sys.argv) > 1 :
	try:
		#abrir imagen
		img_bin = img2bin(sys.argv[1])
		
		#Normalizar y escribir a 8bits,
		if debug : s = ''
		for b in img_bin :
			while len( b ) < 8 :
				b = '0' + b
			if debug : s += b + ', '
			ser.write(bytes( b, encoding = 'ascii') )
		if debug : print( s )

	except IOError:
	    print("Image file %s not found" % imageFile)
	else:
		print( "Dato enviado")
		ser.close()
else :
	print( "Image File argument expected" )