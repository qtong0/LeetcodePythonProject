from typing import List


class Solution:
    # Time O(N), Space O(1)
    # from below solution
    #
    def numOfSubarrays(self, arr: List[int]) -> int:
        if not arr:
            return 0
        odds, evens, res = 0, 0, 0
        for i, num in enumerate(arr):
            is_odd = (num % 2 != 0)
            odds_prev, evens_prev = odds, evens
            if is_odd:
                odds = evens_prev + 1
                evens = odds_prev
            else:
                odds = odds_prev
                evens = evens_prev + 1
            res = (res + odds) % (10**9 + 7)
        return res

    # O(N) Space, can start from here
    def numOfSubarrays_space(self, arr: List[int]) -> int:
        if not arr:
            return 0
        n = len(arr)
        odds = [0]*n
        evens = [0]*n
        for i, num in enumerate(arr):
            is_odd = (num % 2 != 0)
            if i == 0:
                odds[i] = 1 if is_odd else 0
                evens[i] = 0 if is_odd else 1
            else:
                if is_odd:
                    odds[i] = evens[i-1] + 1
                    evens[i] = odds[i-1]
                else:
                    evens[i] = evens[i-1] + 1
                    odds[i] = odds[i-1]
        return sum(odds) % (10**9+7)

    def test(self):
        test_cases = [
            [1,3,5],
            [2,4,6],
            [1,2,3,4,5,6,7],
        ]
        for arr in test_cases:
            res = self.numOfSubarrays(arr)
            print('res: %s' % res)
            print('-='*30 + '-')


if __name__ == '__main__':
    Solution().test()
