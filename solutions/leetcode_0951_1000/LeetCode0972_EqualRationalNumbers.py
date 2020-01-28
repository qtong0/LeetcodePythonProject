import fractions

class Solution:
    def isRationalEqual(self, S: str, T: str) -> bool:
        def convert(s):
            if '.' not in s:
                return fractions.Fraction(int(s), 1)
            i = s.index('.')
            res = fractions.Fraction(int(s[:i]), 1)
            s = s[i+1:]
            if '(' not in s:
                if s:
                    res += fractions.Fraction(int(s), 10**len(s))
                return res
            i = s.index('(')
            if i:
                res += fractions.Fraction(int(s[:i]), 10**i)
            s = s[i+1:-1]
            j = len(s)
            res += fractions.Fraction(int(s), 10**i * (10**j - 1))
            return res
        return convert(S) == convert(T)
