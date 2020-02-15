class Solution:
    def shipWithinDays(self, weights, D: int) -> int:
        maxVal, sumVal = 0, 0
        for w in weights:
            maxVal = max(maxVal, w)
            sumVal += w
        l, r = maxVal, sumVal
        while l < r:
            mid = (l+r)//2
            if self.canSplit(weights, D, mid):
                r = mid
            else:
                l = mid+1
        return r

    def canSplit(self, weights, d, maxVal):
        splits = 0
        sumVal = 0
        for w in weights:
            if sumVal + w > maxVal:
                splits += 1
                sumVal = w
                if splits >= d:
                    return False
            else:
                sumVal += w
        return True

    def test(self):
        testCases = [
            [[1,2,3,4,5,6,7,8,9,10], 5],
            [[3,2,2,4,1,4], 3],
            [[1,2,3,1,1], 4],
        ]
        for weights, D in testCases:
            res = self.shipWithinDays(weights, D)
            print('res: %s' % res)
            print('-='*30+'-')


if __name__ == '__main__':
    Solution().canSplit([1,2,3,4,5,6,7,8,9,10], 5, 12)

    Solution().test()
