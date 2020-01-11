class Solution(object):
    def movesToStamp(self, stamp, target):
        """
        :type stamp: str
        :type target: str
        :rtype: List[int]
        """
        m, n = len(stamp), len(target)
        res = []
        count = 0
        while count < n:
            onePass = 0
            for i in range(n-m+1):
                t = target[i:i+m]
                matched = self.match(stamp, t)
                if matched:
                    for j in range(i, i+m):
                        target = target[:j] + '?' + target[j+1:]
                    res.append(i)
                onePass += matched
            if onePass == 0:
                break
            count += onePass
        if count < n:
            return []
        res = res[::-1]
        return res

    def match(self, s, t):
        count = 0
        for i in range(len(s)):
            if t[i] != '?': count += 1
            if t[i] != '?' and s[i] != t[i]:
                return 0
        return count

    def test(self):
        testCases = [
            ["abc", "ababc"],
        ]
        for stamp, target in testCases:
            res = self.movesToStamp(stamp, target)
            print('res: %s' % res)
            print('-='*30+'-')


if __name__ == '__main__':
    Solution().test()
