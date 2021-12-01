from typing import List


class Solution:
    # Binary Search + Longest Increasing Sequence
    def minOperations(self, target: List[int], arr: List[int]) -> int:
        hashmap = {}
        for i, num in enumerate(target):
            hashmap[num] = i
        stack = []
        for num in arr:
            if num not in hashmap:
                continue
            if not stack or hashmap[num] > stack[-1]:
                stack.append(hashmap[num])
                continue
            l, r = 0, len(stack)-1
            while l < r:
                mid = (l + r) // 2
                if stack[mid] < hashmap[num]:
                    l = mid + 1
                else:
                    r = mid
            stack[l] = hashmap[num]
        return len(target) - len(stack)


    # Using Longest Common Sequence is still not the best solution
    def minOperations_own_TLE_LCS(self, target: List[int], arr: List[int]) -> int:
        lcs = self.lcs(target, arr)
        return len(target) - lcs

    def lcs(self, target, arr):
        m, n = len(target), len(arr)
        dp = [[0]*(n+1) for _ in range(m+1)]
        for i in range(m):
            for j in range(n):
                if target[i] == arr[j]:
                    dp[i+1][j+1] = dp[i][j] + 1
                else:
                    dp[i+1][j+1] = max(dp[i][j+1], dp[i+1][j])
        return dp[-1][-1]


    def test(self):
        test_cases = [
            [[5,1,3], [9,4,2,3,4]],
            [[6,4,8,1,3,2], [4,7,6,2,3,8,6,1]],
        ]
        for target, arr in test_cases:
            res = self.minOperations(target, arr)
            print('res: %s' % res)
            print('-='*30 + '-')


if __name__ == '__main__':
    Solution().test()
