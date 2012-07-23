repython
========

repython is a utility to run a command and then restart it based
on filesystem changes (using pyinotify).

Installation
------------

You can install the repython module using:

    python setup.py install

Usage
-----

Basic example:

	python -m repython "python example.py"

This would open the command in a subprocess and recursively monitor
the current working directory for any changed files matching the *.py
filename pattern. 

For more details please see:

	python -m repython --help
