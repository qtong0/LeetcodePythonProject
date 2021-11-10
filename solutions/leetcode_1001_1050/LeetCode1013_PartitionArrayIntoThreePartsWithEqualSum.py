from typing import List


class Solution:
    def canThreePartsEqualSum(self, arr: List[int]) -> bool:
        sum_val = sum(arr)
        if sum_val % 3 != 0:
            return False
        target = sum_val // 3
        sum_val = 0
        found = 0
        for num in arr:
            sum_val += num
            if sum_val == target:
                sum_val = 0
                found += 1
        return found >= 3


    def test(self):
        test_cases = [
            [18,12,-18,18,-19,-1,10,10],
        ]
        for arr in test_cases:
            res = self.canThreePartsEqualSum(arr)
            print('res: %s' % res)
            print('-='*30 + '-')


if __name__ == '__main__':
    Solution().test()
