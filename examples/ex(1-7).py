def convert_temperature_to_celsius(value):
    return (value - 32) * 5 / 9

# init global variable
g_temperature = 0

# Query user input with a try catch in a while loop
valid_input = False
while valid_input == False:
    try:
        # raw_input() returns user typed input while printing a mesage at the same time.
        g_a = float(input("Input the temperature you want to convert to celsius: "))

        valid_input = True
    except ValueError:
        print "Oops!  That was not a valid NUMBER.  Try again... \n"
        valid_input = False  # keep the loop repeating because the value was not valid

print "{} degrees fahrenheit is {} degrees celsius.".format(g_a, convert_temperature_to_celsius(g_a))
