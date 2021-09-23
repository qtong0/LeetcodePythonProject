class Solution:
    def findMaxValueOfEquation(self, points: list[list[int]], k: int) -> int:
        deque = []
        res = float('-inf')
        for x, y in points:
            while deque and deque[0][1] < x-k:
                deque.pop(0)
            if deque:
                res = max(res, deque[0][0] + y+x)
            while deque and deque[-1][0] <= y-x:
                deque.pop()
            deque.append([y-x, x])
        return res

    def test(self):
        test_cases = [
            [[[1,3],[2,0],[5,10],[6,-10]], 1],
            [[[0,0],[3,0],[9,2]], 3],
            [[[-19,-12],[-13,-18],[-12,18],[-11,-8],[-8,2],[-7,12],[-5,16],[-3,9],[1,-7],[5,-4],[6,-20],[10,4],[16,4],[19,-9],[20,19]], 6],
        ]
        for points, k in test_cases:
            res = self.findMaxValueOfEquation(points, k)
            print('res: %s' % res)
            print('-='*30+'-')


if __name__ == '__main__':
    Solution().test()
