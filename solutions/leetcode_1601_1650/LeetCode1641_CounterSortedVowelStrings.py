class Solution:
    # DP
    # curr[0] = prev[0]
    # curr[1] = prev[0] + prev[1]
    # ...
    # curr[i] = sum(prev[:i+1])
    #
    def countVowelStrings(self, n: int) -> int:
        prev = [1] * 5
        for _ in range(2, n+1):
            curr = [0]*5
            for i in range(5):
                curr[i] = sum(prev[:i+1])
            prev = curr
        return sum(prev)

    def test(self):
        test_cases = [
            1,
            2,
            33,
        ]
        for n in test_cases:
            res = self.countVowelStrings(n)
            print('res: %s' % res)
            print('-='*30 + '-')


if __name__ == '__main__':
    Solution().test()
