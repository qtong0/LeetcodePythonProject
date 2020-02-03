class Solution:
    def addToArrayForm(self, A, K: int):
        i = 0
        toAdd = 0
        while K > 0:
            mod = K % 10
            K = K // 10
            if i < len(A):
                mod += A[len(A)-1-i] + toAdd
            else:
                mod += toAdd
            if mod >= 10:
                mod -= 10
                toAdd = 1
            else:
                toAdd = 0
            if i < len(A):
                A[len(A)-1-i] = mod
            else:
                A.insert(0, mod)
            i += 1
        while toAdd:
            if i < len(A):
                val = A[len(A)-1-i] + toAdd
            else:
                val = toAdd
            if val >= 10:
                val -= 10
                toAdd = 1
            else:
                toAdd = 0
            if i < len(A):
                A[len(A)-1-i] = val
            else:
                A.insert(0, val)
            i += 1
        return A

    def test(self):
        testCases = [
            [
                [0],
                23,
            ],
            [
                [2,1,5],
                806,
            ],
            # [
            #     [1,2,0,0],
            #     34,
            # ],
            # [
            #     [9,9,9,9,9,9,9,9,9,9],
            #     1,
            # ],
        ]
        for arr, k in testCases:
            res = self.addToArrayForm(arr, k)
            print('res: %s' % res)
            print('-='*30+'-')


if __name__ == '__main__':
    Solution().test()
