from typing import List


class Solution:
    def findBestValue(self, arr: List[int], target: int) -> int:
        l = 1
        r = max(arr)
        while l <= r:
            mid = (l + r)//2
            sum_val = self.getSum(arr, mid)
            if sum_val >= target:
                r = mid-1
            else:
                l = mid+1
        l_val = self.getSum(arr, l)
        r_val = self.getSum(arr, r)
        return r if abs(r_val - target) <= abs(l_val - target) else l

    def getSum(self, arr, changed):
        res = 0
        for num in arr:
            if num >= changed:
                res += changed
            else:
                res += num
        return res



    def test(self):
        test_cases = [
            [[4,9,3], 10],
            [[2,3,5], 10],
            [[60864,25176,27249,21296,20204], 56803],
        ]
        for arr, target in test_cases:
            res = self.findBestValue(arr, target)
            print('res: %s' % res)
            print('-='*30 + '-')


if __name__ == '__main__':
    Solution().test()
