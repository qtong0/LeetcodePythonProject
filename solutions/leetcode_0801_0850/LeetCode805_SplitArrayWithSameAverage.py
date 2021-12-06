from functools import lru_cache
from typing import List


class Solution(object):
    # bitSet
    def splitArraySameAverage(self, nums: List[int]) -> bool:
        N, S, P = len(nums), sum(nums), [1]
        for a in nums:
            P[1:] = [(p << a) | q for p, q in zip(P, P[1:] + [0])]
        return any(S * n % N == 0 and P[n] & (1 << (S * n // N))
                   for n in range(1, N))



    # DFS + Memorization
    # TLE - but I think it's fine
    def splitArraySameAverage_DFS_Memorization(self, nums: List[int]) -> bool:
        n, sum_val = len(nums), sum(nums)
        @lru_cache()
        def find(target, k, i):
            if k == 0:
                return target == 0
            if target < 0 or k + i > n:
                return False
            return find(target - nums[i], k-1, i+1) or find(target, k, i+1)
        for k in range(1, n//2 + 1):
            if sum_val * k % n == 0:
                if find(sum_val*k//n, k, 0):
                    return True
        return False



    # Own - TLE now
    def splitArraySameAverage_own(self, A: List[int]) -> bool:
        arr = A
        if len(arr) == 1: return False
        sumA = 0
        for num in arr:
            sumA += num
        arr.sort()
        for lenOfB in range(1, len(arr)//2+1):
            if (sumA*lenOfB) % len(arr) == 0:
                if self.check(arr, (sumA*lenOfB)/len(arr), lenOfB, 0):
                    return True
        return False

    def check(self, arr, leftSum, leftNum, startIdx):
        if leftNum == 0:
            return leftSum == 0
        if arr[startIdx] > leftSum/leftNum:
            return False
        for i in range(startIdx, len(arr)-leftNum+1):
            if i > startIdx and arr[i] == arr[i-1]:
                continue
            if self.check(arr, leftSum-arr[i], leftNum-1, i+1):
                return True
        return False



    def test(self):
        testCases = [
            [3,1],
            [1,2,3,4,5,6,7,8],
            [11,1,15,2,14,16,8,9,4],
            [4, 4, 4, 4, 4, 4, 5, 4, 4, 4, 4, 4, 4, 5],
        ]
        for arr in testCases:
            print('arr: %s' % arr)
            result = self.splitArraySameAverage(arr)
            print('result: %s' % result)
            print('-='*30+'-')



if __name__ == '__main__':
    Solution().test()
