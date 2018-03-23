## pi-tetra

import time
from picamera import PiCamera
from tetra import *


camera = PiCamera()
camera.resolution = (240, 240)
camera.start_preview()
print("Camera ready!")
# for image_file_name in glob.glob(image_directory + '/*'):
	
image_file_name = 'pics/temp.jpg'
while True:
	start_millis = int(round(time.time() * 1000))

	camera.capture(image_file_name)

	print(image_file_name)
	result = tetra(image_file_name)
	if( type(result) == list and len(result) == 5 ):
		print("Mismatch probability: %.4g" % result[0])
		print("RA:   %.4f" % result[1])
		print("DEC:  %.4f" % result[2])
		print("ROLL: %.4f" % result[3])
		print("FOV:  %.4f\n" % result[4])
	else:
  		print("Failed to determine attitude")
	
	print("Took " + str(int(round(time.time() * 1000)) - start_millis  ) + " ms\n")
	time.sleep(5)