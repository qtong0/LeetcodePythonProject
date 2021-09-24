class Solution:
    def maxPoints(self, points: list[list[int]]) -> int:
        if not points or not points[0]:
            return 0
        m, n = len(points), len(points[0])
        prev = list(points[0])
        for i in range(1, m):
            left = [0]*n
            left[0] = prev[0]
            right = [0]*n
            right[-1] = prev[-1]
            curr = [0]*n
            for j in range(1, n):
                left[j] = max(left[j-1] - 1, prev[j])
            for j in range(n-2, -1, -1):
                right[j] = max(right[j+1] - 1, prev[j])
            for j in range(n):
                curr[j] = points[i][j] + max(left[j], right[j])
            prev = curr
        return max(prev)

    # my own solution, NOT good enough, :(
    # !!Don't use!! Applying left & right two-pass will make it better
    def maxPoints_own_TLE(self, points: list[list[int]]) -> int:
        if not points or not points[0]:
            return 0
        m, n = len(points), len(points[0])
        dp = list(points[0])
        for i in range(1, m):
            new_dp = [float('-inf')]*n
            for j in range(n):
                for k in range(n):
                    diff = j-k if j>k else k-j
                    new_dp[j] = max(new_dp[j], dp[k] + points[i][j] - diff)
            dp = new_dp
        return max(dp)

    def test(self):
        test_cases = [
            [[1,2,3],[1,5,1],[3,1,1]],
            [[1,5],[2,3],[4,2]],
        ]
        for points in test_cases:
            res = self.maxPoints(points)
            print('res: %s' % res)
            print('-='*30+'-')


if __name__ == '__main__':
    Solution().test()
