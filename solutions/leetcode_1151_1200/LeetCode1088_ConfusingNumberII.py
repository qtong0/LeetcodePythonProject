import datetime


class Solution:
    def confusingNumberII(self, N: int) -> int:
        def generateNum(candidates, num, length, result, cur):
            if length == 0:
                if int(cur) <= num:
                    result.append(int(cur))
                return
            for element in candidates:
                generateNum(candidates, num, length-1, result, cur+element)

        def checkNum(num):
            newNum = ''.join(reversed(str(num)))
            newNum = newNum.replace('6', '-').replace('9', '6').replace('-', '0')
            return int(newNum) != num

        collection = []
        generateNum(['0', '1', '6', '8', '9'], N, len(str(N)), collection, '')
        return sum(checkNum(element) for element in collection)



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
            1000000000,
        ]
        now = datetime.datetime.now()
        for n in testCases:
            res = self.confusingNumberII_own_TLE(n)
            print('res: %s' % res)
            print('-='*30+'-')
        print('time taken: %s' % (datetime.datetime.now() - now))

        now = datetime.datetime.now()
        for n in testCases:
            res = self.confusingNumberII(n)
            print('res: %s' % res)
            print('-='*30+'-')
        print('time taken: %s' % (datetime.datetime.now() - now))


if __name__ == '__main__':
    Solution().test()
