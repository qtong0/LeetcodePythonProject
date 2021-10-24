from typing import List


class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        res = []
        hashmap = {}
        maxKey = 0
        m = len(nums)
        for i in range(m):
            for j, num in enumerate(nums[i]):
                hashmap[i+j] = hashmap.get(i+j, []) + [num]
                maxKey = max(maxKey, i+j)
        for i in range(maxKey+1):
            res += hashmap[i][::-1]
        return res


    def findDiagonalOrder_own_slow(self, nums: List[List[int]]) -> List[int]:
        res = []
        l = 0
        while True:
            curr = []
            for j in range(l+1):
                i = l-j
                if i < len(nums) and 0 <= j < len(nums[i]):
                    curr.append(nums[i][j])
            if curr:
                res += curr
                l += 1
            else:
                break
        return res


    def test(self):
        test_cases = [
            [[1,2,3],[4,5,6],[7,8,9]],
            [[1,2,3,4,5],[6,7],[8],[9,10,11],[12,13,14,15,16]],
            [[1,2,3],[4],[5,6,7],[8],[9,10,11]],
            [[1,2,3,4,5,6]],
        ]
        for nums in test_cases:
            res = self.findDiagonalOrder(nums)
            print('res: %s' % res)
            print('-='*30 + '-')


if __name__ == '__main__':
    Solution().test()
