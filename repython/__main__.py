#!/usr/bin/env python

from argparse import ArgumentParser

import twiggy
from repython import Repython


def parse_args(args=None):
	# TODO: the argparse usage line is wrong, Python issue #15433
	parser = ArgumentParser(description='Runs command and restarts it if files maching given patterns are updated',
		prog='python -m repython')
	parser.add_argument('command', help='run command')
	parser.add_argument('-p', '--patterns',
		help='filename patterns to monitor for changes (default: %s)' % ', '.join(Repython.patterns),
		nargs='*', default=Repython.patterns, metavar='PATTERN')
	parser.add_argument('-d', '--directories',
		help='paths to monitor (default: working directory)',
		nargs='*', default=Repython.directories, metavar='PATH')
	group = parser.add_mutually_exclusive_group()
	group.add_argument('-v', '--verbose', action='store_true')
	group.add_argument('-q', '--quiet', action='store_true')
	return parser.parse_args(args)


if __name__ == '__main__':
	args = parse_args()
	if args.quiet:
		log_level = twiggy.levels.DISABLED
	elif args.verbose:
		log_level = twiggy.levels.DEBUG
	else:
		log_level = twiggy.levels.INFO
	repython = Repython(args.patterns, args.directories, log_level=log_level)
	try:
		repython.run(args.command.split(' '))
	except KeyboardInterrupt:
		repython.stop()
		raise
