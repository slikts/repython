repython
========

repython is a utility to run a command and then restart it based
on filesystem changes. It's useful for quickly testing changes to a
running program. For instance, Django uses a similar but more
sophisticated method to reload its source code when it detects
a change.

repython uses the pyinotify library to make monitoring for changes
efficient compared to just polling the filesystem.

Installation
------------

Dependencies:

 * [pyinotify](https://github.com/seb-m/pyinotify)
 * [twiggy](http://hg.wearpants.org/twiggy/)

You can install the repython module using:

    $ python setup.py install

repython is also available from Cheese Shop:

	$ pip install repython

Or using setuptools:

	$ easy_install repython

Usage
-----

Basic example:

	$ python -m repython "python example.py"

This would open the command in a subprocess and recursively monitor
the current working directory for any changed files matching the *.py
filename pattern (default behavior).

repython is not limited to running Python programs, so a command like
this should work as well:

    $ python -m repython "ruby example.rb" -p "*.rb" "*.txt"

The `-p` or `--pattern` arguments determine which file changes
trigger restarting the run command.

The `-d` or `--directory` arguments allow monitoring other directories
than the current working directory. It can be used like this:

	$ python -m repython "python example.py" -d . ~/example

This command would make repython recursively (i.e., including
subdirectories) monitor both the working directory and the
`~/example` directory.

The `-v` or `--verbose` argument can be used to get more detailed
output from repython, and the `-q` or `--quiet` argument can be used
to suppress all output.

For more details please see:

	$ python -m repython --help

Known issues
------------

[Python issue #15433](http://bugs.python.org/issue15433) causes the
argument order to be wrong in the generated usage instructions
(shown when using the `--help` argument). The command argument should
come before the optional arguments for the tool to work.
