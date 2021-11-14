class Solution:
    def asteroidCollision(self, asteroids):
        res = []
        for a in asteroids:
            if a > 0:
                res.append(a)
            else:
                while res and 0 < res[-1] < -a:
                    res.pop()
                if res and res[-1] == -a:
                    res.pop()
                elif not res or res[-1] < 0:
                    res.append(a)
        return res

    def test(self):
        testCases = [
            [5, 10, -5],
            [8, -8],
            [10, 2, -5],
            [-2, -1, 1, 2],
        ]
        for asteroids in testCases:
            print('asteroids: %s' % asteroids)
            result = self.asteroidCollision(asteroids)
            print('result: %s' % result)
            print('-=' * 30 + '-')


if __name__ == '__main__':
    Solution().test()
