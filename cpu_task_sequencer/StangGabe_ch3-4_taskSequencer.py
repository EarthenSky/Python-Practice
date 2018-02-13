# subprocess is used instead of popen because it is a newer verison
# This module lets the program run processes
import subprocess
# This module lets the program use multiple cores
import multiprocessing

print "Task Sequencer"
in_val = raw_input("Press enter to continue...")

# This function runs
def run_task():
    subprocess.call("stangGabe_stochasticProcess.py", shell=True)

run_task()
