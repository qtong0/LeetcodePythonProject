from typing import List


class Solution:
    # two pointers, count zero first
    def duplicateZeros(self, arr: List[int]) -> None:
        n = len(arr)
        zeros = arr.count(0)
        for i in range(n-1, -1, -1):
            if i + zeros < n:
                arr[i+zeros] = arr[i]
            if arr[i] == 0:
                zeros -= 1
                if i + zeros < n:
                    arr[i + zeros] = 0


    # own solution, space complexity is O(N)
    def duplicateZeros_own_space(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        n = len(arr)
        new_arr = [0]*n
        j = 0
        for i, num in enumerate(arr):
            if j >= n:
                break
            if num != 0:
                new_arr[j] = num
                j += 1
            else:
                j += 2
        for i, num in enumerate(new_arr):
            arr[i] = num
