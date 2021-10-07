class Solution:
    def __init__(self):
        self.dp = {}

    def minDays(self, n: int) -> int:
        if n <= 1:
            return n
        if n not in self.dp:
            self.dp[n] = 1+min(n%2 + self.minDays(n//2), n%3 + self.minDays(n//3))
        return self.dp[n]

    # Another my own solution, it's better than BFS
    # but O(N) is not good enough because days <= N
    def minDays_own_dp_TLE(self, n: int) -> int:
        if n == 1:
            return 1
        dp = list(range(n+1))
        for i in range(1, n+1):
            dp[i] = min(dp[i], dp[i-1] + 1)
            if i % 2 == 0:
                dp[i] = min(dp[i], dp[i//2] + 1)
            if i % 3 == 0:
                dp[i] = min(dp[i], dp[i-2*i//3] + 1)
        return dp[-1]

    # BFS is TLE :(
    def minDays_own_bfs_TLE(self, n: int) -> int:
        queue = [n]
        days = 0
        while queue:
            for _ in range(len(queue)):
                node = queue.pop(0)
                if node == 0:
                    return days
                queue.append(node-1)
                if node % 2 == 0:
                    queue.append(node//2)
                if node % 3 == 0:
                    queue.append(node-2*node//3)
            days += 1
        return n

    def test(self):
        test_cases = [
            10,
            6,
            1,
            56,
            84703,
        ]
        for n in test_cases:
            res_1 = self.minDays(n)
            res_2 = self.minDays_own_bfs_TLE(n)
            print('res_1: %s' % res_1)
            print('res_2: %s' % res_2)
            print('-='*30 + '-')


if __name__ == '__main__':
    Solution().test()
