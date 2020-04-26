"""
Explanation
Find the index i of the next maximum number x.
Reverse i + 1 numbers, so that the x will be at A[0]
Reverse x numbers, so that x will be at A[x - 1].
Repeat this process N times.
"""


class Solution:
    def pancakeSort(self, A):
        res = []
        for x in range(len(A), 0, -1):
            i = 0
            while A[i] != x:
                i += 1
            self.reverse(A, i+1)
            res.append(i+1)
            self.reverse(A, x)
            res.append(x)
        return res

    def reverse(self, nums, k):
        i, j = 0, k-1
        while i < j:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
            j -= 1

    def test(self):
        testCases = [
            [3,2,4,1],
            [1,2,3],
        ]
        for arr in testCases:
            res = self.pancakeSort(arr)
            print('res: %s' % res)
            print('-='*30 + '-')


if __name__ == '__main__':
    Solution().test()
