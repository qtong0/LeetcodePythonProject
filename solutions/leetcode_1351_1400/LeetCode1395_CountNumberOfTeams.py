from typing import List


class Solution:
    def numTeams(self, rating: List[int]) -> int:
        res = 0
        n = len(rating)
        for i in range(1, n):
            less = [0]*2
            greater = [0]*2
            for j in range(n):
                if rating[i] < rating[j]:
                    if j > i:
                        less[1] += 1
                    else:
                        less[0] += 1
                if rating[i] > rating[j]:
                    if j > i:
                        greater[1] += 1
                    else:
                        greater[0] += 1
            res += less[0]*greater[1] + greater[0]*less[1]
        return res


    def test(self):
        test_cases = [
            [2,5,3,4,1],
            [2,1,3],
            [1,2,3,4],
        ]
        for rating in test_cases:
            res = self.numTeams(rating)
            print('res: %s' % res)
            print('-='*30 + '-')


if __name__ == '__main__':
    Solution().test()
