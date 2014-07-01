# NOTE: print "text" prints text then \n
# NOTE: print "text", prints text then no \n
# In other words, print WITH comma is like print in c++, print WITHOUT comma is like println in c++
print "How old are you?",
# raw_input() grabs user input
age = raw_input()
print "How tall are you?",
height = raw_input()
print "How much do you weigh?",
weight = raw_input()

# %r = raw formatting, debugging
print "So you're %r old, %r tall, and %r heavy." % (age, height, weight)