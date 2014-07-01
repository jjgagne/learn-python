# Author: Justin Gagne
# Date: June 30, 2014
# File: ex17.py
# Usage: python ex17.py from_file.txt to_file.txt
# Description: Copies data from from_file.txt to to_file.txt

# import argv, allows command line args
from sys import argv
# import exists, returns True if filename exists, False otherwise
from os.path import exists

# unpack args
script, from_file, to_file = argv

# copy contents of from_file to indata string
indata = open(from_file).read()

# len(str) returns length of string
print "The input file is %d bytes long." % len(indata)

# prints True if to_file is already found, False otherwise
print "Does the output file exist? %r" % exists(to_file)

# write copied data into to_file
open(to_file, 'w').write(indata)