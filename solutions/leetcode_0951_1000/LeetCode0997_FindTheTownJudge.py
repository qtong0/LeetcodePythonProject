class Solution:
    def findJudge(self, N: int, trust) -> int:
        if N == 1 and not trust: return 1
        trustMap = {}
        candidates = set()
        for t in trust:
            trustMap[t[0]] = trustMap.get(t[0], []) + [t[1]]
            candidates.add(t[1])
        candidates -= trustMap.keys()
        if len(candidates) == 1:
            cand = candidates.pop()
            for num in range(1, N+1):
                if num != cand and \
                        (num not in trustMap or cand not in trustMap[num]):
                    return -1
            return cand
        return -1

    def test(self):
        testCases = [
            [2, [[1,2]]],
            [3, [[1,3],[2,3]]],
            [3, [[1,3],[2,3],[3,1]]],
        ]
        for n, trust in testCases:
            res = self.findJudge(n, trust)
            print('res: %s' % res)
            print('-='*30+'-')


if __name__ == '__main__':
    Solution().test()
