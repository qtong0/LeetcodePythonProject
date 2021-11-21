from typing import List


class Solution:
    def wateringPlants(self, plants: List[int], capacity: int) -> int:
        n = len(plants)
        c = capacity
        res = 0
        for i, p in enumerate(plants):
            if p > c:
                c = capacity - p
                res += i
                res += i + 1
            else:
                c -= p
                res += 1
            if i == n-1:
                return res
        return res


    def test(self):
        test_cases = [
            [[2,2,3,3], 5],
            [[1,1,1,4,2,3], 4],
            [[7,7,7,7,7,7,7], 8],
        ]
        for plants, capacity in test_cases:
            res = self.wateringPlants(plants, capacity)
            print('res: %s' % res)
            print('-='*30 + '-')


if __name__ == '__main__':
    Solution().test()
