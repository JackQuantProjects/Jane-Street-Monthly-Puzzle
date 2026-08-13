import random


def main(n):
    '''
    Simulates n cases of Andy's stroll.

    Returns the proportion of times Andy makes it
    home without finding out.
    '''
    home = 0

    for _ in range(n):
        if one():
            home += 1

    return home / n


def one():
    '''
    Andy is one tile from home.

    1/3 -> home
    2/3 -> tile two
    '''
    outcome = random.random()

    if outcome < 1/3:
        return True

    return two()


def two():
    '''
    Andy is two tiles from home.

    1/3 -> tile one
    1/3 -> discovers he isn't on the ball
    1/3 -> tile three
    '''
    outcome = random.random()

    if outcome < 1/3:
        return one()

    elif outcome < 2/3:
        return False

    else:
        return three()


def three():
    '''
    Andy is three tiles from home.

    1/3 -> tile two
    1/3 -> discovers he isn't on the ball
    1/3 -> tile four
    '''
    outcome = random.random()

    if outcome < 1/3:
        return two()

    elif outcome < 2/3:
        return False

    else:
        return four()


def four():
    '''
    Andy is four tiles from home.

    1/3 -> discovers he isn't on the ball
    2/3 -> tile three
    '''
    outcome = random.random()

    if outcome < 1/3:
        return False

    else:
        return three()


print(main(100000000))
