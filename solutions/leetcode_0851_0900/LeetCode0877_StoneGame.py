'''
Created on Oct 8, 2019

@author: tongq
'''
class Solution(object):
    def stoneGame(self, piles):
        """
        :type piles: List[int]
        :rtype: bool
        """
        mem = {}
        return self.dfs(mem, piles, 0, [0, 0], sum(piles) / 2.0)
    
    def dfs(self, mem, piles, idx, nums, target):
        if not piles:
            return nums[idx%2] > target
        h = tuple(piles)
        if h in mem: return mem[h]
        if nums[idx%2] > target:
            mem[h] = True
            return True
        if nums[(idx+1)%2] > target:
            mem[h] = False
            return False
        for i in (0, -1):
            nums[idx%2] += piles[i]
            if not self.dfs(mem, piles, idx+1, nums, target) or \
            not self.dfs(mem, piles, idx+1, nums, target):
                mem[h] = True
                return True
            nums[idx%2] -= piles[i]
        mem[h] = False
        return False
    
    def test(self):
        testCases = [
            [3,7,2,3],
            [5,3,4,5],
        ]
        for piles in testCases:
            res = self.stoneGame(piles)
            print('res: %s' % res)
            print('-='*30+'-')

if __name__ == '__main__':
    Solution().test()
