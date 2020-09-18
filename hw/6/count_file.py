import os
import string


def count_word(row: string) -> int:
    return sum([i.strip(string.punctuation).isalpha() for i in row.split()])


def linecount_wc():
    return os.popen('wc test.txt').read().split()


# Num 2
start_line = 1
file = open(r'test.txt')
line = 1
for row in file:
    print('Row {:d} Sum of chars: {:d}, words: {:d}'.format(line, len(row), count_word(row)))
    line += 1
    print(row)

print('Sum of line: {}, file size {} bite, words: {}'.format(int(linecount_wc()[0]) + start_line, linecount_wc()[2],
                                                             linecount_wc()[1]))
file.close()
