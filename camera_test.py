import time
import numpy as np
from PIL import Image
from picamera import PiCamera
from io import BytesIO


# Create the in-memory stream
stream = BytesIO()


# Set Camera configuration
# these attributes are all relatively expensive to set individually, 
# hence setting them all upon construction is a speed optimization
camera = PiCamera(	resolution = (480, 480), 
					framerate = 90, 
					led_pin = False)


#camera.color_effects = (128,128) # turn camera to black and white
time.sleep(2)

camera_res_X = camera.resolution[0]
camera_res_Y = camera.resolution[1]


i = 0
t_t = 0
while i < 30:
	start_millis = int(round(time.time() * 1000))

	camera.capture(stream, format='rgb', use_video_port=True)

	capture_t =  int(round(time.time() * 1000))
	print("\nCapture: " + str( capture_t - start_millis ))

	# "Rewind" the stream to the beginning so we can read its content
	stream.seek(0)
	image = np.array( Image.frombytes('RGB', (camera_res_X,camera_res_Y), stream.getvalue()).convert('L'))


	t_t += int(round(time.time() * 1000)) - start_millis  
	print("Convert: " + str(int(round(time.time() * 1000)) - start_millis  ))
	print("Size of array: " + str( image.size )  )
	i +=1
print("\nCamera Stats:\nSensor Mode:" + str(camera.sensor_mode))
print("resolution:" + str(camera.resolution))
print("framerate:" + str(camera.framerate))
print("\nAverage t = " + str( t_t/30))


# Save image ina file
result = Image.fromarray(image)
result.save('out.jpg')





