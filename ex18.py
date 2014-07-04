# Author: Justin Gagne
# Date: July 4, 2014
# File: ex18.py
# Usage: python ex18.py
# Description: introduces functions; prints text using dynamic-param, multi-param, single-param, and no-param functions

# this one is like your scripts with argv; * lets you decompose args... rarely used
def print_two(*args):
	arg1, arg2 = args
	print "arg1: %r, arg2: %r" % (arg1, arg2)

# ok, that *args is actually pointless, we can just do this... this version is used more often
def print_two_again(arg1, arg2):
	print "arg1: %r, arg2: %r" % (arg1, arg2)

# this just takes one argument
def print_one(arg1):
	print "arg1: %r" % arg1

# this one takes no arguments
def print_none():
	print "I got nothin'."


print_two("Zed", "Shaw")
print_two_again("Zed", "Shaw")
print_one("First!")
print_none