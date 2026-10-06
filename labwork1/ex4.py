number = int(input("Enter a number? "))

sum_divisors = 0

for i in range(1, number):
    if number % i == 0:
        sum_divisors += i

if sum_divisors == number:
    print(number, "is a perfect number")
else:
    print(number, "is a NOT perfect number")