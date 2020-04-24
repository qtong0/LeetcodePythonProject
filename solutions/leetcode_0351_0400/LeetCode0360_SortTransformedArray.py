class Solution:
    def sortTransformedArray(self, nums, a: int, b: int, c: int):
        n = len(nums)
        sorted = [0]*n
        i, j = 0, n-1
        if a >= 0:
            idx = n-1
        else:
            idx = 0
        while i <= j:
            if a >= 0:
                if self.quad(nums[i], a, b, c) >= self.quad(nums[j], a, b, c):
                    sorted[idx] = self.quad(nums[i], a, b, c)
                    i += 1
                else:
                    sorted[idx] = self.quad(nums[j], a, b, c)
                    j -= 1
                idx -= 1
            else:
                if self.quad(nums[i], a, b, c) >= self.quad(nums[j], a, b, c):
                    sorted[idx] = self.quad(nums[j], a, b, c)
                    j -= 1
                else:
                    sorted[idx] = self.quad(nums[i], a, b, c)
                    i += 1
                idx += 1
        return sorted

    def quad(self, x, a, b, c):
        return a*x*x + b*x + c

    def test(self):
        testCases = [
            [
                [-4,-2,2,4],
                -1,
                3,
                5,
            ],
        ]
        for nums, a, b, c in testCases:
            res = self.sortTransformedArray(nums, a, b, c)
            print('res: %s' % res)
            print('-='*30+'-')


if __name__ == '__main__':
    Solution().test()
