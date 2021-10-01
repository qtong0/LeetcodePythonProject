class Solution:
    # There are only two possibilities to form a non-adjacent row:
    #       3 colors combination (use all three colors, e.g., RYG)
    #       and 2 color combination (use only two of three colors, e.g., RYR).
    #
    # We add the new row one by one. Apart from its inner adjacent relation,
    #      every new added row only relies on the previous one row (new added row is only adjacent with the row above it).
    #
    # Every color combination follows the same pattern indicated below.
    #       3-color combination can generate two 3-color combination,
    #       and two 2-color combination for the next round. 2-color combination can generate two 3-color combination,
    #       and three 2-color combination for the next round.

    def numOfWays(self, n: int) -> int:
        MOD = 10**9 + 7
        color3 = 6
        color2 = 6
        for _ in range(2, n+1):
            tempColor3 = color3
            color3 = (color2 * 2 + color3 * 2) % MOD
            color2 = (color2 * 3 + tempColor3 * 2) % MOD
        return (color2 + color3) % MOD

    def test(self):
        test_cases = [
            1,
            2,
            3,
            7,
            5000,
        ]
        for n in test_cases:
            res = self.numOfWays(n)
            print('res: %s' % res)
            print('-='*30 + '-')


if __name__ == '__main__':
    Solution().test()
