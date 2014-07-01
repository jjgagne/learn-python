# import argv so that we can use arguments from command line
from sys import argv

# unpack command line args
script, filename = argv

# Ctrl-C is the break command; file will end executing if user enters Ctrl-C, otherwise continues to line 14
print "We're going to erase %r." % filename
print "If you don't want that, hit CTRL-C (^C)."
print "If you do want that, hit RETURN."

raw_input("?")

# save the filename file object to the variable "target" 
# and use "write" mode, which truncates the file and lets you write to it ('r' = read by default, 'a' = append also available)
print "Opening the file..."
target = open(filename, 'w')

print "Truncating the file... Goodbye!"
# ultimately, using the 'w' mode truncates the file anyway, so no need to truncate again...
# target.truncate()

# prompt user for 3 lines to write to the file
print "Now I'm going to ask you for three lines."
line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")

print "I'm going to write these to the file."
target.write(line1 + "\n" + line2 + "\n" + line3 + "\n")

print "And finally, we close it."
target.close()