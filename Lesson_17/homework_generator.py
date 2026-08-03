# Напишіть генератор, який повертає послідовність парних чисел від 0 до N.

def even_numbers(n):
    for i in range(0, n + 1, 2):
        yield i


N = 10

for number in even_numbers(N):
    print(number)

# Створіть генератор, який генерує послідовність Фібоначчі до певного числа N.

def fibonacci(n):
    a, b = 0, 1
    while a <= n:
        yield a
        a, b = b, a + b


N = 50

for number in fibonacci(N):
    print(number)