def find_max(lst):
    highest = lst[0]
    for n in lst:
        if n > highest:
            highest = n
    return highest

def test(input, expected, number):
    if input == expected:
        print("passed test " + str(number) + " output: " + str(input))
    else:
        print("failed test " + str(number) + " output: " + str(input))

test(find_max([12, 13, 2, 1, -2123, 12, -1, 12]), 13, 1)
test(find_max([-221, -221, -221, -221, -221]), -221, 2)
test(find_max([2, 1, 3, 1, 3, -100, 1, 1, 0]), 3, 3)
test(find_max([1, 0, -1, 1, 1]), 1, 4)
test(find_max([6, 6, 5, 4, 3, 2, 7]), 7, 5)