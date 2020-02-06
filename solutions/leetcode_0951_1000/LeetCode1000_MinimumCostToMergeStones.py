class Solution:
    def mergeStones(self, stones, K):
        # dp[i][j][x] = min cost to merge stones to x pile
        # dp[i][i][1] = 0
        # dp[i][j][x] = dp[i][t][x-1] + dp[t+1][j][1] + sum[i][j]
        n = len(stones)
        if (n-1)%(K-1):
            return -1
        dp = [[[0]*(K+1) for _ in range(n+1)] for _ in range(n+1)]
        pref = [0]*n
        pref[0] = stones[0]
        for i in range(1, n):
            pref[i] = pref[i-1] + stones[i]
        for i in range(n):
            for j in range(i, n):
                for k in range(1, K+1):
                    dp[i][j][k] = 1e9
        for i in range(n):
            dp[i][i][1] = 0
        for length in range(2, n+1):
            for i in range(n-length+1):
                j = i+length-1
                sumVal = 0
                if i == 0:
                    sumVal = pref[j]
                else:
                    sumVal = pref[j] - pref[i-1]
                for k in range(2, K+1):
                    for t in range(i, j):
                        dp[i][j][k] = min(dp[i][j][k], dp[i][t][k-1] + dp[t+1][j][1])
                dp[i][j][1] = dp[i][j][K] + sumVal
        return dp[0][n-1][1]

    def mergeStones_own_TLE(self, stones, K: int) -> int:
        mem = {}
        return self.helper(stones, K, mem)

    def helper(self, stones, k, mem):
        if not stones: return 0
        hash = str(stones)
        if hash in mem:
            return mem[hash]
        if len(stones) == 1:
            mem[hash] = 0
            return 0
        if len(stones) < k:
            mem[hash] = -1
            return -1
        sumVals = [0]
        for i, num in enumerate(stones):
            sumVals.append(num+sumVals[-1])
        minVal = float('inf')
        for i in range(len(stones)-k+1):
            sumVal = sumVals[i+k] - sumVals[i]
            res = self.helper(stones[:i] + [sumVal] + stones[i+k:], k, mem)
            if res != -1:
                minVal = min(minVal, sumVal+res)
        res = minVal if minVal != float('inf') else -1
        mem[hash] = res
        return res

    def test(self):
        testCases = [
            [[3,2,4,1], 2],
            [[3,2,4,1], 3],
            [[3,5,1,2,6], 3],
            [
                [16,43,87,30,4,98,12,30,47,45,32,4,64,14,24,84,86,51,11,22,4],
                2,
            ],
        ]
        for stones, k in testCases:
            res = self.mergeStones(stones, k)
            print('res: %s' % res)
            print('-='*30+'-')


if __name__ == '__main__':
    Solution().test()
