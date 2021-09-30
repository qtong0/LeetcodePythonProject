class Solution(object):
    def checkRecord(self, n):
        mod = 10 ** 9 + 7
        a = [0] * n
        p = [0] * n
        l = [0] * n

        if n == 1:
            return 3
        if n == 2:
            return 8

        a[0] = 1
        a[1] = 2
        a[2] = 4
        p[0] = 1
        l[0] = 1
        l[1] = 3

        for i in range(1, n):
            p[i] = (a[i - 1] + p[i - 1] + l[i - 1]) % mod
            if i > 1:
                l[i] = (a[i - 1] + p[i - 1] + a[i - 2] + p[i - 2]) % mod
            if i > 2:
                # A(n) = noAP(n - 1) + noAL(n - 1), n ≥ 2.
                # noAP(n) = noAP(n - 1) + noAL(n - 1), n ≥ 2.
                # noAL(n) = noAP(n - 1) + noAP(n - 2), n ≥ 3.
                a[i] = (a[i - 1] + a[i - 2] + a[i - 3]) % mod

        return (a[-1] + p[-1] + l[-1]) % mod

    def test(self):
        testCases = [
            2,
            3,
            4,
        ]
        for n in testCases:
            print('n: %s' % n)
            result = self.checkRecord(n)
            print('result: %s' % result)
            print('-=' * 30 + '-')


if __name__ == '__main__':
    Solution().test()
