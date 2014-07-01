# argv = argument variable; holds arguments you pass to script when you run it
from sys import argv

# unpack contents of argv into 4 variables we can work with
script, first, second, third = argv

# print the contents of the arguments passed in
print "The script is called:", script
print "Your first variable is:", first
print "Your second variable is:", second
print "Your third variable is:", third