def merge_lists_ascending(list1, list2):
    merged_list = []
    index1 = 0
    index2 = 0
    while True:
        if index1 != len(list1) and index2 != len(list2):
            if index1 < len(list1) and list1[index1] < list2[index2]:
                merged_list.append(list1[index1])

                index1 += 1
            elif index2 < len(list2):
                merged_list.append(list2[index2])

                index2 += 1
        elif index1 < len(list1):
            merged_list.append(list1[index1])
            index1 += 1
        elif index2 < len(list2):
            merged_list.append(list2[index2])
            index2 += 1
        else:
            return merged_list

def test(input, expected, msg):
    if input == expected:
        print(msg, "passed")
    else:
        print(msg, "failed")

test(merge_lists_ascending([1, 2, 3, 5, 7, 10, 11, 13], [3, 5, 8, 9]), [1, 2, 3, 3, 5, 5, 7, 8, 9, 10, 11, 13], "1")
test(merge_lists_ascending([1, 2, 13, 14], [3, 5, 8, 15]), [1, 2, 3, 5, 8, 13, 14, 15], "2")
test(merge_lists_ascending([2, 5, 7, 9], [3, 5, 8, 9]), [2, 3, 5, 5, 7, 8, 9, 9], "3")
test(merge_lists_ascending([2, 5, 6, 6, 6, 7, 10], [5, 7, 10, 11]), [2, 5, 5, 6, 6, 6, 7, 7, 10, 10, 11], "4")
test(merge_lists_ascending([1, 1, 2], [0, 0, 0]), [0, 0, 0, 1, 1, 2], "5")