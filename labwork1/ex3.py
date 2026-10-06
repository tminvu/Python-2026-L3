number = int(input("Enter a number? "))

if number < 2:
    print(number, "is a NOT prime number")
else:
    prime = True

    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            prime = False
            break

    if prime:
        print(number, "is a prime number")
    else:
        print(number, "is a NOT prime number")