class Solution:
    def minDeletionSize(self, A: list[str]) -> int:
        n = len(A[0])
        dp = [1]*n
        for i in range(n-2, -1, -1):
            for j in range(i+1, n):
                if all (row[i] <= row[j] for row in A):
                    dp[i] = max(dp[i], 1+dp[j])
        return n-max(dp)
