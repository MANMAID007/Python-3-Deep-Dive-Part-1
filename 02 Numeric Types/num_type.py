# Integers
import sys, gc

def int_size(n):
    print("size of {} is {}".format(n, sys.getsizeof(n)))

int_size(0)
int_size(111111111444444464444444447866666666624444444444445666666666688888888888322222222222222)
# int_size(2**10**4)
print("-------------------------------")

# Integers: Constructor and Bases
a = int(10.9)
print(a)
a = int(-0.9)
print(a)
a = int(True)
print(a)
a = int("10011101", 2)
print(a)
a = int("AAB3F", 16)
print(a)
a = bin(565)
print(a)
print("-------------------------------")

# Rational numbers
from fractions import Fraction
import math
print("fraction 33/ 7, 10/4 be like: {}, {}".format(Fraction(33, 7), Fraction(10, 4)))
print(Fraction(math.pi))
print(Fraction(0.3))
print(5404319552844595/18014398509481984)
print(Fraction(3, 10))
print("-------------------------------")


