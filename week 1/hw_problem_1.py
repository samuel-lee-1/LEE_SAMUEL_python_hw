# I used this for getting the date https://stackoverflow.com/questions/28189442/datetime-current-year-and-month-in-python
# I used this for input https://stackoverflow.com/questions/70797/user-input-and-command-line-arguments

from datetime import datetime

name = input("enter your name: ")
age = input("enter your age: ")

current_year = datetime.now().year
future_year = str(100 - int(age) + current_year)

print(name + ", you will be 100 in the year " + future_year + ".")