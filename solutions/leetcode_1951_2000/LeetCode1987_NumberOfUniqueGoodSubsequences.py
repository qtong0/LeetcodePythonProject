class Solution:
    # ends0: if we meet 0, we can append 0 to all existing ends0 + ends1
    # ends0 = ends0 + ends1
    #
    # ends1: if we meet 1, we can append 1 to all existing ends0 + ends1
    # and also adding "1"
    # ends1 = ends0 + ends1 + 1
    #
    # example:
    # num         1          0          1                  1
    # end0Count   0          1          1                  1
    # end1Count   1          1          3                  5
    # end0Arr     []        [10]       [10]               [10]
    # end1Arr     [1]       [1]        [11, 101, 1]       [101, 111, 1011, 11, 1]

    def numberOfUniqueGoodSubsequences(self, binary: str) -> int:
        MOD = 10**9 + 7
        ends0 = 0
        ends1 = 0
        has0 = 0
        for i, c in enumerate(binary):
            if c == '1':
                ends1 = (ends0 + ends1 + 1) % MOD
            else:
                ends0 = (ends0 + ends1) % MOD
                has0 = 1
        return (ends0 + ends1 + has0) % MOD


    def test(self):
        test_cases = [
            '001',
            '11',
            '101',
        ]
        for binary in test_cases:
            res = self.numberOfUniqueGoodSubsequences(binary)
            print('res: %s' % res)
            print('-='*30 + '-')


if __name__ == '__main__':
    Solution().test()
