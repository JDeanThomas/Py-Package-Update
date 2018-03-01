#!/usr/local/bin/python2

# Update all pip installed packages for Python 2

import pip
from subprocess import call

for dist in pip.get_installed_distributions():
    call("python2 -m pip install --upgrade " + dist.project_name, shell=True)
    