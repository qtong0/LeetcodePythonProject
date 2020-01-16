class Solution(object):
    def largestTimeFromDigits(self, A):
        """
        :type A: List[int]
        :rtype: str
        """
        for num in range(24*60-1, -1, -1):
            mins = num % 60
            hours = num // 60
            tmp = '%02d%02d' % (hours, mins)
            if sorted(''.join(str(num0) for num0 in A)) == sorted(tmp):
                return tmp[:2] + ':' + tmp[2:]
        return ''

    def test(self):
        testCases = [
            [1,2,3,4],
        ]
        for arr in testCases:
            res = self.largestTimeFromDigits(arr)
            print('res: %s' % res)
            print('-='*30+'-')


if __name__ == '__main__':
    Solution().test()
