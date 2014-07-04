# Author: Justin Gagne
# Date: July 4, 2014
# File: ex20.py
# Usage: python ex20.py ex20_sample.txt
# Description: Use functions to print an entire file or a file line-by-line

# allow command line args
from sys import argv

# unpack args
script, input_file = argv

# print entire contents of file
def print_all(f):
	print f.read()

# return to the beginning of the file
def rewind(f):
	f.seek(0)

# print one line at a time; readline() reads the line from the current seek position (set to start of file using rewind function above)
# note: could add a comma after readline() to prevent \n\n from occurring
def print_a_line(line_count, f):
	print line_count, f.readline()

# create file object
current_file = open(input_file)

print "First let's print the whole file:\n"

print_all(current_file)

print "Now let's rewind, kind of like a tape."

rewind(current_file)

print "Let's print three lines:"

# NOTE: current_line is just used for debugging purposes and is not actually passed to readline()
current_line = 1
print_a_line(current_line, current_file)

current_line += 1
print_a_line(current_line, current_file)

current_line += 1
print_a_line(current_line, current_file)

# don't forget to close the file afterwards
current_file.close()