import math


def Fibonacci_Finder(term):
    term = round(((1.618034**term) - (-.618034)**term) / (math.sqrt(5)))
    return term


# Test cases
print(Fibonacci_Finder(0))
print(Fibonacci_Finder(1))
print(Fibonacci_Finder(2))
print(Fibonacci_Finder(3))
print(Fibonacci_Finder(4))
print(Fibonacci_Finder(5))
print(Fibonacci_Finder(6))
print(Fibonacci_Finder(7))
print(Fibonacci_Finder(8))
print(Fibonacci_Finder(9))
print(Fibonacci_Finder(10))
