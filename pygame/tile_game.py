#import pygame  # Import the pygame library.

#pass  # This line is skipped.


# The animal class holds animal specific behaviour (like colour or size)
class Animal:
    extinct = []

    def __init__(self, colour, height_meters):
        self._colour = colour

        # This code makes sure that the height_meters variable is a "number" value.
        try:
            self._height = float(height_meters)
        except:
            print "ERR 0: Incorrect Value for _height. _height initialized to 0 meters."
            self._height = 0

    def get_height_string(self):
        return "The height of this animal is {} meters".format(self._height)

    def get_colour_string(self):
        return "The colour of this animal is {}".format(self._colour)
#end

# The dog class holds dog specific information (like name)
class Pet(Animal):
    def __init__(self, name, colour, height_meters):
        self._name = name

        # Calls the parent constructor.
        Animal.__init__(self, colour, height_meters)

    def get_name_string(self):
        return "The name of this pet is {}".format(self._name)
#end

# The beast class holds dog specific information (like sound)
class Beast(Animal):
    def __init__(self, sound, colour, height_meters):
        self._sound = sound

        # Calls the parent constructor.
        Animal.__init__(self, colour, height_meters)

    def get_sound_string(self):
        return "The sound this beast makes is {}".format(self._sound)
#end

# Instantiate boar object
bill_the_boar = Beast("rahhwr", "brown", 50)
harry_the_boar = Beast("rahhwr", "brown", 50)
sam_the_boar = Beast("rahhwr", "brown", 50)

# boars are extinct therefore all animals should be dead
bill_the_boar.extinct.append("yeas")
harry_the_boar.extinct.append("weah")

sam_the_boar.extinct[0] = "whohoh"

# check if dead
print bill_the_boar.extinct
print harry_the_boar.extinct
print sam_the_boar.extinct
