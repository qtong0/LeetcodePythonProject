class Solution(object):
    def minFlipsMonoIncr(self, S):
        """
        :type S: str
        :rtype: int
        """
        flip0, flip1 = 0, 0
        for i, c in enumerate(S):
            if c == '0':
                # keep 0
                # Do nothing
                # flip one
                flip1 = min(flip0, flip1)+1
            else:
                # keep 1
                flip1 = min(flip0, flip1)
                # flip 0
                flip0 = flip0+1
        return min(flip0, flip1)

    def test(self):
        testCases = [
            '00110',
            '010110',
            '00011000',
        ]
        for s in testCases:
            res = self.minFlipsMonoIncr(s)
            print('res: %s' % res)
            print('-='*30+'-')


if __name__ == '__main__':
    Solution().test()
