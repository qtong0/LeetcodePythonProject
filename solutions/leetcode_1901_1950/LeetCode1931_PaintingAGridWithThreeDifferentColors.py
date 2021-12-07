from functools import lru_cache


class Solution:
    def colorTheGrid(self, m: int, n: int) -> int:
        # Get color of the bitMask as pos, use 2 bits to store a color
        def getColor(mask, pos):
            return (mask >> (2 * pos)) & 3

        # Set color to the mask at pos, use 2 bits to store a color
        def setColor(mask, pos, color):
            return mask | (color << (2 * pos))

        def dfs(r, curColMask, prevColMask, out):
            # Filled full color for this column
            if r == m:
                out.append(curColMask)
                return
            # try different colors
            for i in [1, 2, 3]:
                if getColor(prevColMask, r) != i and (r == 0 or getColor(curColMask, r-1) != i):
                    dfs(r+1, setColor(curColMask, r, i), prevColMask, out)

        @lru_cache(None)
        # Generate all possible columns as we can draw, if the previous col is 'prevColMask'
        def neighbor(prevColMask):
            out = []
            dfs(0, 0, prevColMask, out)
            return out

        @lru_cache(None)
        def dp(c, prevColMask):
            # Found a valid way
            if c == n:
                return 1
            res = 0
            for nei in neighbor(prevColMask):
                res = (res + dp(c+1, nei)) % 1_000_000_007
            return res

        return dp(0, 0)



if __name__ == '__main__':
    Solution().test()
