from typing import List


class Solution(object):
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        n = len(nums)
        preSums = [0]*(n+1)
        for i in range(n):
            preSums[i+1] = preSums[i] + nums[i]
        deque = []
        res = n+1
        for i in range(n+1):
            while deque and preSums[i] - preSums[deque[0]] >= k:
                res = min(res, i-deque.pop(0))
            while deque and preSums[i] <= preSums[deque[-1]]:
                deque.pop()
            deque.append(i)
        return res if res <= n else -1
    
    def test(self):
        testCase = [
            [
                [56,-21,56,35,-9],
                61,
            ],
            [
                [84,-37,32,40,95],
                167,
            ],
            [
                [1],
                1,
            ],
            [
                [1,2],
                4
            ],
            [
                [2,-1,2],
                3
            ],
            [
                [77,19,35,10,-14],
                19
            ],
            [
                [-3, 4, 1],
                5,
            ],
        ]
        for nums, k in testCase:
            res = self.shortestSubarray(nums, k)
            print('res: %s' % res)
            print('-='*30+'-')


if __name__ == '__main__':
    Solution().test()
