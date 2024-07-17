import sys
sys.path.insert(0, '/Users/samlee/Documents/LEE_SAMUEL_python_hw/homework/testing')
from testing import test
import re


def check_valid_password(passwords):
    password_list = ""
    for password in passwords:
        password = repr(password)[1:-1]
        if re.search("[a-z]", password) and re.search("[0-9]", password) and re.search("[A-Z]", password) \
            and re.search("[^A-Za-z0-9 ]", password) and len(password) >= 6 and len(password) <= 12:
            password_list += password + ", "
    password_list = password_list[:-2]
    return password_list

test(check_valid_password(["ABd1234@1", "a F1#", "2w3E*", "2We3345", "oo1\nS", "\n\n90Abcdefg", "abcd3\nM"]), r"ABd1234@1, oo1\nS, abcd3\nM", 1)