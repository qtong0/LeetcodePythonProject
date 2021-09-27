from typing import List


class Solution:
    def minJumps(self, arr: List[int]) -> int:
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
            res = self.minJumps(arr)
            print('res: %s' % res)
            print('-='*30 + '-')


if __name__ == '__main__':
    Solution().test()
