from typing import List


class Solution(object):
    def shoppingOffers(self, price: List[int], special: List[List[int]], needs: List[int]) -> int:
        return self.helper(price, special, needs, 0)

    def helper(self, price, special, needs, pos):
        # direct purchase
        local_min = sum([price[i]*needs[i] for i in range(len(needs))])

        for i in range(pos, len(special)):
            offer = special[i]
            tmp = []
            for j in range(len(needs)):
                if needs[j] < offer[j]:
                    tmp = None
                    break
                tmp.append(needs[j] - offer[j])
            if tmp:
                local_min = min(local_min, offer[-1] + self.helper(price, special, tmp, i))
        return local_min


    def test(self):
        testCases = [
            [
                [2,5],
                [[3,0,5],[1,2,10]],
                [3,2],
            ],
            [
                [2,3,4],
                [[1,1,0,4],[2,2,1,9]],
                [1,2,1],
            ],
            [
                [9,9],
                [[1,1,1]],
                [2,2],
            ],
            [
                [2,3],
                [[1,0,1],[0,1,2]],
                [1,1],
            ],
        ]
        for price, special, needs in testCases:
            print('price: %s' % price)
            print('special: %s' % special)
            print('needs: %s' % needs)
            result = self.shoppingOffers(price, special, needs)
            print('result: %s' % result)
            print('-='*30+'-')


if __name__ == '__main__':
    Solution().test()
