#Gabe.S and Jocelyn.G
#DO NOT TOUCH
#variables
temp = 0 #user input for conversion
temp_converted = 0  #converted temperature
temp_type = 0
name_list = ["C -> F", "F -> C"]
eq_list = ["temp * 1.8 + 32", "(temp - 32) / 1.8"]

#checks for valid input on conversion
def check_conv_type ():
    global temp_type
    while True:
         try:
             print "type 0 to create custom temperature"
             #prints out conversion input
             index = 0
             for element in name_list:
                 index += 1
                 print "type {} for {}".format(index, element)

             temp_type = int(raw_input("Input Value: "))

             print ""

             #makes sure temp type valid number
             if temp_type >= 0 and temp_type <= len(name_list):
                 break  #stop running code here
             else:
                 print "Oops! That was not valid number\n"
         except ValueError:
             print "\nOops!  That was not the correct type.  Try again...\n"

#if user enters wrong input, asks to try again
def check_temp_val ():
    global temp_type, temp
    while True:
         try:
             #check for temperature input
             temp = float(raw_input("Enter temperature value: "))

             print ""

             break  #stop running code after
         except ValueError:
             print "\nOops!  That was no valid number.  Try again...\n"

#creates a custom temp
def make_custom_temp ():
    #created temp name variables
    start_name = raw_input("Enter name of temperature: ")
    end_name = raw_input("Enter name of temperature to convert to: ")
    new_name = "{} -> {}".format(start_name, end_name)

    #inputs new equation from user input
    new_equation = raw_input("Enter temperature conversion equation with x being variable converted to:\n")
    new_equation = new_equation.replace("x", "temp")

    #checks if equation creates syntax error
    try:
        temp = 1.0
        eval(new_equation)
    except (SyntaxError, NameError):
        print "\nOops! That was not a valid equation\n"
        return #exits the function

    #adds new name and equation to list
    name_list.append(new_name)
    eq_list.append(new_equation)

    #reports back to user
    print "\nsuccessfully created new equation: {} and {}\n".format(new_name, new_equation)

while True:
    #checks for valid input on conversion type
    check_conv_type()
    #to create new equation
    if temp_type == 0:
        make_custom_temp()
    else:
        #check for valid temperature value
        check_temp_val()

        #converts one unit to another using the list (eq_list)
        temp_converted = str(eval(eq_list[temp_type-1])) + " degrees "


        #output
        print temp_converted
        print ""
