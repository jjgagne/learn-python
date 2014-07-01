# pass in prompt text in raw_input... no line break after the string until user hits enter
age = raw_input("How old are you? ")
height = raw_input("How tall are you? ")
weight = raw_input("How much do you weigh? ")

print "So you're %r old, %r tall, and %r heavy." % (age, height, weight)