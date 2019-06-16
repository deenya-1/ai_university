"""
Задача 13: Придумайте структуру для хранения действительных чисел, которая могла бы выполнять следующие операции:
вставить элемент, удалить элемент, удалить минимальный элемент, удалить максимальный элемент.
Последние две операции должны выполняться за O(1).
Постарайтесь так же минимизировать время выполнения первых двух запросов.

Возможно ли выполнять все операции за O(1)? Если да, то реализуйте данную структуру.
Если нет, то в отдельном файле объясните, почему это не возможно.
В качестве ответа вставьте ссылку на git репозиторий с кодом на языке Python и файлом с обоснованием невозможности при необходимости.
"""

class RealNumbers:
    # define attribute name
    def __init__(self, arr = None):
        self.arr = arr or []

    def add(self, elem):
        self.arr.append(elem)

    def remove(self, elem):
        self.arr.remove(elem)

    def remove_min(self):
        self.arr.remove(min(self.arr))

    def remove_max(self):
        self.arr.remove(max(self.arr))

#Test
numbers = RealNumbers([1,2,3, 4,5,6])
numbers.add(4)
print(numbers.arr)
numbers.remove(1)
print(numbers.arr)
numbers.remove_min()
print(numbers.arr)
numbers.remove_max()
print(numbers.arr)