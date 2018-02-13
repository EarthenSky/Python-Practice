# Initial print statements
print "Name: Gabe Stang"
print "Class: Magic Number 144"
print "Teacher: Mr. Euclid \n"

# "def" is how you define a function / method.
# A function in python may or may not have a return value.

# Outputs a string detailing what numbers were added and the solution
def string_sum(num1, num2):
    return "{} + {} = {}".format(num1, num2, num1 + num2)

# Outputs a string detailing what numbers were multiplied and the solution
def string_mul(num1, num2):
    return "{} * {} = {}".format(num1, num2, num1 * num2)

# Outputs a string detailing what numbers were divided and the solution
def string_div(num1, num2):
    return "{} / {} = {}".format(num1, num2, num1 / num2)

# Outputs a string detailing what number was squared and the solution
def string_sqr(num1):
    return "{}^2 = {}".format(num1, num1 ** 2)


# Problem answers using string.format()
print "1. {}".format(string_sum(144, 144))
print "2. {}".format(string_sum(144, -19))

print "3. {}".format(string_mul(144, 9))
print "4. {}".format(string_div(144, 12))

print "5. {}".format(string_sqr(144))

print "6. {}".format(string_sum(144, 24))
print "7. {}".format(string_sum(144, -45))

print "8. {}".format(string_mul(144, 11))
print "9. {}".format(string_div(144, 70))

"""I think that the spacing makes it easier to read"""
