# This function requests an int from the user and can make sure it is within the specified bounds.
# (Bounds are both inclusive, Largest allow is MAX, smallest allowed is MIN)
# if bounds are not included it does not do bounds checking
def get_user_int (message_string, min="NaN", max="NaN"):
    """Get an int from the user between a min and max value, (both inclusive.)"""
    if min == "NaN" or max == "NaN":
        # Query user input with a try catch in a while loop
        while True:
            # try catch statements (in this case try execpt statements) will run specific
            # code, (and skip code,) if a error is caught.
            try:
                # raw_input() returns user typed input while printing a mesage at the same time.
                out_value = int(input(message_string + "\nPlease type an INTEGER: "))

                # This line is only reached when the input is a valid string and
                # doesn't raise an exception.
                return out_value  # The function ends when return is called.
            except ValueError:
                print( "Oops!  That was not a valid INTEGER.  Try again... \n" )  # These brackets make this python 3.0 safe.
    else:
        # Query user input with a try catch in a while loop
        while True:
            # try catch statements (in this case try execpt statements) will run specific
            # code, (and skip code,) if a error is caught.
            try:
                # raw_input() returns user typed input while printing a mesage at the same time.
                out_value = int(input(message_string + "\nPlease type an INTEGER between {} and {} (both inclusive): ".format(min, max)))

                # This line is only reached when the input is a valid string and
                # doesn't raise an exception.
                if out_value > max:
                    print( "Oops!  That number was too LARGE.  Try again... \n" )  # These brackets make this python 3.0 safe.
                elif out_value < min:
                    print( "Oops!  That number was too SMALL.  Try again... \n" )  # These brackets make this python 3.0 safe.
                else:
                    return out_value  # The function ends when return is called.
            except ValueError:
                print( "Oops!  That was not a valid INTEGER.  Try again... \n" )  # These brackets make this python 3.0 safe.
