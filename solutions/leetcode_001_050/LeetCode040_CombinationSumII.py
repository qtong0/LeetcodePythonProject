'''
Created on Jun 6, 2018

@author: tongq
'''
class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        if not candidates: return []
        candidates.sort()
        res = []
        self.helper(candidates, target, 0, [], res)
        return res
    
    def helper(self, nums, target, ind, curr, res):
        if target == 0:
            res.append(list(curr))
            return
        prev = -1
        for i in range(ind, len(nums)):
            if nums[i] > target:
                return
            if prev != nums[i]:
                curr.append(nums[i])
                self.helper(nums, target-nums[i], i+1, curr, res)
                prev = curr.pop()
