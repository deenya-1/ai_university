class RealNumbers:
    # define attribute name
    def __init__(self, arr = None):
        self.arr = arr or []

    def add(self, elem):
        self.arr.append(elem)
        self.arr.sort()

    def remove(self, elem):
        self.arr.remove(elem)

    def remove_min(self):
        del self.arr[0]

    def remove_max(self):
        del self.arr[len(self.arr)-1]

#Test
numbers = RealNumbers([6,5,3,7,2,1])
numbers.add(4)
print(numbers.arr)
numbers.remove(1)
print(numbers.arr)
numbers.remove_min()
print(numbers.arr)
numbers.remove_max()
print(numbers.arr)