# Subprocess is used instead of popen because it is a newer verison.
# This module lets the program run processes.
import subprocess
# This module lets the program use multiple cores.
import multiprocessing
import sys
import os

# This function runs a task
def run_task():
    subprocess.call("stangGabe_stochasticProcess.py", shell=True)

# The code after this if statement will only run once.
# When another process is called it will import this file and will not
# trigger code in this if statement because it is not the "original" instance.
if __name__ == '__main__':

    print "This program runs cpu hog processes on multiple cores."
    in_val = raw_input("Press enter to continue...")

    # Create an array to hold all of the processes
    processes = []

    # Run 2 processes
    for i in range(2):
        # Create a process to run the other python file.
        p = Process(target=run_task, args=())
        p.start()

        # Add process to array
        processes.append(p)

    # This for loop waits for the processes to be complete.
    for p in processes:
        p.join()
