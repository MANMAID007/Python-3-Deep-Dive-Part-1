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

# Float Equality Testing
x = 0.1 + 0.1 + 0.1
y = 0.3
print("Is 0.1 + 0.1 + 0.1 is same as 0.3 in Python: {}, x is {}, y is {}".format(x == y, x, y))
print(0.31/3)
print("-------------------------------")

# Rounding
x = 1.23
print(round(x, 0))
print("-------------------------------")

# Decimals
import decimal
from decimal import Decimal

# print(decimal.getcontext())
# decimal.getcontext().prec = 5
# print(decimal.getcontext())
# decimal.getcontext().rounding = decimal.ROUND_HALF_UP
# print(decimal.getcontext())
with decimal.localcontext() as ctx:
    ctx.prec = 28
    ctx.rounding = decimal.ROUND_CEILING
    print(ctx)
    print(Decimal(10))
    print(Decimal('10.1'))
    t = (0, (4, 8, 4, 5, 8, 5, 6), -6)
    print(Decimal(t))
    # x, y, z = Decimal('0.1'), Decimal('0.1'), Decimal('0.1')
    # print(0.1 + 0.1 + 0.1)
    # print(x+y+z)
    def bunch_of_calc(a, b):
        x = a
        x_dec = Decimal(b)
        root_float, root_mixed, root_dec = math.sqrt(x), math.sqrt(x_dec), x_dec.sqrt()
        print(format(root_float, '1.27f'), format(root_float * root_float, '1.27f'))
        print(format(root_mixed, '1.27f'), format(root_mixed * root_mixed, '1.27f'))
        print(root_dec, root_dec * root_dec)


    bunch_of_calc(2, '2')
    bunch_of_calc(0.01, '0.01')
print("-------------------------------")

# Complex
import cmath
a = complex(1, 2)
print(a, a.real, a.imag, a.conjugate(), a ** 2, cmath.sqrt(a))
print(cmath.exp(complex(0, cmath.pi)) + 1)




