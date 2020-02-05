import collections


class Solution:
    def subarraysWithKDistinct(self, A, K: int) -> int:
        c1 = collections.Counter()
        c2 = collections.Counter()
        d1, d2 = 0, 0
        res = 0
        l1, l2 = 0, 0
        for i, num in enumerate(A):
            c1[num] += 1
            c2[num] += 1
            if c1[num] == 1:
                d1 += 1
            if c2[num] == 1:
                d2 += 1
            while d1 > K:
                n = A[l1]
                c1[n] -= 1
                if c1[n] == 0:
                    d1 -= 1
                l1 += 1
            while d2 >= K:
                n = A[l2]
                c2[n] -= 1
                if c2[n] == 0:
                    d2 -= 1
                l2 += 1
            res += l2 - l1
        return res

    def test(self):
        testCases = [
            [
                [1,2,1,2,3], 2,
            ],
            [
                [1,2,1,3,4], 3,
            ],
        ]
        for arr, k in testCases:
            res = self.subarraysWithKDistinct(arr, k)
            print('res: %s' % res)
            print('-='*30+'-')


if __name__ == '__main__':
    Solution().test()
