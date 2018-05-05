#!/usr/local/bin/python2

# Update all pip installed packages for Python 2

import pkg_resources
from subprocess import call

dists = [d for d in pkg_resources.working_set]
for dist in dists:
    call("python2 -m pip install --upgrade " + dist.project_name, shell=True)
    