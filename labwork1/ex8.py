def extract_even(l):
    even_numbers = []

    for number in l:
        if number % 2 == 0:
            even_numbers.append(number)

    return even_numbers
numbers = [1, 4, 5, -1, 10]

print(extract_even(numbers))