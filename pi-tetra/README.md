# Tetra

##Try Tetra Out
Test Tetra before you download it with the web demo: <a href="http://tetra.rocks" target="_blank">tetra.rocks</a>.



##Run Tetra on Your Personal Computer

1. Create a directory (i.e. Tetra).
2. Place tetra.py in the directory.
3. Place Yale's Bright Star Catalog in the directory: <a href="http://tdc-www.harvard.edu/catalogs/BSC5" target="_blank">BSC5</a>
4. Create a subdirectory called 'pics'
5. Place images in 'pics' such as this one: <a href="http://i.imgur.com/7qPnoi1.jpg" target="_blank">Aurora</a>
6. Run 'python tetra.py'

The first run may take a while as it needs to generate the catalog.  From then on, the majority of the runtime will be taken up by loading the catalog into memory and image processing.



##Run Tetra on Raspberry Pi
Once with Raspbian installed and running on Raspberry Pi:
1. Enable Picamera:
	- run: sudo raspi-config
	- Select "Interfacing Options"
	- Select "P1 Camera"
	- Select "Yes"
	- Exit
2. Install full version of Python3
3. Install pip3
4. Install following packages using pip3:
	- picamera
	- pillow
	- numpy
	- scipy


#Posible Errors and solutions:
Error: "libf77blas.so.3: cannot open shared object file"
Solution:  sudo apt-get install libatlas-base-dev

Error: "ImportError: libopenjp2.so.7"
Solution: sudo apt-get install libopenjp2-7-dev

Error: "ImportError: libtiff.so.5"
Solution: sudo apt-get install libtiff5 





