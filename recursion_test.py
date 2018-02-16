import sys

def fib_sum(l):

    # Base cases
    if l == 0:
        sys.stdout.write('0 ')
        return 0
    if l == 1:
        sys.stdout.write('1 ')
        return 1
    if l == 2:
        sys.stdout.write('2 ')
        return 2

    # Equation
    return 2 * fib_sum(l - 1) - fib_sum(l - 3)

print ""
print fib_sum(30)
