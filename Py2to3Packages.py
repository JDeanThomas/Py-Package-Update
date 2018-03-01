#!/usr/local/bin/python2

# Get list of pip installed packages for Python 2 
# Install them for Python 3

import pip
from subprocess import call

for dist in pip.get_installed_distributions():
    call("pip3 install " + dist.project_name, shell=True)