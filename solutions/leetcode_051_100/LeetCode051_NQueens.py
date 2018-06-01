'''
Created on Jan 21, 2017

@author: MT
'''

class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        if n <= 0: return []
        result = []
        row = [0]*n
        self.helper(row, result, n, 0)
        return result
    
    def helper(self, row, result, n, ind):
        if ind == n:
            elem = self.translateString(row)
            result.append(list(elem))
            return
        for i in range(n):
            if self.isValid(row, ind, i):
                row[ind] = i
                self.helper(row, result, n, ind+1)
                row[ind] = 0
    
    def translateString(self, row):
        result = []
        for i in range(len(row)):
            s = ''
            for j in range(len(row)):
                if j == row[i]:
                    s += 'Q'
                else:
                    s += '.'
            result.append(s)
        return result
    
    def isValid(self, row, rowNum, colNum):
        for i in range(rowNum):
            if row[i] == colNum:
                return False
            if abs(row[i] - colNum) == abs(i-rowNum):
                return False
        return True
    
    def test(self):
        result = self.solveNQueens(4)
        print(result)
        print()
        result = self.solveNQueens(5)
        print(result)

if __name__ == '__main__':
    Solution().test()