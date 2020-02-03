class Solution:
    def equationsPossible(self, equations) -> bool:
        roots = list(range(26))
        for s in equations:
            if '==' == s[1:3]:
                val1, val2 = ord(s[0])-ord('a'), ord(s[3])-ord('a')
                root1 = self.findRoot(roots, val1)
                root2 = self.findRoot(roots, val2)
                roots[root1] = root2

        for s in equations:
            if '!=' == s[1:3]:
                val1, val2 = ord(s[0])-ord('a'), ord(s[3])-ord('a')
                root1 = self.findRoot(roots, val1)
                root2 = self.findRoot(roots, val2)
                if root1 == root2:
                    return False

        return True

    def findRoot(self, roots, val):
        while val != roots[val]:
            val = roots[val]
        return val

    def test(self):
        testCases = [
            ["a==b","b!=a"],
            ["b==b","b==e","e==c","d!=e"],
        ]
        for equations in testCases:
            res = self.equationsPossible(equations)
            print('res: %s' % res)
            print('-='*30+'-')


if __name__ == '__main__':
    Solution().test()
