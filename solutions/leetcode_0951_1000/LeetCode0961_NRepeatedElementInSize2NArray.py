class Solution:
    def repeatedNTimes(self, A) -> int:
        hashset = set()
        for num in A:
            if num in hashset:
                return num
            hashset.add(num)

    def test(self):
        testCases = [
            [2,1,2,5,2,1],
        ]
        for arr in testCases:
            res = self.repeatedNTimes(arr)
            print('res: %s' % res)
            print('-='*30+'-')


if __name__ == '__main__':
    Solution().test()
