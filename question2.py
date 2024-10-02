"""
ECE241 - Fall 2024, Homework 2, question 2.
    denote WORTH CASE asymptotic time complexity use the big-O notation
    assuming the input parameters are all arrays.
    You can use the variable name to represent the length of the input array in your solution.
    You can assume ``len()'' function takes O(1) time.
"""

from math import log, sin, tan  # assume these functions all take O(1) time


def demo(n):
    # NOTE: This is a demo for this question.
    # You DO NOT need to include the solution for this one in your submission

    total = 0
    for i in n:
        total += i
    return total
    # Let n is the input array.
    # The time complexity of this function is O(n), where in this question, you can use the variable name to represent the length of the input array.


def function1(n, m):
    nm = []

    for n_i in n:
        nm.append(n_i)
    # The time complexity of this for loop is O(n)

    for m_i in m:
        nm.append(m_i)
    # The time complexity of this for loop is O(m)

    return nm
    # Let n, m is the input array.
    # Both loops run sequentially, so the total time complexity of this function1 is O(n + m).



def function2(n):
    lt = len(n)
    nm = []

    while lt > 1:
        nm.append(n[202420242024])
        lt = lt / 2

    return nm


def function3(a, b):
    sum = b[0]
    count = 0
    index = 1
    while index <= int(log(a[2024])) and index < len(b):
        sum += b[index]
        index += 1
        count += 1

    return count


def function4(n):
    nn = []

    sum = 0
    for i in n:
        sum += i
    avg = sum / len(n)
    for i in n:
        for j in range(int(sin(avg))):
            nn.append(i * j)

    return nn


def function5(m, n, x, y, z, t):
    if 2024 * len(m) + min(2024 * n[2024], 2024) < max(2024, 2024 ** x[-2024]):
        return 2024 ** log(log(tan(2024 + sin(2024)))) - abs(x[2024]) + 9 * log(log(len(t)))
    else:
        return 2024 * 2024 - min(x[2024], y[-2024], z[20] + z[24], -2024) + 9 * log(
            log(log(len(t) + 2024)) + log(t[2024 ** 2024]))

