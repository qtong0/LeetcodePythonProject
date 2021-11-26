from typing import List


class Solution:
    def longestCommonSubsequence(self, arrays: List[List[int]]) -> List[int]:
        res = []
        counter = {}
        m = len(arrays)
        maxRowLen = max(len(row) for row in arrays)
        for j in range(maxRowLen):
            for i in range(m):
                if j < len(arrays[i]):
                    val = arrays[i][j]
                    counter[val] = counter.get(val, 0) + 1
                    if counter[val] == m:
                        res.append(val)
        return res


    def test(self):
        test_cases = [
            [[1,3,4], [1,4,7,9]],
            [[2,3,6,8], [1,2,3,5,6,7,10], [2,3,4,6,9]],
            [[1,2,3,4,5], [6,7,8]],
        ]
        for arrays in test_cases:
            res = self.longestCommonSubsequence(arrays)
            print('res: %s' % res)
            print('-='*30 + '-')


if __name__ == '__main__':
    Solution().test()
