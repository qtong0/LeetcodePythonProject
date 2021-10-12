# Best solution
# TC: O(1)
# SC: O(K) - k is last non-zero numbers
#
class ProductOfNumbers:

    def __init__(self):
        self.arr = [1]

    def add(self, num: int) -> None:
        if num == 0:
            self.arr = [1]
        else:
            self.arr.append(self.arr[-1] * num)

    def getProduct(self, k: int) -> int:
        if k >= len(self.arr):
            return 0
        else:
            return self.arr[-1] // self.arr[-k-1]


# TC: O(1)
# SC: O(N)
# Further improvement: only tracks last non-zero, use an array
#
class ProductOfNumbers_own:

    def __init__(self):
        self.size = 0
        self.hashmap = {0:1}
        self.last_zero = 0

    def add(self, num: int) -> None:
        self.size += 1
        if num != 0:
            self.hashmap[self.size] = self.hashmap[self.size-1]*num
        else:
            self.hashmap[self.size] = 1
            self.last_zero = self.size

    def getProduct(self, k: int) -> int:
        if self.last_zero + k > self.size:
            return 0
        return self.hashmap[self.size] // self.hashmap[self.size-k]


# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)

if __name__ == '__main__':
    obj = ProductOfNumbers()
    print(obj.add(3))
    print(obj.add(0))
    print(obj.add(2))
    print(obj.add(5))
    print(obj.add(4))
    print(obj.getProduct(2))
    print(obj.getProduct(3))
    print(obj.getProduct(4))
    print(obj.add(8))
    print(obj.getProduct(2))
