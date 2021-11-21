from typing import List


class Solution:
    def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:
        graph = [[] for _ in range(n)]
        degrees = [0]*n
        for n1, n2 in relations:
            n1, n2 = n1-1, n2-1
            graph[n1].append(n2)
            degrees[n2] += 1

        queue = []
        dist = [0]*n
        for i in range(n):
            if degrees[i] == 0:
                queue.append(i)
                dist[i] = time[i]

        while queue:
            node = queue.pop(0)
            for nei in graph[node]:
                # Update `dist[node]` using the maximum dist of the predecessor nodes
                dist[nei] = max(dist[nei], dist[node] + time[nei])
                degrees[nei] -= 1
                if degrees[nei] == 0:
                    queue.append(nei)
        return max(dist)


    def test(self):
        test_cases = [
            [3, [[1,3],[2,3]], [3,2,5]],
            [5, [[1,5],[2,5],[3,5],[3,4],[4,5]], [1,2,3,4,5]],
            [
                9,
                [[2,7],[2,6],[3,6],[4,6],[7,6],[2,1],[3,1],[4,1],[6,1],[7,1],[3,8],[5,8],[7,8],[1,9],[2,9],[6,9],[7,9]],
                [9,5,9,5,8,7,7,8,4],
            ],
        ]
        for n, relations, time in test_cases:
            res = self.minimumTime(n, relations, time)
            print('res: %s' % res)
            print('-='*30 + '-')


if __name__ == '__main__':
    Solution().test()
