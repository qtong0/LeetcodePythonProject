class Solution:
    def minFlips(self, mat) -> int:
        queue = [(mat, 0)]
        visited = set()
        visited.add(str(mat))
        while queue:
            mat, d = queue.pop(0)
            if self.isValid(mat):
                return d
            neighbors = self.getNeighbors(mat)
            for node in neighbors:
                hash = str(node)
                if hash not in visited:
                    visited.add(hash)
                    queue.append((node, d+1))
        return -1

    def getNeighbors(self, mat):
        res = []
        m, n = len(mat), len(mat[0])
        for i in range(m):
            for j in range(n):
                mat2 = list(list(row) for row in mat)
                mat2[i][j] = 0 if mat[i][j] else 1
                for x, y in (i+1, j), (i, j+1), (i-1, j), (i, j-1):
                    if 0 <= x < m and 0 <= y < n:
                        mat2[x][y] = 0 if mat[x][y] else 1
                res.append(mat2)
        return res

    def isValid(self, mat):
        for row in mat:
            for val in row:
                if val == 1:
                    return False
        return True

    def test(self):
        testCases = [
            [[0,0],[0,1]],
            [[0]],
            [[1,1,1],[1,0,1],[0,0,0]],
            [[1,0,0],[1,0,0]],
        ]
        for mat in testCases:
            res = self.minFlips(mat)
            print('res: %s' % res)
            print('-='*30+'-')


if __name__ == '__main__':
    Solution().test()
