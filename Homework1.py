"""
    Home Work 1
    Pavel Shvarchov - 319270583
"""


# Task 1
def Nand(x, y):
    """ 
    :param x:
    :type x:bool
    :param y:
    :type y:bool
    :return:
    :rtype:bool
    """
    return not (x and y)


# Task 2
def Younger():
    """
    :return: younger name
    :rtype: str
    """

    def bday_younger(d1, m1, y1, d2, m2, y2):
        return (y1 < y2) or (y1 == y2 and (m1 < m2 or (m1 == m2 and d1 < d2)))

    person1 = (input("Enter first person name:"))
    print("enter {}'s birthday: ".format(person1), end="")
    p1day, p1month, p1year = input("day:"), input("month:"), input("year:")
    person2 = (input("Enter second person name:"))
    print("enter {}'s birthday: ".format(person2), end="")
    p2day, p2month, p2year = input("day:"), input("month:"), input("year:")

    if bday_younger(p1day, p1month, p1year, p2day, p2month, p2year):
        print("{} is younger".format(person1))
        return person1
    elif bday_younger(p2day, p2month, p2year, p1day, p1month, p1year):
        print("{} is younger".format(person2))
        return person2
    else:
        print("both are the same age")
        return None

Younger()
# Task 3
def CheckNumber(x):
    """
    :param x:number to check
    :type x:long, int
    :return: true if 4*x reversed is the same as x
    :rtype: bool
    """

    def numsize(x):
        """
        :param x:number to count digits
        :type x:int
        :return:digit count of the number, the alg doesnt consider 0 as a digit
        :rtype:int
        """
        size = 0
        while (x != 0):
            x = int(x / 10)
            size += 1
        return size

    def reverse(x):
        """
        :param x:number to reverse its digits
        :type x:int
        :return:reversed number
        :rtype:int
        """
        y, i = 0, numsize(x) - 1
        while i >= 0:
            y += (x % 10) * (10 ** i)
            x = int(x / 10)
            i -= 1
        return y

    return x == reverse(x * 4)


# Task 4
def SumOfSmallest(x, y, z):
    """
    :param x:num 1
    :type x:int
    :param y:num 2
    :type y: int
    :param z:num 3
    :type z: int
    :return:sum of each of the smallest 2 in x,y,z squared, done by arranging xyz, from smallest to biggest and squareing each
    :rtype:int
    """
    if y > z: y, z = z, y
    if x > y: x, y = y, x
    if y > z: y, z = z, y
    return x ** 2 + y ** 2


# Task 5
def PrintFibonacciSeries(startI, endI):
    """
    the fib sequence starts with 0 as index 0
    :param startI: the starting index of the first number in the fibonacci series to show
    :type startI: int
    :param endI: the ending index of the last number in the fibonacci series to show
    :type endI: int
    :return: None
    :rtype: None
    """
    current, next, currentI = 0, 1, 0
    while currentI <= endI:
        if currentI >= startI: print(current)
        current, next, currentI = next, current + next, currentI + 1


# Task 6
def SumOfPrimeFactors(number):
    """
    :param number:number of which to return sum of all prime factors
    :type number: int
    :return: sum of all factors, done by checking all the factors up to the number and adding them
    :rtype: int
    """
    sum = 0
    for i in range(2, number + 1):
        while (number % i) == 0:
            sum += i
            number = number / i
    return sum


# Task 7
def CheckNumberRec(number):
    """
    :param number:number to check if all digits are even
    :type number: int
    :return: true if all digits are even, else false
    :rtype: bool
    """
    if number == 0: return True
    if (number % 2 != 0):
        return False
    CheckNumberRec(int(number / 10))


# Task 8
def PrintReverse(number):
    """
    :param number: number to check print all its digits from left to right
    :type number: int
    :return: None
    :rtype: None
    """
    if number == 0:
        return
    mod = number % 10
    div = int(number / 10)
    if div == 0:
        print("%d" % (mod))
    else:
        print("%d*" % (mod), end=" ")
    PrintReverse(div)
