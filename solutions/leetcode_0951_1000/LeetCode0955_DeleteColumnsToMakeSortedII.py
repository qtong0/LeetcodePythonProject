class Solution(object):
    def minDeletionSize(self, A):
        """
        :type A: List[str]
        :rtype: int
        """
        # cuts[i] is True : we don't need to check col[i] <= col[i+1]
        cuts = [False] * (len(A)-1)
        res = 0
        for col in zip(*A):
            if all(cuts[i] or col[i] <= col[i+1] for i in range(len(A)-1)):
                for i in range(len(col)-1):
                    if col[i] < col[i+1]:
                        cuts[i] = True
            else:
                res += 1
        return res

    def test(self):
        testCases = [
            ["xc","yb","za"]
        ]
        for arr in testCases:
            res = self.minDeletionSize(arr)
            print('res: %s' % res)
            print('-='*30+'-')


if __name__ == '__main__':
    Solution().test()
