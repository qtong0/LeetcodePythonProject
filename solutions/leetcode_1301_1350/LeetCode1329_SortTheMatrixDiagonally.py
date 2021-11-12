from typing import List


class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        m, n = len(mat), len(mat[0])
        for i in range(m-1, -1, -1):
            arr = []
            for j in range(n):
                if 0 <= i+j < m and 0 <= j < n:
                    arr.append(mat[i+j][j])
            arr.sort()
            for j in range(n):
                if 0 <= i+j < m and 0 <= j < n:
                    mat[i+j][j] = arr[j]
        for j in range(1, n):
            arr = []
            for i in range(m):
                if 0 <= i < m and 0 <= j+i < n:
                    arr.append(mat[i][j+i])
            arr.sort()
            for i in range(m):
                if 0 <= i < m and 0 <= j+i < n:
                    mat[i][j+i] = arr[i]
        return mat


    def test(self):
        test_cases = [
            [[3,3,1,1],[2,2,1,2],[1,1,1,2]],
            [[11,25,66,1,69,7],[23,55,17,45,15,52],[75,31,36,44,58,8],[22,27,33,25,68,4],[84,28,14,11,5,50]],
        ]
        for mat in test_cases:
            res = self.diagonalSort(mat)
            print('res: %s' % res)
            print('-='*30 + '-')


if __name__ == '__main__':
    Solution().test()
