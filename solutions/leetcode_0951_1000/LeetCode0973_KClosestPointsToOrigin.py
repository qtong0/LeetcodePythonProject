import heapq


class Solution:
    def kClosest(self, points, K):
        if K < 1 or not points:
            return []
        self.helper(points, 0, len(points)-1, K-1)
        return points[:K]

    def helper(self, points, i, j, k):
        i0, j0 = i, j
        pivot = self.dist(points[j])
        while True:
            while i < j and self.dist(points[i]) < pivot:
                i += 1
            while i < j and self.dist(points[j]) >= pivot:
                j -= 1
            if i < j:
                points[i], points[j] = points[j], points[i]
            else:
                break
        points[i], points[j0] = points[j0], points[i]
        if i == k:
            return
        elif i < k:
            self.helper(points, i+1, j0, k)
        else:
            self.helper(points, i0, i-1, k)

    def dist(self, p):
        return p[0]**2 + p[1]**2



    def kClosest_heap(self, points, K):
        heap = []
        for p in points:
            heapq.heappush(heap, (p[0]**2 + p[1]**2, p))
        res = []
        for _ in range(K):
            res.append(heapq.heappop(heap)[1])
        return res


    def test(self):
        testCases = [
            [[[1,3],[-2,2]], 1],
            [[[3,3],[5,-1],[-2,4]], 2],
            [
                [[0,1],[1,0]],
                2,
            ],
        ]
        for points, k in testCases:
            res = self.kClosest(points, k)
            print('res: %s' % res)
            print('-='*30+'-')


if __name__ == '__main__':
    Solution().test()
