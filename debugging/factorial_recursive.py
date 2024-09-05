#!/usr/bin/python3
import sys

def factorial(n):
    """
    Calculates the factorial of a given number using recursion.

    Parameters:
    n (int): The number for which to calculate the factorial.

    Returns:
    int: The factorial of the given number. If n is 0, returns 1.
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

# Retrieve the argument from the command line, convert it to an integer, and calculate the factorial
f = factorial(int(sys.argv[1]))

# Print the calculated factorial
print(f)
