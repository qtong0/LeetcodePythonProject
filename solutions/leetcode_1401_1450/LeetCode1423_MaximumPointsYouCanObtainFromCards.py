class Solution:
    def maxScore(self, cardPoints: list[int], k: int) -> int:
        size = len(cardPoints) - k
        minSubArraySum = float('inf')
        j = curr = 0

        for i, val in enumerate(cardPoints):
            curr += val
            if i-j+1 > size:
                curr -= cardPoints[j]
                j += 1
            if i-j+1 == size:
                minSubArraySum = min(minSubArraySum, curr)

        return sum(cardPoints) - minSubArraySum


    ### Own solution, but DFS + Memorization is not good enough :'(
    def maxScore_own(self, cardPoints: list[int], k: int) -> int:
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
