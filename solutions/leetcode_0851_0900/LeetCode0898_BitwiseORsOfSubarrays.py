class Solution(object):
    def subarrayBitwiseORs(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        prevSet = set()
        uniqSet = set()
        for num in A:
            currSet = set()
            prevSet.add(0)
            for num1 in prevSet:
                currSet.add(num | num1)
                uniqSet.add(num | num1)
            prevSet = currSet
        return len(uniqSet)

    def subarrayBitwiseORs_own_DFS_TLE(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        hashset = set()
        self.dfs(hashset, 0, len(A)-1, A)
        return len(hashset)

    def dfs(self, hashset, start, end, A):
        if A[start:end+1]:
            tmp = 0
            for i in range(start, end+1):
                tmp |= A[i]
            hashset.add(tmp)
        for i in range(start, end+1):
            self.dfs(hashset, start, i-1, A)
            self.dfs(hashset, i+1, end, A)

    def test(self):
        testCases = [
            # [0],
            # [1, 1, 2],
            [1, 2, 4],
        ]
        for arr in testCases:
            res = self.subarrayBitwiseORs(arr)
            print('res: %s' % res)
            print('-='*30+'-')


if __name__ == '__main__':
    Solution().test()
