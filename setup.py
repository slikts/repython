#!/usr/bin/env python

import os
from distutils.core import setup


def read(filename):
    return open(os.path.join(os.path.dirname(__file__), filename)).read()

setup(name='repython',
	version='0.1',
	description='Tool to restart commands based on filesystem changes',
	author='Reinis Ivanovs',
	author_email='dabas@untu.ms',
	url='https://github.com/slikts/repython',
	packages=['repython'],
	keywords='cli restart inotify monitor',
	license='BSD',
	long_description=read('README.md'),
	# http://pypi.python.org/pypi?%3Aaction=list_classifiers
	classifiers=[
		'Development Status :: 3 - Alpha',
		'Environment :: Console',
		'Intended Audience :: Developers',
		'License :: OSI Approved :: BSD License',
		'Operating System :: POSIX',
		'Programming Language :: Python',
		'Topic :: Software Development',
		'Topic :: Utilities',
	],
	install_requires=['pyinotify', 'twiggy'],
)
