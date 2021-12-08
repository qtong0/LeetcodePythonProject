class Solution:
    # Math
    # f(k) = f(k - x) + 1
    def findMinFibonacciNumbers(self, k: int) -> int:
        if k < 2:
            return k
        a, b = 1, 1
        while b <= k:
            a, b = b, a + b
        return self.findMinFibonacciNumbers(k - a) + 1



    # Knapsack problem, own - TLE
    def findMinFibonacciNumbers_own_knapsack(self, k: int) -> int:
        fib = [1, 1]
        while fib[-1] < k:
            fib.append(fib[-2] + fib[-1])
        dp = [float('inf')]*(k+1)
        dp[0] = 0
        for num in fib:
            for i in range(k-num+1):
                if dp[i] != float('inf'):
                    dp[i+num] = min(dp[i+num], dp[i] + 1)
        return dp[-1]



    def test(self):
        test_cases = [
            7,
            10,
            19,
            427010,
        ]
        for k in test_cases:
            res = self.findMinFibonacciNumbers(k)
            print('res: %s' % res)
            print('-='*30 + '-')



if __name__ == '__main__':
    Solution().test()
