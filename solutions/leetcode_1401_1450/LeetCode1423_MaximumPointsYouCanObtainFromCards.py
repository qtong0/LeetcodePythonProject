from typing import List


class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        front_sum, back_sum = [0], [0]
        for num in cardPoints:
            front_sum.append(front_sum[-1] + num)
        for num in cardPoints[::-1]:
            back_sum.append(back_sum[-1] + num)
        all_combinations = []
        for i in range(k+1):
            all_combinations.append(front_sum[i] + back_sum[k-i])
        return max(all_combinations)


    ### Own solution, but DFS + Memorization is not good enough :'(
    def maxScore_own(self, cardPoints: List[int], k: int) -> int:
        mem = {}
        return self.dfs(cardPoints, mem, k, 0)

    def dfs(self, card_points, mem, k, value):
        hash = str(card_points)
        if hash in mem:
            return mem[hash]
        if k == 0:
            mem[hash] = value
            return value
        first, last = card_points[0], card_points[-1]
        return max(
            self.dfs(card_points[1:], mem, k-1, value+first),
            self.dfs(card_points[:-1], mem, k-1, value+last)
        )

    def test(self):
        test_cases = [
            [[1,2,3,4,5,6,1], 3],
            [[2,2,2], 2],
            [[9,7,7,9,7,7,9], 7],
            [[1,1000,1], 1],
            [[1,79,80,1,1,1,200,1], 3],
        ]
        for card_points, k in test_cases:
            res = self.maxScore(card_points, k)
            print('res: %s' % res)
            print('-='*30+'-')


if __name__ == '__main__':
    Solution().test()
