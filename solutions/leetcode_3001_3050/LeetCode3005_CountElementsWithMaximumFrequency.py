from typing import List


class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        counter = {}
        max_freq = 0
        count = 0
        for num in nums:
            counter[num] = counter.get(num, 0) + 1
            if counter[num] > max_freq:
                max_freq = counter[num]
                count = 0
            if counter[num] == max_freq:
                count += 1
        return count * max_freq

    def test(self):
        test_cases = [
            [1,2,2,3,1,4],
            [1,2,3,4,5],
        ]
        for nums in test_cases:
            res = self.maxFrequencyElements(nums)
            print('res: %s' % res)


if __name__ == '__main__':
    Solution().test()
