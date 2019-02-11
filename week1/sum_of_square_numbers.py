from math import sqrt


def judge_square_sum(c: int):
    for a in range(int(sqrt(c) + 1)):
        b = sqrt(c - a * a)
        if b == int(b):
            return True
    return False
