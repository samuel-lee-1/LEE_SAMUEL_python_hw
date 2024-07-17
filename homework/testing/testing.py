def test(input, expected, msg):
    if input == expected:
        print(msg, "passed")
    else:
        print(msg, "failed")