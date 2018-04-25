import math  #this gives acces to math.pi

""" in this statement I formatted in the value 5 instead of leaving it as a
string because it is easier to read that way and makes it apparent to the
programmer that 5 is an int. """
print "The circumference of a circle with radius {}u is {}u".format(5, math.pi*5*2)

# The equal sign after time_seconds makes the value equal to zero if not included
# when calling the function.  This makes the code more reusable.
def string_calc_move_speed(distance_km, time_min, time_seconds=0):
    # convert time_min and time_seconds to time_hours
    time_hours = time_seconds / 3600 + time_min / 60

    return "Move speed is {} km/h".format(distance_km / time_hours)

print string_calc_move_speed(10, 45, 30)
