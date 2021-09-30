class Solution:
    # O(N)
    def concatenatedBinary(self, n: int) -> int:
        mod = 10**9+7
        res = 0
        length = 0
        for i in range(1, n+1):
            if i & (i - 1) == 0:
                length += 1
            # With bitwise operation, we can check whether a number is the power of 2
            # If (x & (x-1)) == 0, then x is the power of 2.
            res = ((res << length) + i) % mod
        return res % mod

    # This is slower, calculating digits every time
    # Time O(N*Log(N))
    def concatenatedBinary_slower_NLogN(self, n: int) -> int:
        mod = 10**9+7
        prev = 1
        for num in range(2, n+1):
            digits = self.digits(num)
            prev = (prev << digits) + num
        return prev % mod

    def digits(self, n):
        res = 0
        while n > 0:
            n = n >> 1
            res += 1
        return res

    def test(self):
        test_cases = [
            1,
            3,
            12,
        ]
        for n in test_cases:
            res = self.concatenatedBinary(n)
            print('res: %s' % res)
            print('-='*30+'-')


if __name__ == '__main__':
    Solution().test()
