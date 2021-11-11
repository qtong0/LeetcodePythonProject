class Solution:

    # If n is even
    # we can choose x = 1
    # The opponent will get n-1, odd
    # Like odd case below, opponent will lose
    #
    # If n is odd
    # if n == 1, lose directly
    # we have to chose and odd x
    # the opponent will get n-x whic is even
    # like even case above, opponent will win
    #
    def divisorGame(self, n: int) -> bool:
        return n % 2 == 0


    def divisorGame_own_slow_TLE(self, n: int) -> bool:
        for x in range(1, n//2+1):
            if n % x == 0:
                if not self.divisorGame(n-x):
                    return True
        return False

    def test(self):
        test_cases = [
            2,
            3,
            100,
        ]
        for n in test_cases:
            res = self.divisorGame(n)
            print('res: %s' % res)
            print('-='*30 + '-')


if __name__ == '__main__':
    Solution().test()
