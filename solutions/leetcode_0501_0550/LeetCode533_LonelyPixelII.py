class Solution:
    def findBlackPixel(self, picture, N: int) -> int:
        if not picture or not picture[0]:
            return 0
        m, n = len(picture), len(picture[0])
        colCounts = [0]*n
        hashmap= {}
        for i in range(m):
            s = ''
            rowCount = 0
            for j in range(n):
                s += picture[i][j]
                if picture[i][j] == 'B':
                    rowCount += 1
                    colCounts[j] += 1
            if rowCount != N:
                s = ''
            hashmap[s] = hashmap.get(s, 0) + 1
        res = 0
        for row, count in hashmap.items():
            if count == N:
                for j in range(n):
                    if row and row[j] == 'B' and colCounts[j] == N:
                        res += N
        return res
