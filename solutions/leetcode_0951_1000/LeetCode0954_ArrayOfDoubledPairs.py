class Solution(object):
    def canReorderDoubled(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        A.sort()
        hashmap = {}
        for num in A:
            hashmap[num] = hashmap.get(num, 0)+1
        addedCount = {}
        for num in A:
            val = num*2 if num > 0 else num/2.0
            if num not in addedCount and val in hashmap:
                hashmap[val] -= 1
                if hashmap[val] == 0:
                    del hashmap[val]
                addedCount[val] = addedCount.get(val, 0)+1
            elif num in addedCount:
                addedCount[num] -= 1
                if addedCount[num] == 0:
                    del addedCount[num]
            else:
                return False
        return True

    def test(self):
        testCases = [
            [-5,-3],
            [3,1,3,6],
            [4,-2,2,-4],
            [1,2,4,16,8,4],
        ]
        for arr in testCases:
            res = self.canReorderDoubled(arr)
            print('res: %s' % res)
            print('-='*30+'-')


if __name__ == '__main__':
    Solution().test()
