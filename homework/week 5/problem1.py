import sys
sys.path.insert(0, '/Users/samlee/Documents/LEE_SAMUEL_python_hw/homework/testing')
from testing import test


def print_letters_digits(sentence):
    letters = 0
    digits = 0
    for c in sentence:
        if c.isdigit():
            digits += 1
        elif c.isalpha():
            letters += 1
    return [letters, digits]

test(print_letters_digits("hello world! 123"), [10, 3], 1)
test(print_letters_digits("!!!1a 2b 3c 4d 5e 6f!!!"), [6, 6], 2)
test(print_letters_digits("12#345)(*)678"), [0, 8], 3)
test(print_letters_digits("1--1--1--1--1"), [0, 5], 4)
test(print_letters_digits("!@#@!1m--"), [1, 1], 5)
test(print_letters_digits("\n\n1m--"), [1, 1], 6)

