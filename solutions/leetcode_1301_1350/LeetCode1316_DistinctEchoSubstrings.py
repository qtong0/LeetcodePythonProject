class Solution:
    # Hash solution
    # O(N^2)
    #
    def distinctEchoSubstrings(self, text: str) -> int:
        BASE, MOD = 29, 10**9 + 7
        hashset = set()
        n = len(text)
        hash = [0]*(n+1)
        pow = [0]*(n+1)
        pow[0] = 1
        for i in range(1, n+1):
            hash[i] = (hash[i-1] * BASE + ord(text[i-1])) % MOD
            pow[i] = pow[i-1] * BASE % MOD
        for i in range(n):
            length = 2
            while i + length <= n:
                mid = i + length // 2
                hash1 = self.getHash(i, mid, hash, pow)
                hash2 = self.getHash(mid, i+length, hash, pow)
                if hash1 == hash2:
                    hashset.add(hash1)
                length += 2
        return len(hashset)

    def getHash(self, l, r, hash, pow):
        BASE, MOD = 29, 10**9 + 7
        return (hash[r] - hash[l] * pow[r-l] % MOD + MOD) % MOD


    # Own solution
    # O(N^3) - Not TLE
    #
    def distinctEchoSubstrings_own_slow(self, text: str) -> int:
        n = len(text)
        res = set()
        for i in range(n-2):
            for j in range(i+1, n):
                substr = text[i:j]
                if i + len(substr)*2 <= n and text[i:i+len(substr)*2] == substr + substr:
                    res.add(substr+substr)
        return len(res)


    def test(self):
        test_cases = [
            'abcabcabc',
            'leetcodeleetcode',
        ]
        for text in test_cases:
            res1 = self.distinctEchoSubstrings(text)
            res2 = self.distinctEchoSubstrings_own_slow(text)
            print('res1: %s' % res1)
            print('res2: %s' % res2)
            print('-='*30 + '-')


if __name__ == '__main__':
    Solution().test()
