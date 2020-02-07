class Solution(object):
    def minDominoRotations(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: int
        """
        def check(x):
            rotations_a, rotations_b = 0, 0
            for i in range(n):
                if A[i] != x and B[i] != x:
                    return -1
                elif A[i] != x:
                    rotations_a += 1
                elif B[i] != x:
                    rotations_b += 1
            return min(rotations_a, rotations_b)

        n = len(A)
        rotations = check(A[0])
        if rotations != -1 or A[0] == B[0]:
            return rotations
        else:
            return check(B[0])

    def test(self):
        testCases = [
            [
                [2,1,2,4,2,2],
                [5,2,6,2,3,2],
            ],
            # [
            #     [3,5,1,2,3],
            #     [3,6,3,3,4],
            # ],
        ]
        for arrA, arrB in testCases:
            res = self.minDominoRotations(arrA, arrB)
            print('res: %s' % res)
            print('-='*30 + '-')


if __name__ == '__main__':
    Solution().test()
