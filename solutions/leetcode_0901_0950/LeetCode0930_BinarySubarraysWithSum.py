class Solution(object):
    def numSubarraysWithSum(self, A, S):
        """
        :type A: List[int]
        :type S: int
        :rtype: int
        """
        sumVal = 0
        hashmap = {0:1}
        res = 0
        for num in A:
            sumVal += num
            res += hashmap.get(sumVal-S, 0)
            hashmap[sumVal] = hashmap.get(sumVal, 0) + 1
        return res

    def test(self):
        testCases = [
            [
                [1,0,1,0,1],
                2
             ]
        ]
        for a, s in testCases:
            res = self.numSubarraysWithSum(a, s)
            print('res: %s' % res)
            print('-='*30+'-')


if __name__ == '__main__':
    Solution().test()
