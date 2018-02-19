import sys

# This function finds the sum of a fibonacci sequence based on its length
def fib_sum(length):

    # Base cases
    if length == 0:
        sys.stdout.write('0 ')
        return 0
    if length == 1:
        sys.stdout.write('1 ')
        return 1
    if length == 2:
        sys.stdout.write('2 ')
        return 2

    # Equation
    return 2 * fib_sum(length - 1) - fib_sum(length - 3)

print fib_sum(10)
