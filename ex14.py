# argument variable, allows you to pass in args from command line (i.e. python ex14.py username)
from sys import argv

# unpack argv into script and user name
script, user_name = argv
# make it easier to use user prompt by using a variable
prompt = '> '

print "Hi %s, I'm the %s script." % (user_name, script)
print "I'd like to ask you a few questions."
print "Do you like me, %s?" % user_name
likes = raw_input(prompt)

print "Where do you live, %s?" % user_name
lives = raw_input(prompt)

print "What kind of computer do you have?"
computer = raw_input(prompt)

# Using formatters in line-entry string
print """
Alright, so you said %r about liking me.
You live in %r. Not sure where that is.
And you have a %r computer. Nice.
""" % (likes, lives, computer)