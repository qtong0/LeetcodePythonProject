from typing import List


class Solution:
    # Topological Sort!
    # Time: O (N+E)
    # Space: O (N+E)
    def minimumSemesters(self, N: int, relations: List[List[int]]) -> int:
        graph = [[] for _ in range(N+1)]
        degree = [0]*(N+1)
        for prev, curr in relations:
            graph[prev].append(curr)
            degree[curr] += 1
        queue = []
        for node in range(1, N+1):
            if degree[node] == 0:
                queue.append(node)
        level = 0
        count = 0
        while queue:
            level += 1
            for _ in range(len(queue)):
                node = queue.pop(0)
                count += 1
                for node1 in graph[node]:
                    degree[node1] -= 1
                    if degree[node1] == 0:
                        queue.append(node1)
        return level if count == N else -1

    def test(self):
        test_cases = [
            [3, [[1,3],[2,3]]],
            [3, [[1,2],[2,3],[3,1]]],
        ]
        for n, relations in test_cases:
            res = self.minimumSemesters(n, relations)
            print('res: %s' % res)
            print('-='*30 + '-')


if __name__ == '__main__':
    Solution().test()
