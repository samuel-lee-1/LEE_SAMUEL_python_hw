def factorial(n):
    previous = 1
    if n != 1:
        previous = factorial(n-1)
    return n*previous

def test(input, expected, message):
    if input == expected:
        print("passed: " + message + " output: " + str(input))
    else:
        print("failed: " + message + " output: " + str(input))

test(factorial(1), 1, "1!")
test(factorial(2), 2, "2!")
test(factorial(3), 6, "3!")
test(factorial(6), 720, "6!")
test(factorial(12), 479001600, "12!")