class Solution:
    def numDupDigitsAtMostN(self, n: int) -> int:
        n_str = str(n)
        n_digit = len(n_str)
        digits = list(map(int, n_str))
        res = n-1
        prefix = 0
        for i in range(1, n_digit):
            res -= self.n_digit_no_repeat(i)
        for i in range(n_digit):
            # when we fix the most significant digit, it
            # can't be zero
            start = 0 if i else 1
            for j in range(start, digits[i]):
                if self.has_repeated(prefix*10 + j):
                    continue
                if i != n_digit-1:
                    res -= self.permutation(10-i-1, n_digit-1-i)
                else:
                    # optmized from `result -= has_repeated(prefix*10+j)`
                    res -= 1
            prefix = prefix*10 + digits[i]
        return res + self.has_repeated(n)

    def has_repeated(self, n):
        return len(set(str(n))) != len(str(n))

    def permutation(self, n, k):
        prod = 1
        for i in range(k):
            prod *= (n-i)
        return prod

    # calculate number of non-repeated n-digit numbers
    # note: the n-digit number can't start with 0
    # i.e: n_digit_no_repeat(2) calculates the non-repeated
    #   numbers in range [10, 99] (inclusive)
    def n_digit_no_repeat(self, n):
        if n == 1:
            return 9
        else:
            return 9 * self.permutation(9, n-1)


    def test(self):
        test_cases = [
            20,
            100,
            1000,
            6358960,
        ]
        for n in test_cases:
            res = self.numDupDigitsAtMostN(n)
            print('res: %s' % res)
            print('-='*30 + '-')


if __name__ == '__main__':
    Solution().test()
