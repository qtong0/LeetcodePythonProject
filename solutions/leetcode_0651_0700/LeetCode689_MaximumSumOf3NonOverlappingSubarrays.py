class Solution(object):
    def maxSumOfThreeSubarrays(self, nums, k: int):
        n = len(nums)
        sumVals = [0]*(n+1)
        posLeft = [0]*n
        posRight = [0]*n
        for i in range(n):
            sumVals[i+1] = sumVals[i] + nums[i]
        total = sumVals[k]-sumVals[0]
        # DP for starting index of the left max sum interval
        for i in range(k, n):
            if sumVals[i+1]-sumVals[i+1-k] > total:
                posLeft[i] = i+1-k
                total = sumVals[i+1]-sumVals[i+1-k]
            else:
                posLeft[i] = posLeft[i-1]
        # DP for starting index of the right max sum interval
        # caution: the condition is ">= tot" for right interval, and "> tot" for left interval
        posRight[n-k] = n-k
        total = sumVals[n]-sumVals[n-k]
        for i in range(n-k-1, -1, -1):
            if sumVals[i+k]-sumVals[i] >= total:
                posRight[i] = i
                total = sumVals[i+k]-sumVals[i]
            else:
                posRight[i] = posRight[i+1]
        # test all possible middle intervals
        maxSum = 0
        res = [0]*3
        for i in range(k, n-2*k+1):
            l = posLeft[i-1]
            r = posRight[i+k]
            total = (sumVals[l+k]-sumVals[l]) + (sumVals[i+k]-sumVals[i]) + (sumVals[r+k]-sumVals[r])
            if total > maxSum:
                maxSum = total
                res = [l, i, r]
        return res
    
    def test(self):
        testCases = [
            [
                [1,2,1,2,6,7,5,1],
                2,
            ],
            [
                [7,13,20,19,19,2,10,1,1,19],
                3,
            ],
        ]
        for nums, k in testCases:
            print('nums: %s' % nums)
            print('k: %s' % k)
            result = self.maxSumOfThreeSubarrays(nums, k)
            print('result: %s' % result)
            print('-='*30+'-')

if __name__ == '__main__':
    Solution().test()
