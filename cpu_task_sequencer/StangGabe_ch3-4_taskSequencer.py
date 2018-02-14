'''# Subprocess is used instead of popen because it is a newer verison.
# This module lets the program run processes.
import subprocess
# This module lets the program use multiple cores.
import multiprocessing

print "Task Sequencer"
in_val = raw_input("Press enter to continue...")

# This function runs a task
def run_task():
    subprocess.call("stangGabe_stochasticProcess.py", shell=True)

#run_task();
#run_task();
run_task();

# Instantiate process object
if __na12me__ == '__main__':
    p = multiprocessing.Process(target=run_task, args=())
    p.start()
    p.join()
    '''

##

'''
import subprocess
from multiprocessing import Process
import os

def info(title):
    print title
    print 'module name:', __name__
    if hasattr(os, 'getppid'):  # only available on Unix
        print 'parent process:', os.getppid()
    print 'process id:', os.getpid()

def f(name):
    info('function f')
    print 'hello', name
    subprocess.call("stangGabe_stochasticProcess.py", shell=True)

if __name__ == '__main__':
    info('main line')
    p = Process(target=f, args=('bob',))
    p.start()
    p.join()
    '''

from multiprocessing import Process
import sys
import os

# This function runs a task
def run_task():
    #subprocess.call("stangGabe_stochasticProcess.py", shell=True)
    print "1"
    print "2"
    print "3"
    print "4"
    print "5"

processes = []

if __name__ == '__main__':
    p = Process(target=run_task, args=())
    p.start()
    processes.append(p)
    p.join()

for m in range(1, 3):
    pass

for p in processes:
    #p.join()
    pass



#What does p.join() do?
#async allowed
#
