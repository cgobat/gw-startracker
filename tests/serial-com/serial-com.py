# Serial Com Example

# First config the Pi to use Serial Port
# Serial port should be enabled but deattached from console
# http://www.instructables.com/id/Read-and-write-from-serial-port-with-Raspberry-Pi/

import time
import serial

ser = serial.Serial(port='/dev/ttyAMA0', baudrate = 57600, parity=serial.PARITY_NONE, stopbits=serial.STOPBITS_ONE, bytesize=serial.EIGHTBITS, timeout=1)
print("\nSerial Port Ready!\n")

counter = 0
while 1:
	x=ser.readline()
	if(len(x)>0):
		print( x  )
		print("Sending a response "+str(counter)+"\n")
		ser.write(b"A response from from RPi...")
		counter += 1
		time.sleep(1)
