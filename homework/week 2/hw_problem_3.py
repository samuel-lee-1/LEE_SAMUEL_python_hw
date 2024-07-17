int_array = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
target_int = 25

for i in range(len(int_array)):
    other_num = target_int - int_array[i]

    done = False
    for x in range(len(int_array)):
        if not x == i and int_array[x] == other_num:
            print("number 1: " + str(int_array[i]) + " index: " + str(i))
            print("number 2: " + str(int_array[x]) + " index: " + str(x))
            done = True
    if done:
        break
