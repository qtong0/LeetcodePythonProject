from typing import List


class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        hashset = set(arr2)
        hashmap = {}
        res1 = []
        res2 = []
        for num in arr1:
            if num in hashset:
                hashmap[num] = hashmap.get(num, 0) + 1
            else:
                res2.append(num)
        for num in arr2:
            res1 += [num] * hashmap[num]
        return res1 + sorted(res2)


    def test(self):
        test_cases = [
            [[2,3,1,3,2,4,6,7,9,2,19], [2,1,4,3,9,6]],
            [[28,6,22,8,44,17], [22,28,8,6]],
        ]
        for arr1, arr2 in test_cases:
            res = self.relativeSortArray(arr1, arr2)
            print('res: %s' % res)
            print('-='*30 + '-')


if __name__ == '__main__':
    Solution().test()
