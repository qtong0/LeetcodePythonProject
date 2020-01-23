class Solution:
    def leastOpsExpressTarget(self, x: int, target: int) -> int:
        if target == 0 or x == target:
            return 0
        if target < x:
            return min(2*target-1, 2*(x-target))
        nextVal = x*x
        current = x
        count = 0
        while abs(target-nextVal) < abs(target-current):
            current *= x
            nextVal *= x
            count += 1
        if current > target:
            count = 1 + min(count + self.leastOpsExpressTarget(x, current-target), \
                        count + self.leastOpsExpressTarget(x, target-current/x) -1)
        elif current < target:
            count += self.leastOpsExpressTarget(x, target-current) + 1
        return int(count)

    def test(self):
        testCases = [
            [3, 19],
            [5, 501],
        ]
        for x, target in testCases:
            res = self.leastOpsExpressTarget(x, target)
            print('res: %s' % res)
            print('-='*30+'-')


if __name__ == '__main__':
    Solution().test()
