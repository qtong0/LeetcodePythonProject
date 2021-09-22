class Solution:
    def minNumberOperations(self, target: list[int]) -> int:
        res = pre = 0
        for val in target:
            res += max(val - pre, 0)
            pre = val
        return res

    ### my own recursive solution, TLE
    def minNumberOperations_own_TLE(self, target: list[int]) -> int:
        return self.helper(target, 0)

    def helper(self, target, min_val):
        if not target: return 0
        if len(target) == 1:
            return target[0] - min_val
        new_min = min(target)
        res = new_min - min_val
        prev = 0
        for i, val in enumerate(target):
            if val == new_min:
                if prev < i:
                    res += self.helper(target[prev:i], new_min)
                prev = i + 1
        if prev < i + 1:
            res += self.helper(target[prev:i + 1], new_min)
        return res

    def test(self):
        test_cases = [
            [1, 2, 3, 2, 1],
            [3, 1, 1, 2],
            [3, 1, 5, 4, 2],
            [1, 1, 1, 1],
        ]
        for target in test_cases:
            res = self.minNumberOperations(target)
            print('res: %s' % res)
            print('-=' * 30 + '-')


if __name__ == '__main__':
    Solution().test()
