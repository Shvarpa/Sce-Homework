"""
    Home Work 1
    Pavel Shvarchov - 319270583
"""


# import tkinter as tk

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


def Younger():
    """
    :return: younger name
    :rtype: string
    """

    class date:
        def __init__(self, d=None, m=None, y=None):
            self.day = d
            self.month = m
            self.year = y

        def __str__(self):
            return (str(self.day) + '/' + str(self.month) + '/' + str(self.year))

        def __lt__(self, other):
            return (self.year < other.year) or (self.year == other.year and (
            self.month < other.month or (self.month == other.month and self.day < other.day)))

        def input(self):
            year = input("Enter year:")
            month = input("Enter month:")
            day = input("Enter day:")

    def menu(comment):
        """
        :param comment:
        :return:
        """
        return

    return 0
