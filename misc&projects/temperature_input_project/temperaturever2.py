
#variables
temp = 0 #user input for conversion
temp_converted = 0  #converted temperature
temp_type = 0
name_list = ["C", "F"]
eq_list = ["temp * 1.8 + 32", "(temp - 32) / 1.8"]

#checks for valid input on conversion
def check_conv_type ():
    global temp_type
    while True:
         try:
             #choice of conversion input
             print "type 1 for C to F \ntype 2 for F to C "
             temp_type = int(raw_input("Input Value: "))

             print ""

             #makes sure 1 or 2
             if temp_type == 1 or temp_type == 2:
                 break  #stop running code here
             else:
                 print "Oops! that was not 1 or 2\n"
         except ValueError:
             print "\nOops!  That was not the correct type.  Try again...\n"

#if user enters wrong input, asks to try again
def check_temp_val ():
    global temp_type, temp
    while True:
         try:
             #check for C-F or F-C conversion
             if temp_type == 1:
                 temp = float(raw_input("Enter temperature in C: "))
             elif temp_type == 2:
                 temp = float(raw_input("Enter temperature in F: "))

             print ""
             break  #stop running code after
         except ValueError:
             print "\nOops!  That was no valid number.  Try again...\n"

while True:
    #checks for valid input on conversion type
    check_conv_type()

    #check for valid temperature value
    check_temp_val()

    #converts one unit to another using the list (eq_list)
    temp_converted = str(eval(eq_list[temp_type-1])) + " degrees "


    #output
    print temp_converted
    print ""
