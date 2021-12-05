class Solution(object):
    # traverse each digit of n, if n=3401512
    #  for m=100, split n into a=34015 and b=12
    #  if a%10==1, #1=a/10*m+(b+1);
    #  if a%10==0, #2=a/10*m;
    #  if a%10>1; #3=a/10*m+m;
    #  In general, #4=(a+8)/10*m+(a % 10 == 1)*(b + 1).
    #
    # For general expression above:
    #  if a%10>1, then (a+8)/10=a/10+1, #4=#3
    #  if a%10==0, (a+8)/10=a/10, (a % 10 == 1)=false, #4=#2
    #  if a%10==1, (a+8)/10=a/10, (a % 10 == 1)=true, #4=#1
    #
    def countDigitOne(self, n: int) -> int:
        ones = 0
        m = 1
        while m <= n:
            a = n // m
            b = n % m
            # in short:
            # ones += (a + 8) // 10 * m
            # ones += b+1
            if a % 10 == 1:
                ones += a // 10 * m + (b+1)
            elif a % 10 == 0:
                ones += a // 10 * m
            else:
                ones += a // 10 * m + m
            m *= 10
        return ones

    def test(self):
        test_cases = [
            13,
            0,
        ]
        for n in test_cases:
            res = self.countDigitOne(n)
            print('res: %s' % res)
            print('-='*30 + '-')


if __name__ == '__main__':
    Solution().test()
