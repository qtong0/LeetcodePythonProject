# Definition for a QuadTree node.
class Node(object):
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight


class Solution(object):
    def construct(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: Node
        """
        n = len(grid)
        return self.helper(grid, 0, n-1, 0, n-1)

    def helper(self, grid, rStart, rEnd, cStart, cEnd):
        if rStart == rEnd and cStart == cEnd:
            val = grid[rStart][cStart]
            node = Node(val, True, None, None, None, None)
            return node
        else:
            rMid = (rStart+rEnd)//2
            cMid = (cStart+cEnd)//2
            topLeft = self.helper(grid, rStart, rMid, cStart, cMid)
            topRight = self.helper(grid, rStart, rMid, cMid+1, cEnd)
            bottomLeft = self.helper(grid, rMid+1, rEnd, cStart, cMid)
            bottomRight = self.helper(grid, rMid+1, rEnd, cMid+1, cEnd)
            if topLeft.isLeaf and topRight.isLeaf and bottomLeft.isLeaf and bottomRight.isLeaf and\
                    topLeft.val == topRight.val == bottomLeft.val == bottomRight.val:
                return Node(topLeft.val, True, None, None, None, None)
            else:
                return Node(1, False, topLeft, topRight, bottomLeft, bottomRight)

    def test(self):
        testCases = [
            # [
            #     [0,1],
            #     [1,0],
            # ],
            [
                [1,1,1,1,0,0,0,0],
                [1,1,1,1,0,0,0,0],
                [1,1,1,1,1,1,1,1],
                [1,1,1,1,1,1,1,1],
                [1,1,1,1,0,0,0,0],
                [1,1,1,1,0,0,0,0],
                [1,1,1,1,0,0,0,0],
                [1,1,1,1,0,0,0,0],
            ],
        ]
        for grid in testCases:
            res = self.construct(grid)


if __name__ == '__main__':
    Solution().test()
