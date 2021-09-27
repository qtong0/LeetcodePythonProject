'''
Created on Mar 7, 2018

@author: tongq
'''


class Solution:
    def asteroidCollision(self, asteroids):
        res = []
        for asteroid in asteroids:
            while len(res) and asteroid < 0 and res[-1] > 0:
                if res[-1] == -asteroid:
                    res.pop()
                    break
                elif res[-1] < -asteroid:
                    res.pop()
                    continue
                elif res[-1] > -asteroid:
                    break
            else:
                res.append(asteroid)
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
