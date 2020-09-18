import re


def remove_extra_space():
    print(re.sub(r' +', ' ', input('Enter sentence: ')))


def biggest():
    sentence = input('Enter sentence: ')
    sentence_list = sentence.split()
    biggest_val = 0
    biggest_word = ''
    for i in sentence_list:
        if len(i) > biggest_val:
            biggest_val = len(i)
            biggest_word = i

    print('Biggest word: ' + biggest_word)


remove_extra_space()
