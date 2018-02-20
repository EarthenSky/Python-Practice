
#variables
temp = 0 #user input for conversion
temp_converted = 0  #converted temperature

while True:
    #checks for valid input on conversion
    while True:
         try:
             #choice of conversion input
             temp_type = int(raw_input("type 1 for C to F \ntype 2 for F to C \nInput Value: "))
             #makes sure 1 or 2
             if temp_type == 1 or temp_type == 2:
                 break  #stop running code here
             else:
                 print "Oops! that was not 1 or 2"
         except ValueError:
             print "Oops!  That was not the correct type.  Try again..."


    #if user enters wrong input, asks to try again
    while True:
         try:
             #check for C-F or F-C conversion
             if temp_type == 1:
                 temp = float(raw_input("Enter temperature in C: "))
             elif temp_type == 2:
                 temp = float(raw_input("Enter temperature in F: "))

             break  #stop running code after
         except ValueError:
             print "Oops!  That was no valid number.  Try again..."


    #converts C-F or F-C
    if temp_type == 1:
        temp_converted = str(temp * 1.8 + 32) + " degrees F"
    elif temp_type == 2:
        temp_converted = str((temp - 32) / 1.8) + " degrees C"

    #output
    print temp_converted
