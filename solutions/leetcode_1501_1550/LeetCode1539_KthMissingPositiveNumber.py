from typing import List


class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        l, r = 0, len(arr)-1
        while l <= r:
            mid = (l+r) // 2
            if arr[mid] - mid - 1 < k:
                l = mid + 1
            else:
                r = mid - 1
        return l + k

    # Slow O(N)
    def findKthPositive_slow(self, arr: List[int], k: int) -> int:
        i = 0
        for num in range(1, arr[-1]+1):
            if i < len(arr):
                if arr[i] != num:
                    k -= 1
                    if k == 0:
                        return num
                else:
                    i += 1
            else:
                break
        return arr[-1] + k

    def test(self):
        test_cases = [
            [[2,3,4,7,11], 5],
            [[1,2,3,4], 2],
        ]
        for arr, k in test_cases:
            res = self.findKthPositive(arr, k)
            print('res: %s' % res)
            print('-='*30 + '-')


if __name__ == '__main__':
    Solution().test()
