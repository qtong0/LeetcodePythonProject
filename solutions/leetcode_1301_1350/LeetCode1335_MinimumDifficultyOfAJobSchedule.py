from typing import List


class Solution:
    # TC: O(N*D)
    # SC: O(N*D)
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        n = len(jobDifficulty)
        if n < d:
            return -1
        memo = [[-1]*n for _ in range(d+1)]
        return self.dfs(d, 0, jobDifficulty, memo)

    def dfs(self, d, i, jobs, memo):
        n = len(jobs)
        if d == 0 and i == n:
            return 0
        if d == 0 or i == n:
            return float('inf')
        if memo[d][i] != -1:
            return memo[d][i]
        cur_max = jobs[i]
        min_val = float('inf')
        for j in range(i, n):
            cur_max = max(cur_max, jobs[j])
            tmp = self.dfs(d-1, j+1, jobs, memo)
            if tmp != float('inf'):
                min_val = min(min_val, cur_max + tmp)
        memo[d][i] = min_val
        return memo[d][i]

    def test(self):
        test_cases = [
            [[1, 1, 1], 3],
            [[6, 5, 4, 3, 2, 1], 2],
            [[9, 9, 9], 4],
            [[7, 1, 7, 1, 7, 1], 3],
            [[11, 111, 22, 222, 33, 333, 44, 444], 6],
        ]
        for jobDifficulty, d in test_cases:
            res = self.minDifficulty(jobDifficulty, d)
            print('res: %s' % res)
            print('-=' * 30 + '-')


if __name__ == '__main__':
    Solution().test()
