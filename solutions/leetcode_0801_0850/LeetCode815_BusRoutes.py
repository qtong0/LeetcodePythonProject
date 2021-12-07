from typing import List


class Solution(object):
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        if source == target:
            return 0
        hashmap = {}
        for i in range(len(routes)):
            for j in range(len(routes[i])):
                if routes[i][j] not in hashmap:
                    hashmap[routes[i][j]] = []
                hashmap[routes[i][j]].append(i)
        queue = []
        addedRoute = set()
        addedStop = set()
        for r in hashmap[source]:
            if r in addedRoute: continue
            for i in range(len(routes[r])):
                if routes[r][i] not in addedStop:
                    queue.append(routes[r][i])
                    addedStop.add(routes[r][i])
            addedRoute.add(r)
        count = 0
        while queue:
            size = len(queue)
            count += 1
            for _ in range(size):
                stop = queue.pop(0)
                if stop == target:
                    return count
                for r in hashmap[stop]:
                    if r in addedRoute: continue
                    for i in range(len(routes[r])):
                        if routes[r][i] not in addedStop:
                            queue.append(routes[r][i])
                    addedRoute.add(r)
        return -1



    def test(self):
        testCases = [
            [
                [[1, 2, 7], [3, 6, 7]],
                1, 6,
            ], # 2
            [
                [[7,12],[4,5,15],[6],[15,19],[9,12,13]],
                15,12
            ],
        ]
        for routes, s, t in testCases:
            result = self.numBusesToDestination(routes, s, t)
            print('result: %s' % result)
            print('-='*30+'-')



if __name__ == '__main__':
    Solution().test()
