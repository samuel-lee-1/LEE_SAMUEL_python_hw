import sys
sys.path.insert(0, '/Users/samlee/Documents/LEE_SAMUEL_python_hw/homework/testing')
from testing import test
import math


def robot(moves):
    xpos = 0
    ypos = 0
    for move in moves:
        if move[0] == "UP":
            ypos += move[1]
        elif move[0] == "DOWN":
            ypos -= move[1]
        elif move[0] == "RIGHT":
            xpos += move[1]
        elif move[0] == "LEFT":
            xpos -= move[1]
    return round(math.sqrt(xpos*xpos+ypos*ypos))

test(robot([("UP", 5), ("DOWN", 3), ("LEFT", 3), ("RIGHT", 2)]), 2, 1)
test(robot([("UP", 5), ("DOWN", 5), ("LEFT", 5), ("RIGHT", 5)]), 0, 2)
test(robot([("UP", 10), ("DOWN", 213), ("LEFT", 12), ("RIGHT", 1)]), 203, 3)
test(robot([("UP", -2), ("DOWN", -2), ("LEFT", -2), ("RIGHT", -2)]), 0, 4)
test(robot([("UP", 4), ("DOWN", -20), ("LEFT", 1), ("RIGHT", -5)]), 25, 5)