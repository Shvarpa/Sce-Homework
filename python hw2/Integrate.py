"""
    Home Work 2
    Pavel Shvarchov - 319270583
"""
import random


def integrate(a, b, f, tries=10000):
    """
    :param a:left/starting point of integration
    :type a:
    :param b:right/ending point of integration
    :type b:
    :param f:function to intigrate
    :type f:Function
    :param tries:number of random tries for monte carlo method,
    precision increases with number of tries, but so does computing time
    :type tries:int
    :return:result of intigration using monte carlo method
    :rtype:float
    """
    sum = 0
    for _ in range(tries):
        x = random.uniform(a, b)
        sum += f(x)
    return (sum / tries) * (b - a)


print(integrate(2, 4, lambda x: x + 2))
