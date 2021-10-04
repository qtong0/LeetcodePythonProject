from typing import List


class Solution:
    #
    # 1. Find all the reachable nodes without changing anything
    # 2. Save all new visited nodes to a queue bfs.
    # 3. Now iterate the queue
    #       3.1 For each node, try changing it to all 3 other direction
    #       3.2 Save the new reachable and not visited nodes to the queue
    #       3.3 repeat step 3
    #
    # Time O(n*m)
    # Space O(n*m)
    #
    def minCost(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        dp = [[float('inf')]*n for _ in range(m)]
        self.DIR = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        cost = 0
        queue = []
        self.dfs(0, 0, grid, dp, cost, queue)
        while queue:
            cost += 1
            for _ in range(len(queue)):
                x, y = queue.pop(0)
                for i in range(4):
                    self.dfs(x+self.DIR[i][0], y+self.DIR[i][1], grid, dp, cost, queue)
        return dp[-1][-1]

    def dfs(self, x, y, grid, dp, cost, queue):
        m, n = len(grid), len(grid[0])
        if not (0 <= x < m and 0 <= y < n and dp[x][y] == float('inf')):
            return
        dp[x][y] = cost
        queue.append([x, y])
        nextDir = grid[x][y] - 1
        self.dfs(x+self.DIR[nextDir][0], y+self.DIR[nextDir][1], grid, dp, cost, queue)

    def test(self):
        test_cases = [
            [[1,1,1,1],[2,2,2,2],[1,1,1,1],[2,2,2,2]],
            [[1,1,3],[3,2,2],[1,1,4]],
            [[1,2],[4,3]],
            [[2,2,2],[2,2,2]],
            [[4]],
        ]
        for grid in test_cases:
            res = self.minCost(grid)
            print('res: %s' % res)
            print('-='*30 + '-')


if __name__ == '__main__':
    Solution().test()
