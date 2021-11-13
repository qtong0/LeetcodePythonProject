from typing import List
import heapq


class Solution:
    def connectSticks(self, sticks: List[int]) -> int:
        heap = sticks
        heapq.heapify(heap)
        res = 0
        while len(heap) > 1:
            val1 = heapq.heappop(heap)
            val2 = heapq.heappop(heap)
            val = val1 + val2
            res += val
            heapq.heappush(heap, val)
        return res


    def test(self):
        test_cases = [
            [2,4,3],
            [1,8,3,5],
            [5],
        ]
        for sticks in test_cases:
            res = self.connectSticks(sticks)
            print('res: %s' % res)
            print('-='*30 + '-')


if __name__ == '__main__':
    Solution().test()
