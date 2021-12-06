from typing import List


class Solution:
    # !!! Knapsacks Problem !!!
    #
    # Why it's Knapsacks problem?
    # One way to understand the fact that "The minimum result of cancellation = the minimum difference between the sum of two groups".
    # Say you've already found two groups with smallest difference.
    # Group A = [A1, A2, ..., An]
    # Group B = [B1, B2, ..., Bm]
    # The process we cancel two stones is to arbitrarily pick one from group A and one from Group B.
    # If Ai > Bj, then put Ai-Bj into group A.
    # If Ai < Bj, then put Ai-Bj into group B.
    # If Ai = Bj, then nothing will be put into group A and B.
    # We repeat the process until there is only one stone left.
    # You will find the remaining stone is |sum(Group A) - sum(Group B)|.
    #
    def lastStoneWeightII(self, stones: List[int]) -> int:
        sum_all = sum(stones)
        dp = [False]*(1 + sum_all//2)
        dp[0] = True
        for num in stones:
            for i in range(sum_all//2, num-1, -1):
                if dp[i-num]:
                    dp[i] = True
        for i in range(sum_all//2, -1, -1):
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
