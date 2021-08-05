#!/usr/bin/env python

import argparse

parser = argparse.ArgumentParser()
parser.add_argument('file_name', help='the file to read')
parser.add_argument('line_number', type=int, help='the line to print from the file')

args = parser.parse_args()

try:
    lines = open(args.file_name, 'r').readlines()
    line = lines[args.line_number - 1]
except IndexError:
    print("Error: file '%s' doesn't have %i lines." % (args.file_name, args.line_number))
except IOError as err:
    print("Error: %s" % err)
else:
    print(line)
