#!/usr/bin/env python

import argparse


def repython(command, directories, patterns):
	pass

	
if __name__ == '__main__':
	parser = argparse.ArgumentParser(description='Runs command and restarts it if files maching given patterns are updated')
	parser.add_argument('command', help='run command')
	default_patterns = ['*.py']
	parser.add_argument('-p', '--patterns', 
		help='filename patterns to monitor for changes (default: %s)' % ', '.join(default_patterns),
		nargs='+', default=default_patterns, metavar='PATTERN')
	parser.add_argument('-d', '--directories', 
		help='paths to monitor (default: working directory)',
		nargs='+', default=['.'], metavar='PATH')
	args = parser.parse_args()
	repython(args.command, args.directories, args.patterns)
