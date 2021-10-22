from typing import List


class Solution:
    def evaluate(self, s: str, knowledge: List[List[str]]) -> str:
        hashmap = {}
        for key, val in knowledge:
            hashmap[key] = val
        res = ''
        prev = 0
        closed = True
        for i, c in enumerate(s):
            if c == '(':
                prev = i
                closed = False
            elif c == ')':
                closed = True
                sub = s[prev+1:i]
                if sub in hashmap:
                    res += hashmap[sub]
                else:
                    res += '?'
            else:
                if closed:
                    res += c
        return res

    def test(self):
        test_cases = [
            ["(name)is(age)yearsold", [["name","bob"],["age","two"]]],
            ["hi(name)", [["a","b"]]],
            ["(a)(a)(a)aaa", [["a","yes"]]],
            ["(a)(b)", [["a","b"],["b","a"]]],
        ]
        for s, knowledge in test_cases:
            res = self.evaluate(s, knowledge)
            print('res: %s' % res)
            print('-='*30 + '-')


if __name__ == '__main__':
    Solution().test()
