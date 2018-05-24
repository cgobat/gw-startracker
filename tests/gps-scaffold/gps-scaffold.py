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
		print("$GPRMC,201606.916,V,3554.931,N,07402.499,W,75.5,3.31,240518,,E*4B")
		ser.write(b"$GPRMC,201606.916,V,3554.931,N,07402.499,W,75.5,3.31,240518,,E*4B")
		time.sleep(1)
		
		print("$GPRMC,201607.916,V,3554.932,N,07402.500,W,27.8,3.41,240518,,E*45")
		ser.write(b"$GPRMC,201607.916,V,3554.932,N,07402.500,W,27.8,3.41,240518,,E*45")
		time.sleep(1)
		
		print("$GPRMC,201608.916,V,3554.933,N,07402.502,W,65.6,3.49,240518,,E*49")
		ser.write(b"$GPRMC,201608.916,V,3554.933,N,07402.502,W,65.6,3.49,240518,,E*49")
		time.sleep(1)
		
		print("$GPRMC,201609.916,V,3554.934,N,07402.503,W,94.3,3.45,240518,,E*49")
		ser.write(b"$GPRMC,201609.916,V,3554.934,N,07402.503,W,94.3,3.45,240518,,E*49")
		time.sleep(1)
		
		print("$GPRMC,201610.916,V,3554.935,N,07402.504,W,96.5,3.44,240518,,E*42")
		ser.write(b"$GPRMC,201610.916,V,3554.935,N,07402.504,W,96.5,3.44,240518,,E*42")
		time.sleep(1)
		
		print("$GPRMC,201611.916,V,3554.936,N,07402.506,W,17.4,3.33,240518,,E*4A")
		ser.write(b"$GPRMC,201611.916,V,3554.936,N,07402.506,W,17.4,3.33,240518,,E*4A")
		time.sleep(1)
