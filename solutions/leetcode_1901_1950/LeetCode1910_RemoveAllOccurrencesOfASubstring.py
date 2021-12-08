class Solution:

    # KMP Solution
    def removeOccurrences_kmp(self, s: str, part: str) -> str:
        kmp = [0]*(len(part) + 1)
        idx = [0]*len(s)
        i, j = 1, 0
        while i < len(part):
            if part[i] == part[j]:
                kmp[i] = j
                i += 1
                j += 1
            else:
                if j == 0:
                    i += 1
                j = kmp[j]
        d = 0
        i, j = 0, 0
        arr = list(s)
        while i < len(arr):
            arr[i-d] = arr[i]
            if arr[i-d] == part[j]:
                idx[i-d] = j+1
                j += 1
                if j == len(part):
                    d += len(part)
                    j = idx[i-d] if i >= d else 0
            else:
                if j != 0:
                    j = kmp[j]
                    i -= 1
            i += 1
        return ''.join(arr[:len(arr) - d])

    # Stack solution
    # The best solution is KMP - but I don't think this might be good enough
    def removeOccurrences(self, s: str, part: str) -> str:
        res = list(s)
        part = list(part)
        j = 0
        n, m = len(s), len(part)
        for i in range(n):
            res[j] = s[i]
            j += 1
            if j >= m and res[j-m:j] == part:
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
            res2 = self.removeOccurrences_kmp(s, part)
            print('res: %s' % res)
            print('res2: %s' % res2)
            print('-='*30 + '-')


if __name__ == '__main__':
    Solution().test()
