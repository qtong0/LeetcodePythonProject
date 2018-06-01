'''
Created on Jan 21, 2017

@author: MT
'''

class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if not nums:
            return False
        farthest = nums[0]
        for i, num in enumerate(nums):
            if i<=farthest and num+i>farthest:
                farthest = num+i
        return farthest >= len(nums)-1
    
    def test(self):
        testCases = [
            [2,3,1,1,4],
            [3,2,1,0,4],
        ]
        for nums in testCases:
            print('nums: %s' % (nums))
            result = self.canJump(nums)
            print('result: %s' % (result))
            print('-='*15+'-')

if __name__ == '__main__':
    Solution().test()
