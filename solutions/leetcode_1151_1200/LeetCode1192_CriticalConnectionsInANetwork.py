from typing import List


class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        graph = [[] for _ in range(n)]
        for n1, n2 in connections:
            graph[n1].append(n2)
            graph[n2].append(n1)

        currRank = 0
        lowestRank = [i for i in range(n)]

        res = []
        visited = [False]*n
        currNode = 0
        prevNode = -1
        self.dfs(res, graph, lowestRank, visited, currRank, prevNode, currNode)
        return res

    def dfs(self, res, graph, lowestRank, visited, currRank, prevNode, currNode):
        visited[currNode] = True
        lowestRank[currNode] = currRank

        for nei in graph[currNode]:
            if nei == prevNode:
                continue
            if not visited[nei]:
                self.dfs(res, graph, lowestRank, visited, currRank+1, currNode, nei)
            lowestRank[currNode] = min(lowestRank[currNode], lowestRank[nei])
            if lowestRank[nei] >= currRank + 1:
                res.append([currNode, nei])


    # My own solution, Brute force by removing connections and check how many notes connected, TLE
    def criticalConnections_own_TLE(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        graph = [set() for _ in range(n)]
        for n1, n2 in connections:
            graph[n1].add(n2)
            graph[n2].add(n1)

        res = []
        for n1, n2 in connections:
            visited = [False] * n
            visited[n1] = True
            graph[n1].remove(n2)
            graph[n2].remove(n1)
            if n != self.dfs2(graph, n1, visited):
                res.append([n1, n2])
            graph[n1].add(n2)
            graph[n2].add(n1)
        return res

    def dfs2(self, graph, n1, visited):
        res = 1
        for nei in graph[n1]:
            if not visited[nei]:
                visited[nei] = True
                res += self.dfs2(graph, nei, visited)
        return res


    def test(self):
        test_cases = [
            [4, [[0,1],[1,2],[2,0],[1,3]]],
            [2, [[0,1]]],
        ]
        for n, connections in test_cases:
            res = self.criticalConnections(n, connections)
            print('res: %s' % res)
            print('-='*30 + '-')


if __name__ == '__main__':
    Solution().test()
