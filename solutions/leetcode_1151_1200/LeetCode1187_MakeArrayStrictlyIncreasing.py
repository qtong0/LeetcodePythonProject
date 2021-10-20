from typing import List
import bisect


class Solution:
    def makeArrayIncreasing(self, arr1: List[int], arr2: List[int]) -> int:
        arr2.sort()
        hashmap = {-1: 0}
        for num in arr1:
            tmp_map = {}
            for key in hashmap:
                if num > key:
                    tmp_map[num] = min(tmp_map.get(num, float('inf')), hashmap[key])
                loc = bisect.bisect_right(arr2, key)
                if loc < len(arr2):
                    tmp_map[arr2[loc]] = min(tmp_map.get(arr2[loc], float('inf')), hashmap[key]+1)
            hashmap = tmp_map
        if hashmap:
            return min(hashmap.values())
        return -1


    def test(self):
        test_cases = [
            [[1,5,3,6,7], [1,3,2,4]],
            [[1,5,3,6,7], [4,3,1]],
            [[1,5,3,6,7], [1,6,3,3]],
        ]
        for arr1, arr2 in test_cases:
            res = self.makeArrayIncreasing(arr1, arr2)
            print('res: %s' % res)
            print('-='*30 + '-')


if __name__ == '__main__':
    Solution().test()
