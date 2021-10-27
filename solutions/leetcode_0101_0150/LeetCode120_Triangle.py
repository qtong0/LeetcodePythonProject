from typing import List


class Solution(object):
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        dp = list(triangle[-1])
        n = len(triangle)
        for i in range(n-2, -1, -1):
            for j in range(i+1):
                dp[j] = min(triangle[i][j]+dp[j], triangle[i][j]+dp[j+1])
        return dp[0]
