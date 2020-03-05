import collections, re


class Solution(object):
    def basicCalculatorIV(self, expression: str, evalvars, evalints):
        class C(collections.Counter):
            def __add__(self, other):
                self.update(other)
                return self
            def __sub__(self, other):
                self.subtract(other)
                return self
            def __mul__(self, other):
                product = C()
                for x in self:
                    for y in other:
                        xy = tuple(sorted(x + y))
                        product[xy] += self[x] * other[y]
                return product
        vals = dict(zip(evalvars, evalints))
        def f(s):
            s = str(vals.get(s, s))
            return C({(s,): 1}) if s.isalpha() else C({(): int(s)})
        c = eval(re.sub('(\w+)', r'f("\1")', expression))
        return ['*'.join((str(c[x]),) + x)
                for x in sorted(c, key=lambda x: (-len(x), x))
                if c[x]]


    def test(self):
        testCases = [
            [
                "e + 8 - a + 5",
                ["e"],
                [1],
            ],
            [
                "e - 8 + temperature - pressure",
                ["e", "temperature"],
                [1, 12],
            ],
            [
                "7 - 7",
                [],
                [],
            ],
            [
                "a * b * c + b * a * c * 4",
                [],
                [],
            ],
            [
                "((a - b) * (b - c) + (c - a)) * ((a - b) + (b - c) * (c - a))",
                [],
                [],
            ],
        ]
        for expression, evalvars, evalints in testCases:
            result = self.basicCalculatorIV(expression, evalvars, evalints)
            print('result: %s' % result)
            print('-='*30+'-')

if __name__ == '__main__':
    Solution().test()
