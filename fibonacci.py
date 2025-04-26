#-------------------------------------------------------
# Write a Python program to compute the square of the
# first N Fibonacci numbers, using the map function and 
# generate a list of the numbers.
#-------------------------------------------------------

#-------------------------------------------------------
# Functions:
def fibonacci(n):
    fib_sequence = [0, 1]
    for x in range(2,n):
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    return fib_sequence

def square(n):
    return n ** 2
#-------------------------------------------------------
# Main Program:

N = int(input("Enter the value of end point of fabonacci series: "))

fib_numbers = fibonacci(N)
print('Fibonacci number:', fib_numbers)

squared_numbers = list(map(square, fib_numbers))
print('After Squaring:', squared_numbers)

#-------------------------------------------------------