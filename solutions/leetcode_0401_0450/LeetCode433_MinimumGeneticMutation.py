from typing import List


class Solution:
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        queue = [start]
        visited = set(queue)
        level = 0
        while queue:
            n = len(queue)
            for _ in range(n):
                s = queue.pop(0)
                if s == end:
                    return level
                for nexts in self.getNext(s, bank):
                    if nexts not in visited:
                        queue.append(nexts)
                        visited.add(nexts)
            level += 1
        return -1

    def getNext(self, start, bank):
        res = []
        for s in bank:
            diff = 0
            for c1, c2 in zip(start, s):
                if c1 != c2:
                    diff += 1
                    if diff > 1:
                        break
            if diff == 1:
                res.append(s)
        return res

    def test(self):
        test_cases = [
            ["AACCGGTT", "AACCGGTA", ["AACCGGTA"]],
            ["AACCGGTT", "AAACGGTA", ["AACCGGTA","AACCGCTA","AAACGGTA"]],
            ["AAAAACCC", "AACCCCCC", ["AAAACCCC","AAACCCCC","AACCCCCC"]],
        ]
        for start, end, bank in test_cases:
            res = self.minMutation(start, end, bank)
            print('res: %s' % res)
            print('-='*30 + '-')


if __name__ == '__main__':
    Solution().test()
