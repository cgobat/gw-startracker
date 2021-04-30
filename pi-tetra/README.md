# Tetra for Raspberry Pi

Tetra originally taken from https://github.com/brownj4/Tetra


Prerequisites:
- Python3
- pipenv 

### Run Tetra for Desktop

Clone This repo and run:
~~~
> pipenv install
> pipenv shell
> python pi-tetra.py
~~~


### Run Tetra on Raspberry Pi
Once with Raspbian installed and running on Raspberry Pi:

1) Enable Picamera:
- run: sudo raspi-config
- Select "Interfacing Options"
- Select "P1 Camera"
- Select "Yes"
- Exit


2) Clone This repo and enable camera in code:

In file pi-tetra.py change line 6:
~~~
use_picamera = True
~~~


3) Run 
~~~
> pipenv install
> pipenv shell
> python pi-tetra.py
~~~


