import sys
import time

x = raw_input("start? ")

print 'hello',
sys.stdout.flush()

time.sleep(1)

print '\rhell ',
sys.stdout.flush()

time.sleep(1)

print '\rhasdasdasdasdas \n',
sys.stdout.flush()

time.sleep(1)


x = raw_input("end")
