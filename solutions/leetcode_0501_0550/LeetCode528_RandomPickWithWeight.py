import random

class Solution:

    def __init__(self, w):
        self.weights = w
        sumVal = 0
        sumVals = []
        for i, weight in enumerate(self.weights):
            sumVal += weight
            sumVals.append(sumVal)
        self.sumVal = sumVal
        self.sumVals = sumVals

    def pickIndex(self) -> int:
        val = random.randint(1, self.sumVal)
        l, r = 0, len(self.sumVals)
        while l < r:
            mid = (l+r)//2
            if self.sumVals[mid] < val:
                l = mid+1
            else:
                r = mid
        return r


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()


if __name__ == '__main__':
    weights = [3, 14, 1, 7]
    s = Solution(weights)
    for _ in range(50):
        print(s.pickIndex())
