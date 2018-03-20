## pi-tetra
from tetra import *


for image_file_name in glob.glob(image_directory + '/*'):
	print(image_file_name)
	result = tetra(image_file_name)
	if( type(result) == list and len(result) == 5 ):
		print("Mismatch probability: %.4g" % result[0])
		print("RA:   %.4f" % result[1])
		print("DEC:  %.4f" % result[2])
		print("ROLL: %.4f" % result[3])
		print("FOV:  %.4f\n" % result[4])
	else:
  		print("failed to determine attitude\n")



