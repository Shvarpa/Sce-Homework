"""
    Home Work 2
    Pavel Shvarchov - 319270583
"""
import random


def integrate(a, b, f):
    sum, sum_pow, tries = 0, 0, 1000
    for _ in range(tries):
        x = random.uniform(a, b)
        fx = f(x)
        sum, sum_pow = sum + fx, sum_pow + (fx ** 2)
        if _ % 50 == 0:
            print("x={} , sum={} , sum_pow={}".format(x, sum, sum_pow))
        sum, sum_pow = sum / tries, sum_pow / tries
        return sum + ((sum_pow-sum**2)/tries)**0.5


print(integrate(0, 1, lambda x: 2))
