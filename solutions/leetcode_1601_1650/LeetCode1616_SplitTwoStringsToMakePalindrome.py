class Solution:
    # Two pointers from 0, n-1 to middle and then check if middle part is palindrome
    def checkPalindromeFormation(self, a: str, b: str) -> bool:
        if self.isPalidrome(a) or self.isPalidrome(b):
            return True
        n = len(a)
        i, j = 0, n-1
        while i < j and a[i] == b[j]:
            i += 1
            j -= 1
        if i == j or i-1 == j:
            return True
        if self.isPalidrome(a[i:j+1]) or self.isPalidrome(b[i:j+1]):
            return True
        i, j = 0, n-1
        while i < j and b[i] == a[j]:
            i += 1
            j -= 1
        if i == j or i-1 == j:
            return True
        if self.isPalidrome(a[i:j+1]) or self.isPalidrome(b[i:j+1]):
            return True
        return False

    def isPalidrome(self, s):
        if not s:
            return True
        i, j = 0, len(s)-1
        while i < j:
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1
        return True


    # Brute force, TLE
    def checkPalindromeFormation_bruteforce_TLE(self, a: str, b: str) -> bool:
        n = len(a)
        for i in range(n+1):
            apre, asuf = a[:i], a[i:]
            bpre, bsuf = b[:i], b[i:]
            if self.isPalidrome(apre + bsuf) or self.isPalidrome(bpre + asuf):
                return True
        return False


    def test(self):
        test_cases = [
            ['x', 'y'],
            ["abdef", "fecab"],
            ["ulacfd", "jizalu"],
            ["xbdef", "xecab"],
            [
                "pvhmupgqeltozftlmfjjde",
                "yjgpzbezspnnpszebzmhvp",
            ],
        ]
        for a, b in test_cases:
            res = self.checkPalindromeFormation(a, b)
            print('res: %s' % res)
            print('-='*30 + '-')


if __name__ == '__main__':
    Solution().test()
