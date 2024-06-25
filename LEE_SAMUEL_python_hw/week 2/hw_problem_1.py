a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
common_elements = []

for n in a:
    if n in b and n not in common_elements:
        common_elements.append(n)

print(common_elements)