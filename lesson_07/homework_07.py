# task 1
""" Задача - надрукувати табличку множення на задане число, але
лише до максимального значення для добутку - 25.
Код майже готовий, треба знайти помилки та випраавити\доповнити.
"""

def multiplication_table(number):
    multiplier = 1

    while True:
        result = number * multiplier

        if result > 25:
            break

        print(str(number) + "x" + str(multiplier) + "=" + str(result))

        multiplier += 1
multiplication_table(3)

# task 2
"""  Написати функцію, яка обчислює суму двох чисел.
"""

def sum_numbers(a, b):
    return a + b
print(sum_numbers(1, 2))

# task 3
"""  Написати функцію, яка розрахує середнє арифметичне списку чисел.
"""

def arithmetic_mean(numbers):
    return sum(numbers) / len(numbers)

nums = [1, 2, 3, 4, 5]
print(arithmetic_mean(nums))

# task 4
"""  Написати функцію, яка приймає рядок та повертає його у зворотному порядку.
"""

def reversed(text):
    return text[::-1]

print(reversed("hello"))

# task 5
"""  Написати функцію, яка приймає список слів та повертає найдовше слово у списку.
"""

def longest_word(text):
    return max(text, key=len)

print(longest_word(["volkswagen", "toyota", "opel"]))

# task 6
"""  Написати функцію, яка приймає два рядки та повертає індекс першого входження другого рядка
у перший рядок, якщо другий рядок є підрядком першого рядка, та -1, якщо другий рядок
не є підрядком першого рядка."""

def find_substring(str1, str2):
    if str2 in str1:
        return str1.index(str2)
    else:
        return -1

print(find_substring("Hello, world!", "world"))

"""  Оберіть будь-які 4 таски з попередніх домашніх робіт та
перетворіть їх у 4 функції, що отримують значення та повертають результат.
Обоязково документуйте функції та дайте зрозумілі імена змінним.
"""

# task 7 homework_03/task 04

def calculate_sea_area(black_sea_area, azov_sea_area):
    """
    Calculates total area of Black Sea and Azov Sea.

    Args:
        black_sea_area (int): Area of Black Sea
        azov_sea_area (int): Area of Azov Sea

    Returns:
        int: Total combined area
    """
    total_area = black_sea_area + azov_sea_area
    return total_area

print(calculate_sea_area(436402, 37800))

# task 8 homework_03/task 06

def calculate_total_cost(payment_period, monthly_payment):
    """
    Calculates total cost based on payment period and monthly payment.

    Args:
        payment_period (int): Number of months
        monthly_payment (int): Payment per month

    Returns:
        int: Total cost of the product
    """
    total_cost = payment_period * monthly_payment
    return total_cost

print(calculate_total_cost(18, 1179))

# task 9 homework_6.1

def sum_unique_numbers(text):
    """
    Checks if a string contains more than 10 unique characters.

    Args:
        text (str): Input string

    Returns:
        bool: True if number of unique characters is greater than 10, otherwise False
    """
    return len(set(text)) > 10

print(sum_unique_numbers("Метелики дуже гарні"))

# task 10 homework_6.4

def sum_even_numbers(numbers):
    """
    Returns the sum of all even numbers in a list.

    Args:
        numbers (list): List of integers

    Returns:
        int: Sum of even numbers
    """
    total = 0

    for number in numbers:
        if number % 2 == 0:
            total += number

    return total

print(sum_even_numbers([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
