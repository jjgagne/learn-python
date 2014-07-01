# import argv, which allows user to pass in parameters from command line
from sys import argv

# unpack argv
script, filename = argv

# create file object from the filename file (ex15_sample.txt in this case)
txt = open(filename)

# print out the contents to the console by calling txt.read()
print "Here's your file %r:" % filename
print txt.read()

# since we are done with the file, we should close it
txt.close()

# grab filename from user input
print "Type the filename again:"
file_again = raw_input("> ")

# create new file object from user inputted filename
txt_again = open(file_again)

# then print its contents
print txt_again.read()

# since we are done with the file, we should close it
txt_again.close()