# """
# This is GridMaster's API interface.
# You should not implement it, or speculate about its implementation
# """
class GridMaster(object):
    def canMove(self, direction: str) -> bool:
        pass

    def move(self, direction: str) -> bool:
        pass

    def isTarget(self) -> None:
        pass


class Solution(object):
    # DFS O(MN) + BFS(O(MN))
    def findShortestPath(self, master: 'GridMaster') -> int:
        self.dirs = {'U': (-1, 0), 'D': (1, 0), 'L': (0, -1), 'R': (0, 1)}
        self.anti = {'U': 'D', 'D': 'U', 'L': 'R', 'R': 'L'}

        valid = {}
        valid[(0, 0)] = master.isTarget()
        self.dfs(0, 0, valid, master)
        seen = set()
        queue = [(0,0,0)]

        while queue:
            i, j, step = queue.pop(0)
            if valid[(i, j)] is True:
                return step
            for x, y in (i+1, j), (i-1, j), (i, j+1), (i, j-1):
                if (x, y) in valid and (x, y) not in seen:
                    seen.add((x, y))
                    queue.append((x, y, step+1))
        return -1

    def dfs(self, i, j, valid, master):
        for d, (dr, dc) in self.dirs.items():
            x, y = i + dr, j + dc
            if (x, y) not in valid and master.canMove(d):
                master.move(d)
                valid[(x, y)] = master.isTarget()
                self.dfs(x, y, valid, master)
                master.move(self.anti[d])
