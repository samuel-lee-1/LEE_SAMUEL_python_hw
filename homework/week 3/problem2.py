def remove_duplicates(lst):
    new_list = []
    for n in lst:
        if not n in new_list: 
            new_list.append(n)
    return new_list

def test(input, expected, number):
    if input == expected:
        print("passed test " + str(number) + " output: " + str(input))
    else:
        print("failed test " + str(number) + " output: " + str(input))

test(remove_duplicates([12, 12, 2, 1, -2123, 12, -1]), [12, 2, 1, -2123, -1], 1)
test(remove_duplicates([-221, -221, -221, -221, -221]), [-221], 2)
test(remove_duplicates([2, 1, 3, 1, 3, 1, 1, 0]), [2, 1, 3, 0], 3)
test(remove_duplicates([1, 0, 1, 1, 1]), [1, 0], 4)
test(remove_duplicates([1, 2, 3, 4, 5, 6, 7]), [1, 2, 3, 4, 5, 6, 7], 5)