class Solution:
    def intervalIntersection(self, A, B):
        A, B = sorted(A), sorted(B)
        res = []
        i, j = 0, 0
        while i < len(A):
            while j < len(B) and B[j][1] < A[i][0]:
                j += 1
            if j < len(B) and B[j][0] <= A[i][1]:
                res.append([max(A[i][0], B[j][0]), min(A[i][1], B[j][1])])
            if j < len(B) and A[i][1] >= B[j][1]:
                j += 1
            else:
                i += 1
        return res

    def test(self):
        testCases = [
            [
                [[0,2],[5,10],[13,23],[24,25]],
                [[1,5],[8,12],[15,24],[25,26]],
            ],
        ]
        for A, B in testCases:
            res = self.intervalIntersection(A, B)
            print('res: %s' % res)
            print('-='*30+'-')


if __name__ == '__main__':
    Solution().test()
