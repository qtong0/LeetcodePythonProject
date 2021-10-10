from typing import List


class Solution:
    def minSumOfLengths(self, arr: List[int], target: int) -> int:
        sum_val = 0
        hashmap = {0: -1}
        for i, num in enumerate(arr):
            sum_val += num
            hashmap[sum_val] = i
        n = len(arr)

        sum_val = 0
        left = float('inf')

        res = float('inf')
        for i, num in enumerate(arr):
            sum_val += num
            if sum_val - target in hashmap and hashmap[sum_val - target] < i:
                left = min(left, i - hashmap[sum_val - target])
            if sum_val + target in hashmap and left != float('inf'):
                res = min(res, hashmap[sum_val+target] - i + left)

        return res if res != float('inf') else -1

    def test(self):
        test_cases = [
            [[3,2,2,4,3], 3],
            [[7,3,4,7], 7],
            [[4,3,2,6,2,3,4], 6],
            [[5,5,4,4,5], 3],
            [[3,1,1,1,5,1,2,1], 3],
            [[1,6,1], 7],
            [[1,2,2,3,2,6,7,2,1,4,8], 5],
            [[11], 11],
        ]
        for arr, target in test_cases:
            res = self.minSumOfLengths(arr, target)
            print('res: %s' % res)
            print('-='*30 + '-')


if __name__ == '__main__':
    Solution().test()
