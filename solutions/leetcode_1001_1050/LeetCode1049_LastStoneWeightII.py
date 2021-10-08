from typing import List


class Solution:
    # Knapsacks Problem !!!
    # DP
    def lastStoneWeightII(self, stones: List[int]) -> int:
        sum_all = sum(stones)
        dp = [False]*(1 + sum_all//2)
        dp[0] = True
        for num in stones:
            for i in range(sum_all//2, num-1, -1):
                if dp[i-num]:
                    dp[i] = True
        for i in range(sum_all // 2, -1, -1):
            if dp[i]:
                return sum_all - i - i
        return 0

    def test(self):
        test_cases = [
            [2,7,4,1,8,1],
            [31,26,33,21,40],
            [1,2],
        ]
        for stones in test_cases:
            res = self.lastStoneWeightII(stones)
            print('res: %s' % res)
            print('-='*30+'-')


if __name__ == '__main__':
    Solution().test()
