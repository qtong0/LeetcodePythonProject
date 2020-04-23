class Solution(object):
    def myPow_rec(self, x, n):
        if n == 0:
            return 1
        if n < 0:
            n = -n
            x = 1/x
        if n%2==0:
            return self.myPow(x*x, n/2)
        else:
            return x*self.myPow(x*x, n/2)


    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        if n < 0:
            n = -n
            x = 1/x
        res = 1
        curProd = x
        i = n
        while i > 0:
            if i % 2 == 1:
                res = res * curProd
            curProd = curProd * curProd
            i //= 2
        return res


if __name__ == '__main__':
    Solution().test()
