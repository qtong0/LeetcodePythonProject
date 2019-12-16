class Solution(object):
    def maxSubarraySumCircular(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        max_dp, min_dp = A[:], A[:]
        for i in range(1, len(A)):
            max_dp[i] = (max_dp[i-1] if max_dp[i-1] > 0 else 0) + A[i]
            min_dp[i] = (min_dp[i-1] if min_dp[i-1] < 0 else 0) + A[i]
        maxVal, minVal = max(max_dp), min(min_dp)
        sumVal = sum(A)
        if sumVal != minVal:
            return max(maxVal, sumVal - minVal)
        else:
            return maxVal

    def maxSubarraySumCircular_TLE_subMaxArray(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        res = float('-inf')
        for i in range(len(A)):
            arr = A[i:] + A[:i]
            res = max(res, self.maxSubarray(arr))
        return res

    def maxSubarray(self, arr):
        n = len(arr)
        dp = [arr[0]]*n
        res = arr[0]
        for i in range(1, n):
            if arr[i] > dp[i-1]+arr[i]:
                dp[i] = arr[i]
            else:
                dp[i] = dp[i-1]+arr[i]
            res = max(res, dp[i])
        return res

    def test(self):
        testCases = [
            [5,5,-3],
            [5,-3,5],
            [1,-2,3,-2],
            [3,-1,2,-1],
            [3,-2,2,-3],
            [-2,-3,-1],
        ]
        for arr in testCases:
            res = self.maxSubarraySumCircular(arr)
            print('res: %s' % res)
            print('-='*30+'-')


if __name__ == '__main__':
    Solution().test()
