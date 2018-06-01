'''
Created on Jan 19, 2017

@author: MT
'''

class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        curr = []
        result = []
        if not nums: return result
        self.dfs(nums, curr, result)
        return result
    
    def dfs(self, nums, curr, result):
        if nums == []:
            result.append(list(curr))
            return
        for i, num in enumerate(nums):
            curr.append(num)
            self.dfs(nums[:i]+nums[i+1:], curr, result)
            curr.pop()
    
    def test(self):
        testCases = [
            [1, 2, 3]
        ]
        for nums in testCases:
            print('nums: %s' % nums)
            result = self.permute(nums)
            print('result: %s' % result)
            print('-='*15+'-')

if __name__ == '__main__':
    Solution().test()