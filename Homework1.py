"""
    Home Work 1
    Pavel Shvarchov - 319270583
"""

#Task 1
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

#Task 2
def Younger():
    """
    :return: younger name
    :rtype: person
    """

    class date:
        def __init__(self, d=None, m=None, y=None):
            """
            :param d: day input
            :type d: int
            :param m: month input
            :type m: int
            :param y: year input
            :type y: int
            """
            self.day = d
            self.month = m
            self.year = y

        def __str__(self):
            """
            :return: string out of the date parameters
            :rtype: str
            """
            return (str(self.day) + '/' + str(self.month) + '/' + str(self.year))

        def __lt__(self, other):
            """
            :param other:
            :type other:date
            :return:
            :rtype: bool
            """
            return (self.year < other.year) or (self.year == other.year and (
                self.month < other.month or (self.month == other.month and self.day < other.day)))

        def input(self):
            """
            :return: updates the date parameters by the user
            """
            self.year = input("Enter year:")
            self.month = input("Enter month:")
            self.day = input("Enter day:")

    class person:
        def __init__(self, n):
            self.bdate = date()
            self.name = n

        def __str__(self):
            return str(self.name)

    person1=person(input("Enter first person name:"))
    person1.bdate.input()
    person2=person(input("Enter second person name:"))
    person2.bdate.input()
    if person1.bdate<person2.bdate:
        print("{} is younger".format(person1))
        return person1
    elif person2.bdate<person1.bdate:
        print("{} is younger".format(person2))
        return person2
    else:
        print("both are the same age")
        return None

#Task 3
def CheckNumber():
    pass