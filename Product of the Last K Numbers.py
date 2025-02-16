# Design an algorithm that accepts a stream of integers and retrieves the product of the last k integers of the stream.

# Implement the ProductOfNumbers class:

#    ProductOfNumbers() Initializes the object with an empty stream.
#    void add(int num) Appends the integer num to the stream.
#    int getProduct(int k) Returns the product of the last k numbers in the current list. You can assume that always the current list has at least k numbers.


class ProductOfNumbers:
   
    def __init__(self):
        self.numbers = [1]
        self.elements_count = 0

        

    def add(self, num: int) -> None:
        if not(num == 0):
            self.numbers.append(num*self.numbers[self.elements_count])
            self.elements_count += 1
        else:
            self.numbers = [1]
            self.elements_count = 0       

    def getProduct(self, k: int) -> int:       
        if k > self.elements_count:
            return 0
        return self.numbers[self.elements_count] // self.numbers[self.elements_count - k]
