from typing import List


class Solution:
    # Bidirectional BFS, faster than below
    # Time O(N)
    # Space O(N)
    #
    def minJumps(self, arr: List[int]) -> int:
        n = len(arr)
        if n <= 1:
            return 0
        graph = {}
        for i in range(n):
            if arr[i] in graph:
                graph[arr[i]].append(i)
            else:
                graph[arr[i]] = [i]

        # stores layers from start
        curs = set([0])
        visited = {0, n-1}
        step = 0

        # stores layer from end
        other = set([n-1])

        while curs:
            if len(curs) > len(other):
                # search from the side with fewer nodes
                curs, other = other, curs
            next_set = set()

            for node in curs:
                for next_node in graph[arr[node]]:
                    if next_node in other:
                        return step+1
                    if next_node not in visited:
                        visited.add(next_node)
                        next_set.add(next_node)

                # clear the list to prevent redundant search
                graph[arr[node]].clear()

                for next_node in [node-1, node+1]:
                    if next_node in other:
                        return step + 1
                    if 0 <= next_node < len(arr) and next_node not in visited:
                        visited.add(next_node)
                        next_set.add(next_node)

            curs = next_set
            step += 1

        return -1


    # TLE
    # Time O(N)
    # Space O(N)
    #
    def minJumps_TLE(self, arr: List[int]) -> int:
        n = len(arr)
        hashmap = {}
        for i, val in enumerate(arr):
            hashmap[val] = hashmap.get(val, []) + [i]

        queue = [[0, 0]]
        visited, visited_graph = set(), set()
        while queue:
            steps, idx = queue.pop(0)
            if idx == n-1:
                return steps

            for neib in [idx-1, idx+1]:
                if 0 <= neib < n and neib not in visited:
                    visited.add(neib)
                    queue.append([steps+1, neib])
            if arr[idx] not in visited_graph:
                for neib in hashmap[arr[idx]]:
                    if neib not in visited:
                        visited.add(neib)
                        queue.append([steps+1, neib])
                visited_graph.add(arr[idx])
        return -1

    def test(self):
        test_cases = [
            [100,-23,-23,404,100,23,23,23,3,404],
            [7],
            [7,6,9,6,9,6,9,7],
            [6,1,9],
            [11,22,7,7,7,7,7,7,7,22,13],
        ]
        for arr in test_cases:
            res_1 = self.minJumps(arr)
            res_2 = self.minJumps_TLE(arr)
            print('res_1: %s' % res_1)
            print('res_2: %s' % res_2)
            print('-='*30 + '-')


if __name__ == '__main__':
    Solution().test()
