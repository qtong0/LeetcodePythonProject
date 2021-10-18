from typing import List
import heapq


class Solution:
    # TC: O(N*Log(K))
    # SC: O(K)
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        n = len(heights)
        heap = []
        for i in range(n-1):
            d = heights[i+1] - heights[i]
            if d > 0:
                heapq.heappush(heap, d)
            if len(heap) > ladders:
                bricks -= heapq.heappop(heap)
            if bricks < 0:
                return i
        return len(heights) - 1



    # DFS - TLE
    def furthestBuilding_DFS_TLE(self, heights: List[int], bricks: int, ladders: int) -> int:
        if len(heights) <= 1:
            return len(heights)
        return self.dfs(heights, bricks, ladders, 0)

    def dfs(self, heights, bricks, ladders, idx):
        n = len(heights)
        if idx >= n - 1:
            return n - 1
        while idx + 1 < n and heights[idx] >= heights[idx + 1]:
            idx += 1
        res = idx
        if ladders > 0:
            res = max(res, self.dfs(heights, bricks, ladders - 1, idx + 1))
        if idx + 1 < n and bricks >= heights[idx + 1] - heights[idx]:
            res = max(res, self.dfs(heights, bricks - (heights[idx + 1] - heights[idx]), ladders, idx + 1))
        return res

    def test(self):
        test_cases = [
            [[4,2,7,6,9,14,12], 5, 1],
            [[4,12,2,7,3,18,20,3,19], 10, 2],
            [[14,3,19,3], 17, 0],
        ]
        for heights, bricks, ladders in test_cases:
            res = self.furthestBuilding(heights, bricks, ladders)
            print('res: %s' % res)
            print('-='*30 + '-')


if __name__ == '__main__':
    Solution().test()
