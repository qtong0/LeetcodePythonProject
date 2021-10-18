from typing import List


class Solution:
    # Binary Search O(Log(N))
    def findSpecialInteger(self, arr: List[int]) -> int:
        for i in range(1, 4):
            idx = int(i * len(arr) / 4)
            start = self.findIndexOfFirst(arr, arr[idx])
            if arr[start] == arr[start+len(arr) // 4]:
                return arr[start]

    def findIndexOfFirst(self, arr, num):
        l, r = 0, len(arr)-1
        while l <= r:
            mid = (l + r) // 2
            if arr[mid] < num:
                l = mid + 1
            else:
                r = mid - 1
        return l



    # O(N) solution - slow
    def findSpecialInteger_own_slow(self, arr: List[int]) -> int:
        if len(arr) < 3:
            return arr[0]
        count = 1
        for i, num in enumerate(arr):
            if i > 0 and num == arr[i-1]:
                count += 1
                if count > len(arr) // 4:
                    return num
            else:
                count = 1



    def test(self):
        test_cases = [
            [1,2,2,6,6,6,6,7,10],
            [1,1],
        ]
        for arr in test_cases:
            res = self.findSpecialInteger(arr)
            print('res: %s' % res)
            print('-='*30 + '-')


if __name__ == '__main__':
    Solution().test()
