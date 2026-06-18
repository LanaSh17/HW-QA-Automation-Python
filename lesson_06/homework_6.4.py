my_list_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
total = 0

for number in my_list_numbers:
    if number % 2 == 0:
        total += number

print(total)