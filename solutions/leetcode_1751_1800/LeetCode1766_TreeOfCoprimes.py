from typing import List


class Solution:
    # TC: O(50 ^ N)
    # SC: O(N)
    #
    def getCoprimes(self, nums: List[int], edges: List[List[int]]) -> List[int]:
        n = len(nums)
        graph = [[] for _ in range(n)]

        for n1, n2 in edges:
            graph[n1].append(n2)
            graph[n2].append(n1)

        path = [[] for _ in range(51)]
        seen = set()
        res = [-1]*n

        def dfs(node, depth):
            if node in seen:
                return
            seen.add(node)
            largestDepth = -1
            for x in range(1, 51):
                # co-prime
                if self.gcd(nums[node], x) == 1:
                    if len(path[x]) > 0:
                        topNode, topDepth = path[x][-1]
                        # Pick node has largest Depth and co-prime with current node as our ancestor node
                        if largestDepth < topDepth:
                            largestDepth = topDepth
                            res[node] = topNode
            path[nums[node]].append((node, depth))
            for nei in graph[node]:
                dfs(nei, depth+1)
            path[nums[node]].pop()

        dfs(0, 0)
        return res

    def gcd(self, a, b):
        while b != 0:
            tmp = b
            b = a % b
            a = tmp
        return a


    def test(self):
        test_cases = [
            [[2,3,3,2], [[0,1],[1,2],[1,3]]],
            [[5,6,10,2,3,6,15], [[0,1],[0,2],[1,3],[1,4],[2,5],[2,6]]],
        ]
        for nums, edges in test_cases:
            res = self.getCoprimes(nums, edges)
            print('res: %s' % res)
            print('-='*30 + '-')


if __name__ == '__main__':
    Solution().test()
