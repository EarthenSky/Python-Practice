import sys  # Imported for outputting values
from threading import Timer  # Imported for using timers
import time
import random

# This is the flag that keeps the math loop ruinning
g_do_math = True

# This method ends the program and gives an output value
def end_task():
    global g_do_math
    g_do_math = False  # Stop the math loop

# Starts a timer that automatically closes the task when done
def start_task_timer():
    # In the random.randint(x, y) function, x and y are both inclusive values.
    timer = Timer(random.randint(1, 5), end_task)
    timer.start()

# Call the timer start function
start_task_timer()

# This is the cpu hog loop.  It does overly complex math to hog cpu.
while g_do_math:
    random_number = random.randint(1, 10)

    random_number **= random_number
    random_number **= 1/random_number

    #print(mod_value)

#time.sleep(2)

# Creates a random output value
out_value = random.randint(1, 10000) - random.randint(1, 10000)

print("##TASK_OVER##")

sys.exit(out_value)  # Temp output value
