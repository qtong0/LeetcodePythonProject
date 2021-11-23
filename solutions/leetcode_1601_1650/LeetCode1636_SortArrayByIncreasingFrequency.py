from typing import List


class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        hashmap = {}
        maxCount = 0
        for num in nums:
            hashmap[num] = hashmap.get(num, 0) + 1
            maxCount = max(maxCount, hashmap[num])
        counter = [[] for _ in range(maxCount+1)]
        for num, count in hashmap.items():
            counter[count].append(num)
        res = []
        for count in range(1, maxCount+1):
            if counter[count]:
                for num in sorted(counter[count], reverse=True):
                    res.extend([num] * count)
        return res


    def test(self):
        test_cases = [
            [1,1,2,2,2,3],
            [2,3,1,3,2],
            [-1,1,-6,4,5,-6,1,4,1],
        ]
        for nums in test_cases:
            res = self.frequencySort(nums)
            print('res: %s' % res)
            print('-='*30 + '-')


if __name__ == '__main__':
    Solution().test()
