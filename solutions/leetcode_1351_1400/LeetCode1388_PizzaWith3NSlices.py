from typing import List


class Solution:
    def maxSizeSlices(self, slices: List[int]) -> int:
        memo = {}
        return self.helper(slices, 0, len(slices)-1, len(slices) // 3, 1, memo)

    def helper(self, slices, start, end, n, cycle, memo):
        serializaed = '%s#%s#%s#%s' % (start, end, n, cycle)
        if serializaed in memo:
            return memo[serializaed]
        if n == 1:
            res = float('-inf')
            for i in range(start, end+1):
                res = max(res, slices[i])
            memo[serializaed] = res
            return res
        if end - start + 1 < n*2 -1:
            memo[serializaed] = float('-inf')
            return float('-inf')
        res = max(
            self.helper(slices, start + cycle, end-2, n-1, 0, memo) + slices[end],
            self.helper(slices, start, end-1, n, 0, memo)
        )
        memo[serializaed] = res
        return res



    # Own DFS TLE
    def maxSizeSlices_own_DFS_TLE(self, slices: List[int]) -> int:
        self.res = 0
        for i in range(len(slices)):
            self.dfs(slices, i, [0, 0, 0])
        return self.res

    def dfs(self, slices, i, arr):
        if len(slices) <= 3:
            self.res = max(self.res, arr[0] + max(slices))
            return
        n = len(slices)
        val1 = slices[i]
        val2 = slices[i+1 if i+1 < n else i+1-n]
        val3 = slices[i-1]
        arr[0] += val1
        arr[1] += val2
        arr[2] += val3
        if i == 0:
            slices = slices[2:n-1]
        elif i == n-1:
            slices = slices[1:n-2]
        else:
            slices = slices[:i-1] + slices[i+2:]
        for idx in range(n-3):
            self.dfs(slices, idx, arr)
        arr[0] -= val1
        arr[1] -= val2
        arr[2] -= val3



    def test(self):
        test_cases = [
            [1,2,3,4,5,6],
            [8,9,8,6,1,1],
            [4,1,2,5,8,3,1,9,7],
            [3,1,2],
        ]
        for slices in test_cases:
            res = self.maxSizeSlices(slices)
            print('res: %s' % res)
            print('-='*30 + '-')


if __name__ == '__main__':
    Solution().test()

    # arr = [0, 1, 2, 3, 4]
    # n = 5
    # print(arr[1:5-2])
    # print(arr[2:5-1])
    # print(arr[:0] + arr[3:])
