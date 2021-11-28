from typing import List


class Solution:
    # DFS + Memorization / Top Down
    # TC: O(N^3)
    # SC: O(N^2)
    #
    def minCost(self, n: int, cuts: List[int]) -> int:
        cuts.append(0)
        cuts.append(n)
        cuts.sort()
        return self.dfs(cuts, 0, len(cuts)-1, {})

    def dfs(self, cuts, i, j, memo):
        if j - i <= 1:
            return 0
        if (i, j) not in memo:
            memo[(i, j)] = float('inf')
            for k in range(i+1, j):
                memo[(i, j)] = min(
                    memo[(i, j)],
                    cuts[j] - cuts[i] + self.dfs(cuts, i, k, memo) + self.dfs(cuts, k, j, memo)
                )
        return memo[(i, j)]


    def test(self):
        test_cases = [
            [7, [1,3,4,5]],
            [9, [5,6,1,4,2]],
            [13, [3,12,1,5,9,11,4,8,7,2,6,10]],
        ]
        for n, cuts in test_cases:
            res = self.minCost(n, cuts)
            print('res: %s' % res)
            print('-='*30 + '-')


if __name__ == '__main__':
    Solution().test()
