#Реалізуйте ітератор для зворотного виведення елементів списку

class ReverseElementsIterator:
    def __init__(self, num):
        self.list = list(reversed(num))
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.list):
            raise StopIteration
        element = self.list[self.index]
        self.index += 1
        return element

my_iterator = ReverseElementsIterator([1, 2, 3, 4, 5])
for element in my_iterator:
    print(element)

#Напишіть ітератор, який повертає всі парні числа в діапазоні від 0 до N.

class IteratorPairwiseNumbers:
    def __init__(self, n):
        self.n = n
        self.current = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.current > self.n:
            raise StopIteration
        element = self.current
        self.current += 2
        return element

iterator = IteratorPairwiseNumbers(100)
for num in iterator:
    print(num)





