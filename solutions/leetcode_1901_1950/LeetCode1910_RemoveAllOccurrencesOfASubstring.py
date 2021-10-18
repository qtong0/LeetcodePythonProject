class Solution:
    # Stack solution
    # The best solution is KMP - but I don't think this might be good enough
    def removeOccurrences(self, s: str, part: str) -> str:
        res = list(s)
        j = 0
        n, m = len(s), len(part)
        for i in range(n):
            res[j] = s[i]
            j += 1
            if j >= m and ''.join(res[j-m:j]) == part:
                j -= m
        return ''.join(res[:j])

    # O(m*n) - somehow it's still not TLE in LC
    def removeOccurrences_own_slow(self, s: str, part: str) -> str:
        res = s
        while part in res:
            for i in range(len(res)-len(part)+1):
                if res[i:i+len(part)] == part:
                    res = res[:i] + res[i+len(part):]
                    break
        return res

    def test(self):
        test_cases = [
            ["daabcbaabcbc", "abc"],
            ["axxxxyyyyb", "xy"],
        ]
        for s, part in test_cases:
            res = self.removeOccurrences(s, part)
            print('res: %s' % res)
            print('-='*30 + '-')


if __name__ == '__main__':
    Solution().test()
