from typing import List

import itertools


class Solution:
    def braceExpansionII(self, expression: str) -> List[str]:
        groups = [[]]
        level = 0
        for i, c in enumerate(expression):
            if c == '{':
                if level == 0:
                    start = i+1
                level += 1
            elif c == '}':
                level -= 1
                if level == 0:
                    groups[-1].append(self.braceExpansionII(expression[start:i]))
            elif c == ',' and level == 0:
                groups.append([])
            elif level == 0:
                groups[-1].append([c])
        word_set = set()
        for group in groups:
            word_set = word_set | set(map(''.join, itertools.product(*group)))
        return sorted(word_set)

    def test(self):
        test_cases = [
            '{a,b}{c,{d,e}}',
            '{{a,z},a{b,c},{ab,z}}',
        ]
        for expression in test_cases:
            res = self.braceExpansionII(expression)
            print('res: %s' % res)
            print('-='*30 + '-')


if __name__ == '__main__':
    Solution().test()
