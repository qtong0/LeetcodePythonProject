from typing import List


class Solution(object):
    def sumSubarrayMins(self, arr: List[int]) -> int:
        MOD = 10**9 + 7
        if not arr:
            return 0
        # value, index, accumulated_sum
        stack = [[float('-inf'), -1, 0]]
        res = 0
        for i, num in enumerate(arr):
            while stack and stack[-1][0] > num:
                stack.pop()
            total = (stack[-1][2] + (i-stack[-1][1]) * num) % MOD
            stack.append([num, i, total])
            res = (res + total) % MOD
        return int(res)



    def test(self):
        testCases = [
            [3,1,2,4],
        ]
        for arr in testCases:
            res = self.sumSubarrayMins(arr)
            print('res: %s' % res)
            print('-='*30+'-')



if __name__ == '__main__':
    Solution().test()
