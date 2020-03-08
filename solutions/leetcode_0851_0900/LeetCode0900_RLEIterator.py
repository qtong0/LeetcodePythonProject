class RLEIterator(object):

    def __init__(self, A):
        """
        :type A: List[int]
        """
        self.arr = A
        self.idx = 0
        self.quantity = 0

    def next(self, n):
        """
        :type n: int
        :rtype: int
        """
        while self.idx < len(self.arr):
            if self.quantity + n > self.arr[self.idx]:
                n -= self.arr[self.idx] - self.quantity
                self.quantity = 0
                self.idx += 2
            else:
                self.quantity += n
                return self.arr[self.idx+1]
        return -1


# Your RLEIterator object will be instantiated and called as such:
# obj = RLEIterator(A)
# param_1 = obj.next(n)
