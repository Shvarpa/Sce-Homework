"""
    Home Work 2
    Pavel Shvarchov - 319270583
"""
from random import randint, choice


# Task 5
def Game():
    """
    guessing game of a three digit number with 6 clues
    :return: returns True for win, False for loss
    :rtype: bool
    """

    def create_target():
        """
        :return: random 3 digit number the user must guess to win
        :rtype: int
        """
        return randint(100, 999)

    score = 100
    target = create_target()
    sum, mul, even_digits, big_digits, ascending, prime = False, False, False, False, False, False  # boolians indicating if the clue hasent been used, i dident put them in a list or dictionary because of the limitations of the assignment
    clue_range = list(range(1,7))  #a sequance pool of integares corresponding to the clue names from wich the random function will generate a clue

    def use_clue():
        """
        generates a clue and function corresponding to the clue and prints it to the screen
        """
        nonlocal sum
        nonlocal mul
        nonlocal even_digits
        nonlocal big_digits
        nonlocal ascending
        nonlocal prime
        nonlocal clue_range

        if clue_range == []:
            return None
        clue = choice(clue_range)
        if clue == 1:
            f_sum = lambda number: 0 if number == 0 else (number % 10) + f_sum(number // 10)
            sum = False
            printF1("sum: ", f_sum)
        elif clue == 2:
            f_mul = lambda number: number if (0 <= number and number <= 9) else (number % 10) * f_mul(number // 10)
            mul = False
            printF1("mul: ", f_mul)
        elif clue == 3:
            f_even_digits = lambda number: number % 2 == 0
            even_digits = False
            printF2("even digits: ", f_even_digits)
        elif clue == 4:
            f_big_digits = lambda number: number >= 5
            big_digits = False
            printF2("big digits: ", f_big_digits)
        elif clue == 5:
            f_ascending = lambda number: True if 0 <= number and number <= 9 \
                else (number // 10 % 10 < number % 10) and f_ascending(number // 10)
            ascending = False
            printF1("ascending order: ", f_ascending)
        elif clue == 6:
            def f_prime(number):
                for n in range(2, number + 1):
                    if (number % n == 0):
                        return False
                return True

            prime = False
            printF2("prime digits: ", f_prime)

        clue_range.remove(clue)

    def printF1(msg, f):
        """
        :param msg: message to print
        :type msg: str
        :param f: clue function
        :type f: Function
        """
        print(msg, "=", f(target))

    true_digit = 'X'
    false_digit = '-'

    def printF2(msg, f):
        print(msg, "=", end=" ")
        for digit in str(target):
            if f(int(digit)) == True:
                print(true_digit, end="")
            else:
                print(false_digit, end="")  # digit==False
        print(end='\n')

    def guess():
        guess = int(input("enter number/Enter to finish: "))
        if guess == target:
            return True
        return False

    while score > 0:
        print(target)
        use_clue()
        if guess():
            print("yes, correct, you win {} points".format(score))
            return True
        else:
            score -= 10
    input("Game Over, press any button to continue")
    return False


Game()
