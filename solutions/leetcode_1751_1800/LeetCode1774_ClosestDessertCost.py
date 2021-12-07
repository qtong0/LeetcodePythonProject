from typing import List


class Solution:
    def closestCost(self, baseCosts: List[int], toppingCosts: List[int], target: int) -> int:
        self.res = float('inf')
        self.target = target
        for base in baseCosts:
            self.helper(base, toppingCosts, 0)
        return self.res

    def helper(self, curr, toppingCosts, idx):
        if abs(curr - self.target) < abs(self.res - self.target):
            self.res = curr
        elif abs(curr - self.target) == abs(self.res - self.target):
            if curr < self.res:
                self.res = curr
        if idx == len(toppingCosts) or curr >= self.target:
            return
        self.helper(curr, toppingCosts, idx+1)
        self.helper(curr + toppingCosts[idx], toppingCosts, idx+1)
        self.helper(curr + toppingCosts[idx]*2, toppingCosts, idx+1)



    def test(self):
        test_cases = [
            [[1,7], [3,4], 10],
            [[2,3], [4,5,100], 18],
            [[3,10], [2,5], 9],
        ]
        for baseCosts, toppingCosts, target in test_cases:
            res = self.closestCost(baseCosts, toppingCosts, target)
            print('res: %s' % res)
            print('-='*30 + '-')



if __name__ == '__main__':
    Solution().test()
