class Solution(object):
    def reachingPoints(self, sx: int, sy: int, tx: int, ty: int) -> bool:
        while tx >= sx and ty >= sy:
            if tx == ty:
                break
            elif tx > ty:
                if ty > sy:
                    tx %= ty
                else:
                    return (tx - sx) % ty == 0
            else:
                if tx > sx:
                    ty %= tx
                else:
                    return (ty - sy) % tx == 0
        return tx == sx and ty == sy


    def reachingPoints_another_TLE(self, sx, sy, tx, ty):
        while tx >= sx and ty >= sy:
            if sx == tx and sy == ty:
                return True
            if tx > ty:
                tx -= ty
            else:
                ty -= tx
        return False
    
    # RuntimeError: maximum recursion depth exceeded
    def reachingPoints_own(self, sx, sy, tx, ty):
        """
        :type sx: int
        :type sy: int
        :type tx: int
        :type ty: int
        :rtype: bool
        """
        mem = {}
        return self.helper(sx, sy, tx, ty, mem)
    
    def helper(self, sx, sy, tx, ty, mem):
        if sx == tx and sy == ty:
            mem[(sx, sy)] = True
            return True
        if sx > tx or sy > ty:
            mem[(sx, sy)] = False
            return False
        if (sx, sy) in mem:
            return mem[(sx, sy)]
        res = self.helper(sx, sx+sy, tx, ty, mem) or\
            self.helper(sx+sy, sy, tx, ty, mem)
        mem[(sx, sy)] = res
        return res
    
    def test(self):
        testCases = [
            [1, 1, 1000000000, 1],
            [1, 1, 3, 5], # True
            [1, 1, 2, 2], # False
            [1, 1, 1, 1], # True
            [6, 5, 11, 16], # True
        ]
        for sx, sy, tx, ty in testCases:
            print('sx: %s, sy: %s, tx: %s, ty: %s' % (sx, sy, tx, ty))
            result = self.reachingPoints(sx, sy, tx, ty)
            print('result: %s' % result)
            print('-='*30+'-')


if __name__ == '__main__':
    Solution().test()
