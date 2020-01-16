import collections

class Solution(object):
    def minIncrementForUnique(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        A.sort()
        A.append(100000)
        res = taken = 0
        for i in range(1, len(A)):
            if A[i] == A[i-1]:
                taken += 1
                res -= A[i]
            else:
                give = min(taken, A[i]-A[i-1]-1)
                res += give*(give+1)//2 + give*A[i-1]
                taken -= give
        return res

    def test(self):
        testCases = [
            # [1,2,2],
            # [3,2,1,2,1,7],
            [7,2,7,2,1,4,3,1,4,8],
        ]
        for arr in testCases:
            res = self.minIncrementForUnique(arr)
            print('res: %s' % res)
            print('-='*30+'-')


if __name__ == '__main__':
    Solution().test()
