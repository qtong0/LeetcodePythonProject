from typing import List


#   This is the custom function interface.
#   You should not implement it, or speculate about its implementation
class CustomFunction:
    # Returns f(x, y) for any given positive integers x and y.
    # Note that f(x, y) is increasing with respect to both x and y.
    # i.e. f(x, y) < f(x + 1, y), f(x, y) < f(x, y + 1)
    def f(self, x, y):
        pass


class Solution:
    # Rephrase the problem:
    # Given a matrix, each row and each column is increasing.
    # Find all coordinates (i,j) that A[i][j] == z
    # O(X + Y) - binary search might not be necessary
    #
    def findSolution(self, customfunction: 'CustomFunction', z: int) -> List[List[int]]:
        res = []
        y = 1000
        for x in range(1, 1000):
            while y > 1 and customfunction.f(x, y) > z:
                y -= 1
            if customfunction.f(x, y) == z:
                res.append([x, y])
        return res
