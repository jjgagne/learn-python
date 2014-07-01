name = 'Justin Gagne'
age = 21 # not a lie
height_in = 68 # inches
height_cm = height_in * 2.54
weight = 135 # lbs
eyes = 'brown'
teeth = 'white-ish'
hair = 'black'

print "Let's talk about %s." % name
print "He's %d inches tall, which is the same as %d centimetres." % (height_in, height_cm)
print "He's %d pounds heavy." % weight
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (eyes, hair)
print "His teeth are usually %s depending on the coffee." % teeth

# this line is tricky, try to get it exactly right
print "If I add %d, %d, and %d I get %d." % (age, height_in, weight, age + height_in + weight)