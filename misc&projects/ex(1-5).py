 # This is a built in python library that gives access to math functions
import math

# Uses pythagorean theorm to find the hypotenuse of a triangle
def find_hypotenuse(a, b):
    return math.sqrt(a ** 2 + b ** 2)

# Inital statement
print "This is a right triangle hypotenuse calculator."

# Define Global input parameters
g_a = 0
g_b = 0

# If the equality statement returns a True value the loop will repeat code inside it.
# Query user input with a try catch in a while loop
valid_input = False
while valid_input == False:
    # try catch statements (in this case try exerpt statements) will run specific
    # code if a error is caught.
    try:
        # raw_input() returns user typed input while printing a mesage at the same time.
        g_a = float(input("Input the length of side A: "))
        g_b = float(input("Input the length of side B: "))

        valid_input = True
    except ValueError:
        print "Oops!  That was not a valid NUMBER.  Try again... \n"
        valid_input = False  # keep the loop repeating because the value was not valid


print "The length of the hypotenuse (side C) is: {}".format(find_hypotenuse(g_a, g_b))
