'''
Created on Oct 21, 2017

@author: MT
'''
class Solution(object):
    def kEmptySlots(self, flowers, k):
        """
        :type flowers: List[int]
        :type k: int
        :rtype: int
        """
        if not flowers: return -1
        n = len(flowers)
        days = [False]*n
        for i in range(n):
            days[flowers[i]-1] = i+1
        left, right = 0, k+1
        res = float('inf')
        for i in range(n):
            if right >= n: break
            if days[i] == days[right] and i == right:
                res = min(res, max(days[left], days[right]))
            if days[i] < days[left] or days[i] < days[right]:
                left = i
                right = k+1+i
        return res if res != float('inf') else -1


# Another Solution, min queue

from collections import deque


class MinQueue(deque):
    def __init__(self):
        deque.__init__(self)
        self.mins = deque()

    def append(self, x):
        deque.append(self, x)
        while self.mins and x < self.mins[-1]:
            self.mins.pop()
        self.mins.append(x)

    def popleft(self):
        x = deque.popleft(self)
        if self.mins[0] == x:
            self.mins.popleft()
        return x

    def min(self):
        return self.mins[0]


class Solution:
    def kEmptySlots(self, bulbs, K: int) -> int:
        days = [0] * len(bulbs)
        for day, position in enumerate(bulbs, 1):
            days[position - 1] = day

        window = MinQueue()
        ans = len(days)

        for i, day in enumerate(days):
            window.append(day)
            if K <= i < len(days) - 1:
                window.popleft()
                if K == 0 or days[i-K] < window.min() > days[i+1]:
                    ans = min(ans, max(days[i-K], days[i+1]))

        return ans if ans < len(days) else -1



    def test(self):
        testCases = [
            [
                [1, 3, 2],
                1,
            ],
            [
                [1, 2, 3],
                1,
            ],
            [
                [1,2,3,4,5,6,7],
                1,
            ],
        ]
        for flowers, k in testCases:
            print('flowers: %s' % flowers)
            print('k: %s' % k)
            result = self.kEmptySlots(flowers, k)
            print('result: %s' % result)
            print('-='*30+'-')

if __name__ == '__main__':
    Solution().test()
