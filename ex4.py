# Total number of cars available
cars = 100
# How many people we can fit in each car
space_in_a_car = 4
# How many people are available to drive a car
drivers = 30
# How many people want to be driven somewhere
passengers = 90
# How many cars will go unused
cars_not_driven = cars - drivers
# How many cars will be used
cars_driven = drivers
# How many total people can be driven, given the number of cars available and number of people can fit in each car
carpool_capacity = cars_driven * space_in_a_car
# How many people we need to fit in each car to make it all happen
average_passengers_per_car = passengers / cars_driven


print "There are", cars, "cars available."
print "There are only", drivers, "drivers available."
print "There will be", cars_not_driven, "empty cars today."
print "We can transport", carpool_capacity, "passengers today."
print "We have", passengers, "to carpool today."
print "We need to put about", average_passengers_per_car, "in each car."