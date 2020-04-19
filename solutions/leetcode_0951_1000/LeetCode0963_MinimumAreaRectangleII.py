import itertools, math


class Solution:
    # O(N^2 * log(N))
    def minAreaFreeRect(self, points) -> float:
        seen = {}
        n = len(points)
        for i in range(n):
            for j in range(i+1, n):
                p1, p2 = points[i], points[j]
                center = p1[0]+p2[0], p1[1]+p2[1]
                r2 = (p1[0]-p2[0])**2 + (p1[1]-p2[1])**2
                if r2 not in seen:
                    seen[r2] = {}
                if center not in seen[r2]:
                    seen[r2][center] = []
                seen[r2][center].append(p1)
        res = float('inf')
        for info in seen.values():
            for center, candidates in info.items():
                m = len(candidates)
                for i in range(m):
                    for j in range(i+1, m):
                        p1 = candidates[i]
                        p2 = candidates[j]
                        p3 = tuple(center)
                        p3 = p3[0]-p2[0], p3[1]-p2[1]
                        area = math.sqrt( (p1[0]-p2[0])**2 + (p1[1]-p2[1])**2 ) * \
                            math.sqrt( (p1[0]-p3[0])**2 + (p1[1]-p3[1])**2 )
                        res = min(res, area)
        return res if res != float('inf') else 0



    def minAreaFreeRect_slow(self, points) -> float:
        EPS = 1e-7
        points = set(map(tuple, points))
        res = float('inf')
        for p1, p2, p3 in itertools.permutations(points, 3):
            p4 = p2[0]+p3[0]-p1[0], p2[1]+p3[1]-p1[1]
            if p4 in points:
                v21 = complex(p2[0]-p1[0], p2[1]-p1[1])
                v31 = complex(p3[0]-p1[0], p3[1]-p1[1])
                if abs(v21.real * v31.real + v21.imag * v31.imag) < EPS:
                    area = abs(v21) * abs(v31)
                    if area < res:
                        res = area
        return res if res < float('inf') else 0


    def test(self):
        testCases = [
            [[1,2],[2,1],[1,0],[0,1]],
        ]
        for points in testCases:
            res = self.minAreaFreeRect(points)
            print('res: %s' % res)
            print('-='*30+'-')


if __name__ == '__main__':
    Solution().test()
