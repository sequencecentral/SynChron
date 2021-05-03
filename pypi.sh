#!/bin/bash
#Github
git add --all
git commit -am 'pypi upload'
git push

#make an egg
python setup.py bdist_egg

#make pypi dist
python setup.py sdist

#upload pypi
twine upload -u sequencecentral --skip-existing dist/*