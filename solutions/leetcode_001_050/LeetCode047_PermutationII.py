'''
Created on Jan 19, 2017

@author: MT
'''

class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if nums is None:
            return []
        if nums == []:
            return [[]]
        curr = []
        result = []
        self.dfs(sorted(nums), curr, result)
        return result
    
    def dfs(self, nums, curr, result):
        if nums == []:
            result.append(list(curr))
            return
        for i, num in enumerate(nums):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            curr.append(num)
            self.dfs(nums[:i]+nums[i+1:], curr, result)
            curr.pop()
    
    def test(self):
        testCases = [
            [1,1,2],
            [3,3,0,3],
        ]
        for nums in testCases:
            print('nums: %s' % nums)
            result = self.permuteUnique(nums)
            print('result: %s' % result)
            print('-='*15+'-')

if __name__ == '__main__':
    Solution().test()