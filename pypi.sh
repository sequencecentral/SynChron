#!/bin/bash

#make an egg
python setup.py bdist_egg

#make pypi dist
python setup.py sdist

#upload pypi
twine upload dist/*