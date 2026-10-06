def print_pattern(n):
    print("* " * n)

    for i in range(n - 2):
        print("* " + "  " * (n - 2) + "*")

    print("* " * n)


print_pattern(5)