# Напишіть декоратор, який логує аргументи та результати викликаної функції.

def logger(func):
    def wrapper(*args, **kwargs):
        print(f"Виклик функції: {func.__name__}")
        print(f"Аргументи: {args}, {kwargs}")
        result = func(*args, **kwargs)
        print(f"Результат: {result}")
        return result

    return wrapper

@logger
def multiply(a, b):
    return a * b

multiply(4, 5)

# Створіть декоратор, який перехоплює та обробляє винятки, які виникають в ході виконання функції.

def handle_exceptions(func):
    def wrapper(*args, **kwargs):
        try:
            result = func(*args, **kwargs)
            return result

        except Exception as error:
            print(f"Виникла помилка: {error}")

    return wrapper

@handle_exceptions
def divide(a, b):
    return a / b

print(divide(10, 2))
divide(10, 0)

