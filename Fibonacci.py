"""
Task: Write a function fib() that takes an integer n, and returns the nth Fibonacci numbe
fib(0)  # => 0
fib(1)  # => 1
fib(2)  # => 1
fib(3)  # => 2
fib(4)  # => 3
...
"""


def fib_recursive(n):
    memo = {
        0: 0,
        1: 1,
        2: 1
    }

    if n < 0:
        raise ValueError("Index was negative, no such thing as negative index")

    if n not in memo:
        memo[n] = fib_recursive(n-1) + fib_recursive(n-2)

    return memo[n]


def fib_iterative(n):
    prev_prev = 0
    prev = 1

    current = 0

    for _ in range(n-1):
        current = prev_prev + prev
        prev_prev = prev
        prev = current

    return current


if __name__ == '__main__':
    print("The 1st Fibonacci number is: " + str(fib_recursive(1)))
    print("The 2nd Fibonacci number is: " + str(fib_recursive(2)))
    print("The 3rd Fibonacci number is: " + str(fib_recursive(3)))
    print("The 4th Fibonacci number is: " + str(fib_recursive(4)))
    print("The 17th Fibonacci number is: " + str(fib_recursive(17))) #Supposed to be 1597
    print("The 23rd Fibonacci number is: " + str(fib_recursive(23))) #Supposed to be 28657

    print("The 1st Fibonacci number is: " + str(fib_iterative(1)))
    print("The 2nd Fibonacci number is: " + str(fib_iterative(2)))
    print("The 3rd Fibonacci number is: " + str(fib_iterative(3)))
    print("The 4th Fibonacci number is: " + str(fib_iterative(4)))
    print("The 17th Fibonacci number is: " + str(fib_iterative(17)))  # Supposed to be 1597
    print("The 23rd Fibonacci number is: " + str(fib_iterative(23)))  # Supposed to be 28657


