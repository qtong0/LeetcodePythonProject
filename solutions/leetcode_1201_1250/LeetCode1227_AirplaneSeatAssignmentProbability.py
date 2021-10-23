class Solution:
    # f(n) = 1/n * (f(1) + f(2) + ... + f(n-1))
    #
    # n*f(n) = f(1) + f(2) + ... + f(n-1)
    # (n-1)*f(n-1) = f(1) + f(2) + ... + f(n-2)
    # subtract the above two
    # f(n) = f(n-1), where n > 2
    #
    def nthPersonGetsNthSeat(self, n: int) -> float:
        if n == 1:
            return n
        else:
            return 0.5

    def test(self):
        test_cases = [
            1,
            2,
            3,
            4,
        ]
        for n in test_cases:
            res = self.nthPersonGetsNthSeat(n)
            print('res: %s' % res)
            print('-='*30 + '-')


if __name__ == '__main__':
    Solution().test()
