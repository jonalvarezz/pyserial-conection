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


# -----------------------------------
# SERIAL CONECTION & IMG TO BINARIZE
# -----------------------------------
def main() :

	# Configuración del Puerto
	ser = serial.Serial('COM1')
	ser.baudrate = 115200
	ser.bytesize = serial.EIGHTBITS
	ser.parity = serial.PARITY_NONE
	ser.stopbits = serial.STOPBITS_ONE
	ser.xonxoff = False
	saveimg = False

	if not ser.isOpen():
		ser.open()

	if len(sys.argv) > 1 :
		if len(sys.argv) >= 3 : saveimg = True

		try:
			im = Image.open(sys.argv[1])
		except IOError:
		    print("Image file not found")
		else:
			x,y = im.size

			if x <= 200 or y <= 200 :
				for i in range(x):
					for j in range(y):
						r,g,b = im.getpixel((i,j))
						if( (r+g+b)/3 < 125 ) :
							if(saveimg): im.putpixel((i,j),(0,0,0))
							ser.write('0')
						else:
							if(saveimg): im.putpixel((i,j),(255,255,255))
							ser.write('1')
				ser.close()

				if saveimg :
					try: im.save( sys.argv[2] )
					except Exception, e: raise e
			else :
				print( "Image Dimensions must be less than 200x200px" )
			
	else :
		print( "Image File argument expected" )


main()