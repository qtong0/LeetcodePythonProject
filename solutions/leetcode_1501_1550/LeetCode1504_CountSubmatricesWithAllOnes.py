from typing import List


class Solution:
    def numSubmat(self, mat: List[List[int]]) -> int:
        m, n = len(mat), len(mat[0])
        res = 0

        heights = [0]*n
        for i in range(m):
            for j in range(n):
                heights[j] = heights[j] + 1 if mat[i][j] else 0
            res += self.helper(heights)
        return res

    def helper(self, heights):
        n = len(heights)
        sums = [0]*n
        stack = []

        for i in range(n):
            while stack and heights[stack[-1]] >= heights[i]:
                stack.pop()
            if stack:
                pre = stack[-1]
                sums[i] = sums[pre]
                sums[i] += heights[i] * (i-pre)
            else:
                sums[i] = heights[i] * (i+1)
            stack.append(i)

        return sum(sums)


    def test(self):
        test_cases = [
            [
                [1,0,1],
                [0,1,0],
                [1,0,1]
            ],
            [
                [0,0,0],
                [0,0,0],
                [0,1,1],
                [1,1,0],
                [0,1,1]
            ],
            [
                [1, 1],
                [1, 1],
            ],
            [
                [1,0,1],
                [1,1,0],
                [1,1,0],
            ],
            [
                [0,1,1,0],
                [0,1,1,1],
                [1,1,1,0],
            ],
            [[1,1,1,1,1,1]],
            [[1,1,1,1,0,1,0],[1,1,1,0,0,0,1],[0,1,1,1,1,0,0],[1,1,0,1,1,0,1],[1,0,0,0,0,0,1],[1,1,0,1,1,1,1],[1,1,0,0,1,1,1]],
        ]
        for mat in test_cases:
            res = self.numSubmat(mat)
            print('res: %s' % res)
            print('-='*30 + '-')


if __name__ == '__main__':
    Solution().test()
