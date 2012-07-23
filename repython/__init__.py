#!/usr/bin/env python

import sys
from subprocess import Popen
from fnmatch import fnmatch

import twiggy
import pyinotify


class Repython(object):
    """Runs a command, monitors files for changes and restarts the
    command if changes are found
    """

    class EventHandler(pyinotify.ProcessEvent):
        def __init__(self, callback, *args, **kwargs):
            self.callback = callback
            super(Repython.EventHandler, self).__init__(*args, **kwargs)

        def process_IN_CLOSE_WRITE(self, event):
            self.callback(event)

    patterns = ('*.py',)
    directories = ('.',)
    _mask = pyinotify.IN_CLOSE_WRITE

    def __init__(self, patterns, directories, log=None, log_level=None):
        if log is None:
            log = twiggy.log
            twiggy.quickSetup(min_level=log_level, file=sys.stderr)
        self.log = log

        self.patterns = patterns
        self.log.fields(patterns=patterns).debug('using config')
        self.directories = directories
        watch_manager = self._watch_manager = pyinotify.WatchManager()
        handler = self.EventHandler(self.check_file)
        notifier = self._notifier = pyinotify.Notifier(watch_manager, handler)
        for directory in self.directories:
            self.log.fields(directory=directory).debug('watching')
            watch_manager.add_watch(directory, self._mask, rec=True)

    def check_file(self, event):
        """ Callback used in pyinotify process event handler """
        for pattern in self.patterns:
            if fnmatch(event.pathname, pattern):
                break
        else:
            # Skip files that don't match any patterns
            return
        self.log.fields(pathname=event.pathname).info('file changed')
        self.restart()

    def run(self, command):
        self._command = command
        self.log.fields(command=command).info('opening subprocess')
        self.process = Popen(command)
        self.monitor()

    def stop(self):
        self.log.info('terminating subprocess')
        self.process.terminate()

    def restart(self):
        self.stop()
        self.run(self._command)

    def monitor(self):
        self.log.debug('entering monitoring loop')
        self._notifier.loop()
