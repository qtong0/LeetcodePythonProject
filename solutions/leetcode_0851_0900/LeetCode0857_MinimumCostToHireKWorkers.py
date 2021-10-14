from typing import List


class Solution(object):
    def mincostToHireWorkers(self, quality: List[int], wage: List[int], K: int) -> float:
        import heapq
        k = K
        workers = sorted([float(w)/q, q] for w, q in zip(wage, quality))
        res = float('inf')
        qsum = 0
        heap = []
        for r, q, in workers:
            heapq.heappush(heap, -q)
            qsum += q
            if len(heap) > k:
                qsum += heapq.heappop(heap)
            if len(heap) == k:
                res = min(res, qsum*r)
        return res
    
    def test(self):
        testCases = [
            [[10,20,5], [70,50,30], 2],
            [[3,1,10,10,1], [4,8,2,2,7], 3],
        ]
        for quality, wage, k in testCases:
            res = self.mincostToHireWorkers(quality, wage, k)
            print('res: %s' % res)
            print('-='*30 + '-')


if __name__ == '__main__':
    Solution().test()
