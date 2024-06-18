# TODO: Not working yet, needs fixes.
class Solution:
    def findMaximumNumber(self, k: int, x: int) -> int:
        l, r = 1, 10**15
        while l < r:
            mid = (r - l) // 2 + l
            priceSum, i = 0, 0
            for i in range(0, 60, x):
                priceSum += self.cal(mid, i)
            if priceSum > k:
                r = mid
            else:
                l = mid + 1
        return l - 1

    def cal(self, num, i) -> int:
        res = 0
        num += 1
        plen = 1 << i
        p = num // plen
        res = p * plen // 2
        num %= plen
        res += max(0, num - plen//2)
        return res
