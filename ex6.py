# There are 10 types of people.
# NOTE: %d = integer formatting
x = "There are %d types of people." % 10
binary = "binary"
do_not = "don't"
# Those who know binary and those who don't.
# NOTE: %s = string formatting
y = "Those who know %s and those who %s." % (binary, do_not)

print x
print y

# NOTE: %r is all-purpose formatting, usually used for debugging
print "I said: %r." % x
print "I also said: '%s'." % y

hilarious = False
joke_evaluation = "Isn't that joke so funny?! %r"

# Woahhh, you can pass a parameter directly when you print, too!
print joke_evaluation % hilarious

w = "This is the left side of..."
e = "a string with a right side."

# Concatenation, awee yeee
print w + e