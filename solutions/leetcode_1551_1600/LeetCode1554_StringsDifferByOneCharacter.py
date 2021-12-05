from typing import List


class Solution:
    # We can use string hashing to bring down the time complexity to O(N*M).
    # Instead of storing all the wildcard words, we store their hash value.
    # And a wildcard word's hash value can be calculated in O(1) time.
    # Specifically, we substract the wildcard position hash value from the word's original hash value.
    #
    # Example:
    # - hash('ba') = 2*26^1 + 1*26^0 = 53
    # - hash('*a') = 53 - 2*26^1 = 1
    # - hash('b*') = 53 - 1*26^0 = 52
    # Note that we may face hash collision problem.
    # Here we use a large prime number (10*11 + 7) to avoid it, but there's still a chance that the algorithm fails.
    # If we add checks for hash collision, the worst-case complexity will go back to O(N*M^2).
    #
    # O(M*N)
    #
    def differByOne(self, words: List[str]) -> bool:
        m, n = len(words), len(words[0])
        hashes = [0] * m
        MOD = 10**11 + 7

        for i in range(m):
            for j in range(n):
                hashes[i] = (26*hashes[i] + (ord(words[i][j]) - ord('a'))) % MOD

        base = 1
        for j in range(n-1, -1, -1):
            seen = set()
            for i in range(m):
                new_h = (hashes[i] - base * (ord(words[i][j]) - ord('a'))) % MOD
                if new_h in seen:
                    return True
                seen.add(new_h)
            base = 26 * base % MOD
        return False



    # O(N^2), Brute Force, TLE
    def differByOne_BruteForce_TLE(self, words: List[str]) -> bool:
        n = len(words)
        for i in range(n):
            for j in range(i):
                w1 = words[i]
                w2 = words[j]
                if self.helper(w1, w2):
                    return True
        return False

    def helper(self, w1, w2):
        hasDiff = False
        for c1, c2 in zip(w1, w2):
            if c1 != c2:
                if hasDiff:
                    return False
                hasDiff = True
        return hasDiff


    def test(self):
        test_cases = [
            ["abcd","acbd", "aacd"],
            ["ab","cd","yz"],
            ["abcd","cccc","abyd","abab"],
        ]
        for words in test_cases:
            res = self.differByOne(words)
            print('res: %s' % res)
            print('-='*30 + '-')


if __name__ == '__main__':
    Solution().test()
