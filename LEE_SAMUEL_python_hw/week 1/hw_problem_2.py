# used this for the random ints https://docs.python.org/3/library/random.html

import random

random_number = random.randint(1, 9)

print("guess a number from 1-9 including 1 and 9")
while True:
    user_number = int(input("--> "))
    if user_number > random_number:
        print("your guess is too high")
    elif user_number < random_number:
        print("you guess is too low")
    else:
        print("you guessed the number")
        break