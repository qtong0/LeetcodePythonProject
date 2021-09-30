import datetime


class Solution:
    def confusingNumberII(self, N: int) -> int:
        self.hashmap = {
            0: 0,
            1: 1,
            6: 9,
            8: 8,
            9: 6,
        }
        self.res = 0
        self.helper(N, 0)
        return self.res

    def helper(self, n, cur):
        if self.isConfusingNum(cur):
            self.res += 1
        for num in self.hashmap.keys():
            if cur*10+num <= n and cur*10+num != 0:
                self.helper(n, cur*10+num)

    def isConfusingNum(self, n):
        res = 0
        num = n
        while n:
            digit = n % 10
            res = res*10 + self.hashmap.get(digit)
            n = (n-digit)//10
        return res != num



    def confusingNumberII_own_TLE(self, N: int) -> int:
        num = 1
        digit = 0
        self.singles = ['0', '1', '8', '6', '9']
        self.reverses = {
            '0': '0',
            '1': '1',
            '8': '8',
            '6': '9',
            '9': '6',
        }
        res = set()
        while num <= N:
            num = 10**digit
            candidates = []
            self.getNums(digit, candidates, '')
            if num > N:
                res = res | set([c for c in candidates if c <= N])
            else:
                res = res | set(candidates)
            digit += 1
        return len(res)

    def getNums(self, digit, candidates, curr):
        if len(curr) == digit:
            if curr != self.getReverse(curr) and curr[0] != '0':
                candidates.append(int(curr))
            return
        if len(curr) > digit:
            return
        for s in self.singles:
            self.getNums(digit, candidates, curr+s)

    def getReverse(self, s):
        res = ''
        for c in s[::-1]:
            res += self.reverses[c]
        return res

    def test(self):
        testCases = [
            20, # 6
            100, # 19
            # 1000000000,
        ]
        # now = datetime.datetime.now()
        # for n in testCases:
        #     res = self.confusingNumberII_own_TLE(n)
        #     print('res: %s' % res)
        #     print('-='*30+'-')
        # print('time taken: %s' % (datetime.datetime.now() - now))

        now = datetime.datetime.now()
        for n in testCases:
            res = self.confusingNumberII(n)
            print('res: %s' % res)
            print('-='*30+'-')
        print('time taken: %s' % (datetime.datetime.now() - now))


if __name__ == '__main__':
    Solution().test()
