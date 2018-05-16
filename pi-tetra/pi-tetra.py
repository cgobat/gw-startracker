# -*- coding: UTF-8 -*-


debug = 0
use_picamera = 0


#################################
###########	 Imports ############
#################################
import sys
if sys.version_info < (3,0):
    print("Requires Python 3.x, not Python 2.x, exiting...\n")
    sys.exit(1)
import time
import glob
import os
import threading


from io import BytesIO


# For profiling
import cProfile
import pstats

# If in Raspberry Pi, use camera; else read files from a folder
picamera_module = False
if use_picamera:
	try:
	    from picamera import PiCamera
	    picamera_module = True	
	except ImportError:
	    picamera_module = False


# If in Raspberry Pi, use serial
try:
    import serial
    serial_com = True
except ImportError:
    serial_com = False



# User import
print("Loading Tetra...")
start_millis = int(round(time.time() * 1000))
from tetra import *
print("Init tetra took:" + str(int(round(time.time() * 1000)) - start_millis  ) + " ms\n")



##################################
#### Const and Global variables	##
##################################

# Cap number of pictures for Testing
max_pics = 5

# store pics in storage
store_pics = True



#################################
###########	 Code	#############
#################################

# If Serial Com Availabe
serial_port = 0
if serial_com:
	serial_port = serial.Serial(port='/dev/ttyAMA0', baudrate = 57600, parity=serial.PARITY_NONE, stopbits=serial.STOPBITS_ONE, bytesize=serial.EIGHTBITS, timeout=1)
	print("\nSerial Port Ready!\n")



# If Camera Module included niit it, else open folder for read image files
if picamera_module:
	# Set Camera configuration
	# these attributes are all relatively expensive to set individually, 
	# hence setting them all upon construction is a speed optimization
	camera = PiCamera(	resolution = (480, 480), 
						framerate = 90, 
						led_pin = False)
	camera.color_effects = (128,128) # turn camera to black and white
	image_file_name_prefix = 'camera_pics/pic_'
	camera_res_X = camera.resolution[0]
	camera_res_Y = camera.resolution[1]
	print("\nCamera ready!\n")
	# Create the in-memory buffer for store incoming pics
	stream = BytesIO()
	time.sleep(2)
else:
	# directory containing input images
	image_directory = './pics'
	image_list =  glob.glob(image_directory + '/*')
	print("\nNo Camera found, reading from folder!\n")


	
def run_tetra():
	i = 0
	t_t = 0
	while i < max_pics:
		start_millis = int(round(time.time() * 1000))

		# For Tetra exit status
		result = 0

		# If Raspberry Pi take picture, else read file
		if picamera_module:
			# Take a picture and store it the stream buffer
			camera.capture(stream, format='rgb', use_video_port=True)			
			# "Rewind" the stream to the beginning so we can read its content
			stream.seek(0)
			# Store image into a numpy array and convert to grayscale
			image = np.array( Image.frombytes('RGB', (camera_res_X,camera_res_Y), stream.getvalue()).convert('L'))
			print("Take pic_"+ str(i)+" took:" + str(int(round(time.time() * 1000)) - start_millis  ) + " ms")
			
			if store_pics:
				image_file_name = image_file_name_prefix + str(i) + '.jpg'
				result = Image.fromarray(image)
				result.save(image_file_name)

			# Call tetra
			result = tetra(image)

		else:
			if len(image_list) == 0	:
				break
			image_file_name = image_list.pop()
			print(image_file_name)
			# Call Tetra 
			result = tetra_from_file(image_file_name)
		
		if( type(result) == list and len(result) == 5 ):
			print("Mismatch probability: %.4g" % result[0])
			print("RA:   %.4f" % result[1])
			print("DEC:  %.4f" % result[2])
			print("ROLL: %.4f" % result[3])
			print("FOV:  %.4f" % result[4])
		else:
	  		print("Failed to determine attitude")

		t_t += int(round(time.time() * 1000)) - start_millis  
		print("Took: t = " + str(int(round(time.time() * 1000)) - start_millis  ) + " ms\n")
		i+=1

	print("\nAverage t = " + str( t_t/max_pics))




def serial_server():
	i = 0
	t_t = 0
	print("Serial Server start")
	while True: 
		# Read serial Port
		in_buffer = serial_port.readline()

		# If nothing in serial port, continue
		if(len(in_buffer)<=0):
			continue

		# If somethin in serial port, check is a valid command
		# A is command to get Star Tracker info
		if(in_buffer.decode()[0] != 'A'):
			print("Invalid command: "+ in_buffer.decode())
			continue

		print("Valid command: " + in_buffer.decode())

		start_millis = int(round(time.time() * 1000))

		# For Tetra exit status
		result = 0

		# If Raspberry Pi take picture, else read file
		if picamera_module:
			# Take a picture and store it the stream buffer
			camera.capture(stream, format='rgb', use_video_port=True)			
			# "Rewind" the stream to the beginning so we can read its content
			stream.seek(0)
			# Store image into a numpy array and convert to grayscale
			image = np.array( Image.frombytes('RGB', (camera_res_X,camera_res_Y), stream.getvalue()).convert('L'))
			print("Take pic_"+ str(i)+" took:" + str(int(round(time.time() * 1000)) - start_millis  ) + " ms")
			
			if store_pics:
				image_file_name = image_file_name_prefix + str(i) + '.jpg'
				result = Image.fromarray(image)
				result.save(image_file_name)

			# Call tetra
			result = tetra(image)

		else:
			if len(image_list) == 0	:
				print("No more images in folder...")
			else:
				image_file_name = image_list.pop()
				print(image_file_name)
				# Call Tetra 
				result = tetra_from_file(image_file_name)
		
		if( type(result) == list and len(result) == 5 ):
			print("Mismatch probability: %.4g" % result[0])
			print("RA:   %.4f" % result[1])
			print("DEC:  %.4f" % result[2])
			print("ROLL: %.4f" % result[3])
			print("FOV:  %.4f" % result[4])

			# Pack Tetra Result to send it to Serial Port
			out_buf = ','.join(str(e) for e in result)

			print("Sending a response: "+out_buf+"\n")
			serial_port.write( out_buf.encode() )

		else:
	  		print("Failed to determine attitude")

	  		# Send Fail Response 'N' to serial port
	  		serial_port.write( b"N" )

		t_t += int(round(time.time() * 1000)) - start_millis  
		print("Took: t = " + str(int(round(time.time() * 1000)) - start_millis  ) + " ms\n")
		i+=1




if __name__ == '__main__':
	if debug:
		temp_prof_out = "{}.profile".format(__file__)
		cProfile.run( "run_tetra()", temp_prof_out )
		s = pstats.Stats(temp_prof_out)
		s.strip_dirs()
		s.sort_stats("time").print_stats(50)
		os.remove( temp_prof_out )
	else:
		serial_server()