from typing import List


class Solution:
    def largestNumber(self, cost: List[int], target: int) -> str:
        hashmap = {}
        for i, c in enumerate(cost):
            if c not in hashmap or hashmap[c] < i+1:
                hashmap[c] = i+1
        dp = ['']*(target + 1)

        # first
        for i in range(1, target+1):
            # second
            for c, d in hashmap.items():
                if i - c == 0 or (i - c > 0 and dp[i - c]):
                    tmp = dp[i-c] + str(d)
                    if len(tmp) > len(dp[i]) or (len(tmp) == len(dp[i]) and tmp > dp[i]):
                        dp[i] = tmp
        return dp[-1] if dp[-1] else '0'


    def test(self):
        test_cases = [
            [[4,3,2,5,6,7,2,5,5], 9],
            [[7,6,5,5,5,6,8,7,8], 12],
            [[2,4,6,2,4,6,4,4,4], 5],
            [[6,10,15,40,40,40,40,40,40], 47],
        ]
        for cost, target in test_cases:
            res = self.largestNumber(cost, target)
            print('res: %s' % res)
            print('-='*30 + '-')


if __name__ == '__main__':
    Solution().test()
