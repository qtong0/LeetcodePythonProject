from typing import List


class Solution:
    # O(N) two pointers
    def maxDistance(self, nums1: List[int], nums2: List[int]) -> int:
        res = 0
        i, j = 0, 0
        m = len(nums1)
        n = len(nums2)
        while i < m and j < n:
            if nums1[i] > nums2[j]:
                i += 1
            else:
                res = max(res, j-i)
                j += 1
        return res


    # Own N*(Log(N)) Binary Search
    def maxDistance_own_binary_search(self, nums1: List[int], nums2: List[int]) -> int:
        m = len(nums1)
        n = len(nums2)
        res = 0
        for j in range(n-1, -1, -1):
            l, r = 0, min(j+1, m)
            while l < r:
                mid = (l+r)//2
                if nums1[mid] <= nums2[j]:
                    r = mid
                else:
                    l = mid+1
            if l < len(nums1) and nums1[l] <= nums2[j]:
                res = max(res, j-l)
        return res


    def test(self):
        test_cases = [
            [[55,30,5,4,2], [100,20,10,10,5]],
            [[2,2,2], [10,10,1]],
            [[30,29,19,5], [25,25,25,25,25]],
            [[5,4], [3,2]],
        ]
        for nums1, nums2 in test_cases:
            res = self.maxDistance(nums1, nums2)
            print('res: %s' % res)
            print('-='*30 + '-')


if __name__ == '__main__':
    Solution().test()
