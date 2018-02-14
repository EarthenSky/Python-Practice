import sys  # Imported for outputting values
from threading import Timer  # Imported for using timers
import time

# This is the flag that keeps the math loop ruinning
g_do_math = True

# This method ends the program and gives an output value
def end_task():
    global g_do_math
    g_do_math = False  # Stop the math loop

def start_task_timer():
    timer = Timer(5.0, end_task)
    timer.start()

# Start a timer that automatically closes the task when done
start_task_timer()

# This is the counter that is incremented to use cpu
inc_value = 0

# This is the cpu hog loop
while g_do_math:
    inc_value += 1
    time.sleep(0.2)
    #print inc_value

#time.sleep(2)

sys.exit(100)  # Temp output value
