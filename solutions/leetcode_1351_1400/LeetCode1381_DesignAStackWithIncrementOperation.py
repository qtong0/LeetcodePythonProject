class CustomStack:

    def __init__(self, maxSize: int):
        self.maxSize = maxSize
        self.arr = []
        self.inc = [0]*maxSize

    def push(self, x: int) -> None:
        if len(self.arr) < self.maxSize:
            self.arr.append(x)

    def pop(self) -> int:
        if not self.arr:
            return -1
        i = len(self.arr) - 1
        self.inc[i-1] += self.inc[i]
        res = self.arr.pop() + self.inc[i]
        self.inc[i] = 0
        return res


    def increment(self, k: int, val: int) -> None:
        i = min(k, len(self.arr)) - 1
        if i >= 0:
            self.inc[i] += val


# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)
