from typing import List


class Solution:
    # O(N)
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        res = 0
        n = len(arr)
        for i in range(n):
            res += ((i + 1) * (n - i) + 1) // 2 * arr[i]
        return res


    # O(N^2)
    # Passing LC
    def sumOddLengthSubarrays_own(self, arr: List[int]) -> int:
        res = 0
        n = len(arr)
        preSums = [0]
        for num in arr:
            preSums.append(preSums[-1] + num)
        for i in range(n):
            for j in range(i, n, 2):
                res += preSums[j+1] - preSums[i]
        return res


    def test(self):
        test_cases = [
            [1,4,2,5,3],
            [1],
            [1,2],
            [10,11,12],
        ]
        for arr in test_cases:
            res = self.sumOddLengthSubarrays(arr)
            print('res: %s' % res)
            print('-='*30 + '-')


if __name__ == '__main__':
    Solution().test()
