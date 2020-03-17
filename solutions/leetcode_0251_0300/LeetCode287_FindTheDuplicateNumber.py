class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        val = nums[0]
        nextVal = nums[val]
        while val != nextVal:
            val = nums[val]
            nextVal = nums[nextVal]
            nextVal = nums[nextVal]
        val0 = 0
        while val0 != val:
            val0 = nums[val0]
            val = nums[val]
        return val
