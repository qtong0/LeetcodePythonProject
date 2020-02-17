class Solution:
    def numSubmatrixSumTarget(self, matrix, target: int) -> int:
        m, n = len(matrix), len(matrix[0])
        for i in range(m):
            for j in range(1, n):
                matrix[i][j] += matrix[i][j-1]
        res = 0
        for i in range(n):
            for j in range(i, n):
                hashmap = {0: 1}
                preSum = 0
                for k in range(m):
                    val = matrix[k][j]
                    if i > 0:
                        val -= matrix[k][i-1]
                    preSum += val
                    res += hashmap.get(preSum-target, 0)
                    hashmap[preSum] = hashmap.get(preSum, 0) + 1
        return res

    def test(self):
        testCases = [
            [
                [
                    [0,1,0],
                    [1,1,1],
                    [0,1,0],
                ],
                0,
            ],
            [
                [
                    [ 1, -1],
                    [-1,  1],
                ],
                0,
            ],
            [
                [
                    [0,1,0,0,1],
                    [0,0,1,1,1],
                    [1,1,1,0,1],
                    [1,1,0,1,1],
                    [0,1,1,0,0],
                ],
                1,
            ], # 47
        ]
        for matrix, target in testCases:
            res = self.numSubmatrixSumTarget(matrix, target)
            print('res: %s' % res)
            print('-='*30 + '-')


if __name__ == '__main__':
    Solution().test()
