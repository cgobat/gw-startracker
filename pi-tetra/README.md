# Tetra

##Try Tetra Out
Test Tetra before you download it with the web demo: <a href="http://tetra.rocks" target="_blank">tetra.rocks</a>.



##Before Run
Install the following python packages:
1. numpy
2. image
3. scipy




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
1. Install full version of Python3: https://www.python.org/downloads/source/
2. Install following packages on the Raspberry Pi:
(?) 2.1. Setuptools: https://pypi.python.org/pypi/setuptools#downloads
2.2. PiCamera: https://github.com/waveform80/picamera
2.3. Cython: https://github.com/cython/cython
2.4. Numpy: https://github.com/numpy/numpy
2.5. Scipy: https://github.com/scipy/scipy







