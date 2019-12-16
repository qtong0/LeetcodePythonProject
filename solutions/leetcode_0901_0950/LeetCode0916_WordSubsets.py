class Solution(object):
    def wordSubsets(self, A, B):
        """
        :type A: List[str]
        :type B: List[str]
        :rtype: List[str]
        """
        hashmap0 = {}
        for s in B:
            hashmap = {}
            for c in s:
                hashmap[c] = hashmap.get(c, 0)+1
            for c, count in hashmap.items():
                if hashmap0.get(c, 0) < count:
                    hashmap0[c] = count
        res = []
        for s in A:
            hashmap = {}
            for c in s:
                hashmap[c] = hashmap.get(c, 0)+1
            if all(hashmap.get(c, 0) >= hashmap0[c] for c in hashmap0):
                res.append(s)
        return res


    def test(self):
        testCases = [
            [
                ["amazon","apple","facebook","google","leetcode"], ["e","o"]
            ],
            [
                ["amazon","apple","facebook","google","leetcode"], ["l","e"]
            ],
            [
                ["amazon","apple","facebook","google","leetcode"], ["e","oo"],
            ],
            [
                ['leetcode'], ['lo', 'eo']
            ],
            [
                ["amazon","apple","facebook","google","leetcode"], ["lo","eo"],
            ],
            [
                ["amazon","apple","facebook","google","leetcode"], ["ec","oc","ceo"],
            ],
        ]
        for a, b in testCases:
            res = self.wordSubsets(a, b)
            print('res: %s' % res)
            print('-='*30+'-')


if __name__ == '__main__':
    Solution().test()
