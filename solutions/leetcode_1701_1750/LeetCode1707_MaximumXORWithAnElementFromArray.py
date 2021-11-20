from typing import List


class Trie:
    def __init__(self):
        self.root = {}

    def insert(self, num):
        node = self.root
        for i in range(31, -1, -1):
            curr = (num >> i) & 1
            if curr not in node:
                node[curr] = {}
            node = node[curr]

    def query(self, num):
        if not self.root:
            return -1
        node, res = self.root, 0
        for i in range(31, -1, -1):
            curr = (num >> i) & 1
            if 1 - curr in node:
                node = node[1 - curr]
                res |= (1 << i)
            else:
                node = node[curr]
        return res


class Solution:
    def maximizeXor(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        nums.sort()
        queries = sorted(enumerate(queries), key=lambda x: x[1][1])
        trie = Trie()
        res = [-1] * len(queries)
        j = 0
        for i, (x, m) in queries:
            while j < len(nums) and nums[j] <= m:
                trie.insert(nums[j])
                j += 1
            res[i] = trie.query(x)
        return res


    def maximizeXor_own_BruteForce(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        nums.sort()
        res = []
        for x, m in queries:
            if nums[0] > m:
                res.append(-1)
            else:
                tmp = float('-inf')
                for num in nums:
                    if num > m:
                        break
                    tmp = max(tmp, num ^ x)
                res.append(tmp)
        return res

    def test(self):
        test_cases = [
            [[0, 1, 2, 3, 4], [[3, 1], [1, 3], [5, 6]]],
            [[5, 2, 4, 6, 6, 3], [[12, 4], [8, 1], [6, 3]]],
        ]
        for nums, queries in test_cases:
            res1 = self.maximizeXor(nums, queries)
            res2 = self.maximizeXor_own_BruteForce(nums, queries)
            print('res1: %s' % res1)
            print('res2: %s' % res2)
            print('-=' * 30 + '-')


if __name__ == '__main__':
    Solution().test()
