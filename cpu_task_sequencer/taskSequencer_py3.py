from multiprocessing import Process
import sys
import os
import subprocess

# This function runs a task
def run_task():
    print ("task_begin")
    subprocess.call("stangGabe_stochasticProcess.py", shell=True)
    print ("task_over")

# The code after this if statement will only run once.
# When another process is called it will trigger this if statement
# and pass it because it is not the "original" instance.
if __name__ == '__main__':
    # Create an array to hold all of the processes
    processes = []

    for m in range(4):
        # This if statement
        p = Process(target=run_task, args=())
        print ("befstart")
        p.start()
        print ("afterstart")
        processes.append(p)

    print ("waiting")

    for p in processes:
        p.join()
        print("join")

    print ("end")

#async allowed -- yes
#
