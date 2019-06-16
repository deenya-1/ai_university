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