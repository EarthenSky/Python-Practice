# Init constants.
MAP_SIZE = 10
TILE_SIZE = 50

# Init a dictionary to store all positional values.
dict = {}

# Loop through every tile number and assign the positional
# values with the tile number as the key.
for index in range(1, 101):

    # Convert tile number into x, y tile values.
    if index % 20 == 0:
        x = 1
    elif (index % 20) <= 10:
        x = 10 if index % 10 == 0 else (index % 10)  # Uses python's ternary operator.
    else:
        x = 21 - (index % 20)

    y = (index - 1) / 10 + 1

    # Calculate the positional values from the x, y tile values and make them an easy to read string
    dict[index] = ( "(x_loc={}, y_loc={})".format( (x-1) * TILE_SIZE + 1, (MAP_SIZE-y) * TILE_SIZE + 1 ) )

# Query user input in this loop. Input number is the key for the dictionary.
exit_program = False
while not exit_program:
    try:
        # Get user input.
        user_input = int( raw_input("number here: ") );

        # Proccess user input, and output a value.
        print dict[user_input]

        # Exit program.
        exit_program = True

    except ValueError:
        print "Input a whole number. (no decimal, no words)"
    except KeyError:
        print "Input a valid number. (between 1 and 100)"
