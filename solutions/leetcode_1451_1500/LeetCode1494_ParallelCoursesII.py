from typing import List

from itertools import permutations


class Solution:
    # bitMask
    # TC: O(n^2 * 2^n)
    # SC: O(2^n * n)
    #
    def minNumberOfSemesters(self, n: int, relations: List[List[int]], k: int) -> int:
        dp = [[(100, 0, 0)] * n for _ in range(1 << n)]

        bm_dep = [0]*n
        for i, j in relations:
            bm_dep[j-1] ^= (1 << (i-1))

        for i in range(n):
            if bm_dep[i] == 0:
                dp[1 << i][i] = (1, 1, 1 << i)

        for i in range(1 << n):
            n_z_bits = [len(bin(i))-p-1 for p, c in enumerate(bin(i)) if c == '1']

            for t, j in permutations(n_z_bits, 2):
                if bm_dep[j] & i == bm_dep[j]:
                    cand, bits, mask = dp[i ^ (1 << j)][t]
                    if bm_dep[j] & mask == 0 and bits < k:
                        dp[i][j] = min(dp[i][j], (cand, bits + 1, mask + (1 << j)))
                    else:
                        dp[i][j] = min(dp[i][j], (cand+1, 1, 1 << j))

        return min([i for i, j, k in dp[-1]])


    def test(self):
        test_cases = [
            [4, [[2,1],[3,1],[1,4]], 2],
            [5, [[2,1],[3,1],[4,1],[1,5]], 2],
            [11, [], 2],
            [
                13,
                [[12,8],[2,4],[3,7],[6,8],[11,8],[9,4],[9,7],[12,4],[11,4],[6,4],[1,4],[10,7],[10,4],[1,7],[1,8],[2,7],[8,4],[10,8],[12,7],[5,4],[3,4],[11,7],[7,4],[13,4],[9,8],[13,8]],
                9,
            ],
        ]
        for n, relations, k in test_cases:
            res = self.minNumberOfSemesters(n, relations, k)
            print('res: %s' % res)
            print('-='*30 + '-')


if __name__ == '__main__':
    Solution().test()
