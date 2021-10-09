from typing import List


# A[i - 1] < A[i] && B[i - 1] < B[i].
# In this case, if we want to keep A and B increasing before the index i, can only have two choices.
# -> 1.1 don't swap at (i-1) and don't swap at i, we can get not_swap[i] = not_swap[i-1]
# -> 1.2 swap at (i-1) and swap at i, we can get swap[i] = swap[i-1]+1
# if swap at (i-1) and do not swap at i, we can not guarantee A and B increasing.
#
# A[i-1] < B[i] && B[i-1] < A[i]
# In this case, if we want to keep A and B increasing before the index i, can only have two choices.
# -> 2.1 swap at (i-1) and do not swap at i, we can get notswap[i] = Math.min(swap[i-1], notswap[i] )
# -> 2.2 do not swap at (i-1) and swap at i, we can get swap[i]=Math.min(notswap[i-1]+1, swap[i])
#
class Solution:
    # Time O(N)
    # Space O(N)
    def minSwap_space(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)
        swap, not_swap = [n]*n, [n]*n
        swap[0] = 1
        not_swap[0] = 0
        for i in range(1, n):

            # In this case, if we want to keep A and B increasing before the index i, can only have two choices.
            if nums1[i-1] < nums1[i] and nums2[i-1] < nums2[i]:
                # -> 1.1 don't swap at (i-1) and don't swap at i, we can get not_swap[i] = not_swap[i-1]
                swap[i] = swap[i-1]+1
                # -> 1.2 swap at (i-1) and swap at i, we can get swap[i] = swap[i-1]+1
                not_swap[i] = not_swap[i-1]

            # In this case, if we want to keep A and B increasing before the index i, can only have two choices.
            if nums1[i-1] < nums2[i] and nums2[i-1] < nums1[i]:
                # -> 2.1 swap at (i-1) and do not swap at i, we can get notswap[i] = Math.min(swap[i-1], notswap[i] )
                swap[i] = min(swap[i], not_swap[i-1] + 1)
                # -> 2.2 do not swap at (i-1) and swap at i, we can get swap[i]=Math.min(notswap[i-1]+1, swap[i])
                not_swap[i] = min(not_swap[i], swap[i-1])

        return min(swap[-1], not_swap[-1])


    # Best
    # Time O(N)
    # Space O(1)
    def minSwap(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)
        not_swap, swap = 0, 1
        for i in range(1, n):
            not_swap2 = swap2 = n
            if nums1[i-1] < nums1[i] and nums2[i-1] < nums2[i]:
                swap2 = swap+1
                not_swap2 = not_swap
            if nums1[i-1] < nums2[i] and nums2[i-1] < nums1[i]:
                swap2 = min(swap2, not_swap+1)
                not_swap2 = min(not_swap2, swap)
            swap, not_swap = swap2, not_swap2
        return min(swap, not_swap)


    # My solution DFS is TLE
    def minSwap_own_DFS_TLE(self, nums1: List[int], nums2: List[int]) -> int:
        arr1, arr2 = nums1, nums2
        self.res = float('inf')
        self.helper(arr1, arr2, 0, 0)
        return self.res
        
    def helper(self, arr1, arr2, i, cur):
        if i == len(arr1):
            self.res = min(self.res, cur)
            return
        if i == 0 or (arr1[i] > arr2[i-1] and arr2[i] > arr1[i-1]):
            arr1[i], arr2[i] = arr2[i], arr1[i]
            self.helper(arr1, arr2, i+1, cur+1)
            arr1[i], arr2[i] = arr2[i], arr1[i]
        if i == 0 or (arr1[i] > arr1[i-1] and arr2[i] > arr2[i-1]):
            self.helper(arr1, arr2, i+1, cur)
    
    def test(self):
        testCases = [
            [
                [1,3,5,4],
                [1,2,3,7],
            ],
            [
                [3,3,8,9,10],
                [1,7,4,6,8],
            ],
        ]
        for arr1, arr2 in testCases:
            print('arr1: %s' % arr1)
            print('arr2: %s' % arr2)
            result = self.minSwap(arr1, arr2)
            print('result: %s' % result)
            print('-='*30+'-')


if __name__ == '__main__':
    Solution().test()
