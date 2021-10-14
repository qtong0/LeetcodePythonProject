from typing import List


class Solution(object):
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        n1, n2 = len(nums1), len(nums2)
        low, high = 0, n1
        while low <= high:
            partition1 = (low+high)//2
            partition2 = (n1+n2+1)//2 - partition1

            # if partitioniX is 0 it means nothing is there on left side. Use -INF for maxLeftX
            # if partitionX is length of input then there is nothing on right side. Use +INF for minRightX
            maxLeft1 = float('-inf') if partition1 == 0 else nums1[partition1-1]
            minRight1 = float('inf') if partition1 == n1 else nums1[partition1]

            maxLeft2 = float('-inf') if partition2 == 0 else nums2[partition2-1]
            minRight2 = float('inf') if partition2 == n2 else nums2[partition2]

            if maxLeft1 <= minRight2 and maxLeft2 <= minRight1:
                # bingo!
                if (n1+n2) % 2 == 0:
                    return (max(maxLeft1, maxLeft2) + min(minRight1, minRight2)) / 2.0
                else:
                    return max(maxLeft1, maxLeft2)
            elif maxLeft1 > minRight2:
                # Far too right on nums1, Need to go left!
                high = partition1 - 1
            else:
                low = partition1 + 1

    def test(self):
        testCases = [
            [
                [1, 3],
                [2],
            ],
            [
                [1, 2],
                [3, 4],
            ],
        ]
        for nums1, nums2 in testCases:
            print('nums1: %s' % nums1)
            print('nums2: %s' % nums2)
            result = self.findMedianSortedArrays(nums1, nums2)
            print('result: %s' % result)
            print('-='*30+'-')


class Solution_lc_orig(object):
    def findMedianSortedArrays(self, nums1, nums2):
        m, n = len(nums1), len(nums2)
        if m > n:
            nums1, nums2, m, n = nums2, nums1, n, m
        imin, imax, half_len = 0, m, (m+n+1)//2
        while imin <= imax:
            i = (imin+imax)//2
            j = half_len - i
            if i < m and nums2[j-1] > nums1[i]:
                imin = i+1
            elif i > 0 and nums1[i-1] > nums2[j]:
                imax = i-1
            else:
                if i == 0:
                    max_of_left = nums2[j-1]
                elif j == 0:
                    max_of_left = nums1[i-1]
                else:
                    max_of_left = max(nums1[i-1], nums2[j-1])
                if (m+n)%2 == 1:
                    return max_of_left
                if i == m:
                    min_of_right = nums2[j]
                elif j == n:
                    min_of_right = nums1[i]
                else:
                    min_of_right = min(nums1[i], nums2[j])
                return (max_of_left + min_of_right)/2.0


if __name__ == '__main__':
    Solution().test()
