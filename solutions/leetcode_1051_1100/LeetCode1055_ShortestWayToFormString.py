class Solution:
    def shortestWay(self, source: str, target: str) -> int:
        res = 1
        i, j = 0, 0
        while j < len(target):
            pos = source.find(target[j], i)
            if pos == -1:
                if i == 0:
                    return -1
                res += 1
                i = 0
            else:
                i = pos + 1
                j += 1
        return res

    def test(self):
        testCases = [
            ["abc", "abcbc"],
            ["abc", "acdbc"],
            ["xyz", "xzyxz"],
        ]
        for source, target in testCases:
            res = self.shortestWay(source, target)
            print('res: %s' % res)
            print('-='*30+'-')


class Solution_own_slow:
    def shortestWay_own_slow(self, source: str, target: str) -> int:
        res = 0
        i = 0
        while i < len(target):
            l = i
            while i+1 <= len(target) and self.isSubsequence(source, target[l:i+1]):
                i += 1
            res += 1
            if i == l:
                return -1
        return res

    def isSubsequence(self, source, target):
        i, j = 0, 0
        while i < len(source) and j < len(target):
            if source[i] == target[j]:
                i += 1
                j += 1
            else:
                i += 1
                if i == len(source):
                    return False
        return j == len(target)



if __name__ == '__main__':
    Solution().test()
