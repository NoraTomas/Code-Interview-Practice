"""
Task: Write a function fib() that takes an integer n, and returns the nth Fibonacci numbe
fib(0)  # => 0
fib(1)  # => 1
fib(2)  # => 1
fib(3)  # => 2
fib(4)  # => 3
...
"""

def fib(n):
    if (n == 1 or n == 2):
        return 1

    else:
        return fib(n-1) + fib(n-2)

print("The 1st Fibonacci number is: " + str(fib(1)))
print("The 2nd Fibonacci number is: " + str(fib(2)))
print("The 3rd Fibonacci number is: " + str(fib(3)))
print("THe 4th Fibonacci number is: " + str(fib(4)))
print("The 17th Fibonacci number is: " + str(fib(17)))
