# Num 1
matrix = [
    [62, 8, 19, 98, 69, 81, 25, 21, 98, 99],
    [55, 96, 67, 69, 81, 43, 89, 39, 22, 4],
    [10, 96, 98, 81, 35, 34, 42, 53, 41, 83],
    [22, 11, 55, 10, 81, 36, 98, 41, 96, 30],
    [11, 59, 49, 47, 80, 83, 63, 27, 79, 28],
    [23, 83, 85, 35, 24, 80, 53, 62, 17, 90],
    [56, 54, 53, 7, 12, 63, 83, 22, 23, 23],
    [87, 93, 5, 7, 91, 63, 90, 28, 37, 45],
    [57, 53, 5, 93, 90, 1, 75, 7, 3, 0],
    [85, 65, 15, 71, 78, 90, 46, 17, 98, 40],
]


def calc_sum_column(column_index: int = 0, max: list = [0 for i in range(len(matrix))]) -> list:
    try:
        row_index = 0
        matrix_len = len(matrix) - 1
        for row in matrix:
            max[column_index] += row[column_index]
            if row_index == matrix_len:
                column_index += 1
                calc_sum_column(column_index, max)
            elif row_index < len(row):
                row_index += 1
    except:
        print("An exception occurred")
    return max


# columns_sum = calc_sum_column()

# print('Max value is {} in column {}. Sum by columns: {}'.format(max(columns_sum), columns_sum.index(max(columns_sum)), ", ".join(map(str, columns_sum))))

import operator
import functools
import os


# import numpy as np

def count_word3(word):
    return sum(ord(c) - 64 for c in word)


def sum_of_strings(list_of_strings):
    return functools.reduce(operator.add, list_of_strings)


def linecount_wc():
    return os.popen('wc test.txt').read().split()


# Num 2
file = open(r'test.txt')
# print(os.popen('wc -l test.txt').read())
# exit(1)
dictionary = {}
line = 0
for row in file:
    print('Row {} Sum of chars: {}'.format(line, len(row)))
    line += 1
    # print(row)

# count = len(file.readlines())
print('Sum of line: {}, file size {} bite, words: {}'.format(linecount_wc()[0], linecount_wc()[2], linecount_wc()[1]))
file.close()


def fib(n):
    if n > 1:
        return fib(n - 1) + fib(n - 2)
    return n


print(fib(7))
