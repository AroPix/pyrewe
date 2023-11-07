# pyrewe
API wrapper for the german grocery store REWE, to be able to order groceries through Python (WIP)

(Code is very crappy so i'm very open to contributions)

# How to use
At the moment there is no Authentication implemented, so login on https://shop.rewe.de, open Chrome developer console (F12), 
change to the network tab, click on your account at the top of the REWE website and copy the cookie from the request header

example_script.py contains a simple terminal ui

# Install Package

Clone the repo:

``git clone https://github.com/AroPix/pyrewe.git``

Install the pip package:

``pip install .``

Import it using:

``from pyrewe import rewe``


