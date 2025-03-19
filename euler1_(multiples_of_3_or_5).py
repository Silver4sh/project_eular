"""
Problem 1
Multiple 3 or 5

If we list all the natural numbers below 10 that are multiples of 3 or 5, we get $3, 5, 6 and 9.
The sum of these multiples is 23.
Find the sum of all the multiples of 3 or 5 below 1000.

"""

def total(a, b, c):
    while b % a != 0:
        b += 1

    while c % a != 0:
        c -= 1

    m = (c - a) / a + 1
    n = (m / 2) * (b + c)
    print(round(n))

total(3,1,100)