class Solution(object):
    def threeEqualParts(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        IMP = [-1, -1]

        s = sum(A)
        if s%3: return IMP
        t = s // 3
        if t == 0:
            return [0, len(A)-1]

        breaks = []
        su = 0
        for i, val in enumerate(A):
            if val:
                su += val
                if su in {1, t+1, 2*t+1}:
                    breaks.append(i)
                if su in {t, 2*t, 3*t}:
                    breaks.append(i)
        i1, j1, i2, j2, i3, j3 = breaks

        if not(A[i1:j1+1] == A[i2:j2+1] == A[i3:j3+1]):
            return [-1, -1]

        x = i2-j1-1
        y = i3-j2-1
        z = len(A)-j3-1

        if x < z or y < z: return IMP
        j1 += z
        j2 += z
        return [j1, j2+1]

    def test(self):
        testCases = [
            [1,0,1,1,0],
            # [0,1,0,1,1],
            # [1,0,1,0,1],
            # [1,1,0,1,1],
        ]
        for arr in testCases:
            res = self.threeEqualParts(arr)
            print('res: %s' % res)
            print('-='*30+'-')


if __name__ == '__main__':
    Solution().test()
