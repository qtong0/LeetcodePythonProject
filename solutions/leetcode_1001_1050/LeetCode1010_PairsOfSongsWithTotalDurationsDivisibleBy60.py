from typing import List


class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        hashmap = {}
        res = 0
        for num in time:
            num = num % 60
            res += hashmap.get((60-num) % 60, 0)
            hashmap[num] = hashmap.get(num, 0) + 1
        return res

    def test(self):
        test_cases = [
            [30,20,150,100,40],
            [60,60,60],
        ]
        for time in test_cases:
            res = self.numPairsDivisibleBy60(time)
            print('res: %s' % res)
            print('-='*30 + '-')


if __name__ == '__main__':
    Solution().test()
