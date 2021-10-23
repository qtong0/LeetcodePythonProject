from typing import List


class Solution:
    # Careful about difference == 0 scenario
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        hashmap = {}
        counter = {}
        res = 1
        for i, num in enumerate(arr):
            hashmap[num] = 1
            counter[num] = counter.get(num, 0) + 1
            if difference == 0:
                res = max(res, counter[num])
            else:
                if num - difference in hashmap:
                    hashmap[num] = max(hashmap[num], hashmap[num-difference]+1)
                res = max(res, hashmap[num])
        return res

    def test(self):
        test_cases = [
            [[1,2,3,4], 1],
            [[1,3,5,7], 1],
            [[1,5,7,8,5,3,4,2,1], -2],
            [[7,7,7,7,7,7,7], 0],
        ]
        for arr, difference in test_cases:
            res = self.longestSubsequence(arr, difference)
            print('res: %s' % res)
            print('-='*30 + '-')


if __name__ == '__main__':
    Solution().test()
