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
import Image

# ---------------
# IMG TO BINARY
# ---------------

def img2bin( imgpath, imgout ) :
	try:
	    im = Image.open(imgpath)	    
	except IOError:
	    print("Image file not found")
	else:
		x,y = im.size

		for i in range(x):
			for j in range(y):
				r,g,b = im.getpixel((i,j))
				if( (r+g+b)/3 < 125 ) :
					im.putpixel((i,j),(0,0,0))
				else:
					im.putpixel((i,j),(255,255,255))
		if imgout: im.save(imgout)

# ---------------
# SERIAL CONECTION
# ---------------
def main() :
	ser = serial.Serial('COM1')
	ser.baudrate = 115200
	ser.bytesize = serial.EIGHTBITS
	ser.parity = serial.PARITY_NONE
	ser.stopbits = serial.STOPBITS_ONE
	ser.xonxoff = False

	if not ser.isOpen():
		ser.open()

	if len(sys.argv) > 1 :
		try:
			#abrir imagen
			im = Image.open(sys.argv[1])
		except IOError:
		    print("Image file not found")
		else:
			x,y = im.size

			for i in range(x):
				for j in range(y):
					r,g,b = im.getpixel((i,j))
					if( (r+g+b)/3 < 125 ) :
						im.putpixel((i,j),(0,0,0))
						ser.write('0')
					else:
						im.putpixel((i,j),(255,255,255))
						ser.write('1')

			ser.close()
	else :
		print( "Image File argument expected" )


main()