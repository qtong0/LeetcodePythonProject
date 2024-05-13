from typing import List


class Solution:
    def maximumSetSize(self, nums1: List[int], nums2: List[int]) -> int:
        i, j, n = 0, 0, len(nums1)
        s1, s2, s3 = set(), set(), set()
        for num in nums1:
            s1.add(num)
            s3.add(num)
        for num in nums2:
            s2.add(num)
            s3.add(num)
        common = len(s1) + len(s2) - len(s3)
        n1, n2 = len(s1), len(s2)
        res = min(n/2, n1-common)
        res += min(n/2, n2-common)
        res += common
        res = min(res, n)
        return int(res)

    def test(self):
        test_cases = [
            [[1,2,1,2], [1,1,1,1]],
            [[1,2,3,4,5,6], [2,3,2,3,2,3]],
            [[1,1,2,2,3,3], [4,4,5,5,6,6]],
        ]
        for nums1, nums2 in test_cases:
            res = self.maximumSetSize(nums1, nums2)
            print('res: %s' % res)
            print('-='*30 + '-')


if __name__ == '__main__':
    Solution().test()