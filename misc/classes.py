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


# Students list
students = [
{ "name" : "Bob", "age" : 14, "gender" : "Male", "gpa" : 3.7 },
{ "name" : "Dan", "age" : 14, "gender" : "Male", "gpa" : 5 },
{ "name" : "Josh", "age" : 12, "gender" : "Male", "gpa" : 4.1 },
{ "name" : "Kite", "age" : 13, "gender" : "Female", "gpa" : 3.8 },
{ "name" : "Gon", "age" : 12, "gender" : "Male", "gpa" : 2.7 },
{ "name" : "Tanaka", "age" : 15, "gender" : "Female", "gpa" : 1 },
{ "name" : "Yuri", "age" : 12, "gender" : "Female", "gpa" : 2 },
{ "name" : "Trish", "age" : 13, "gender" : "Female", "gpa" : 3.8},
{ "name" : "Sam", "age" : 12, "gender" : "Male", "gpa" : 3.7 },
{ "name" : "Ashley", "age" : 18, "gender" : "Female", "gpa" : 3.4 },
]

print students[4-1]["name"]

# Student class
class student:
    # Input a name, age, gender, and gpa for the student object.
    def __init__(self, name, age, gender, gpa):
        self.m_name = name
        self.m_age = age
        self.m_gender = gender
        self.m_gpa = gpa

    # Return student properties as a string
    def __str__(self):
        return "name : {}, age : {}, gender : {}, gpa : {}".format(self.m_name, self.m_age, self.m_gender, self.m_gpa)

    def __int__(self):
        return 1337

tall_kid = student("ben", 7, "male", 5.3)

# OK it works
print tall_kid


# loops and does a thing
class loop:
    def __init__(self, loops):
        self.m_loops = loops
        self._list = []

    def add_thing(self, student):
        self._list += [student]

    def do_thing(self, index):
        self._list[index].m_name = "adgasdgasdg ffaysdkj asdgasdgasdffffgasdgasdg"

    def start_loop(self):
        for index in range(self.m_loops):
            self.add_thing(student("adgasdgasdg", 23412, "adfasdfgasd", 528070.143))
            self.do_thing(index)

# Start
import time

now = time.time()

looper = loop(1000000)
looper.start_loop()

# End
print str(time.time() - now) + "s : Class Ver"

# Start
now = time.time()

# list
temp = []

for index in range(1000000):
    temp += [student("adgasdgasdg", 23412, "adfasdfgasd", 528070.143)]
    temp[index].m_name = "adgasdgasdg ffaysdkj asdgasdgasdffffgasdgasdg"

# End
print time.time() - now
