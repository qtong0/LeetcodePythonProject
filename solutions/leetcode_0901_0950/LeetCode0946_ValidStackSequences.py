class Solution(object):
    def validateStackSequences(self, pushed, popped):
        """
        :type pushed: List[int]
        :type popped: List[int]
        :rtype: bool
        """
        j = 0
        stack = []
        for num in pushed:
            stack.append(num)
            while stack and j < len(popped) and stack[-1] == popped[j]:
                stack.pop()
                j += 1
        return j == len(popped)

    def test(self):
        testCases = [
            [
                [1,0,2],
                [2,1,0],
            ],
            # [
            #     [2,1,0],
            #     [1,2,0],
            # ],
            [
                [1,2,3,4,5],
                [4,5,3,2,1],
            ],

        ]
        for pushed, popped in testCases:
            res = self.validateStackSequences(pushed,popped)
            print('res: %s' % res)
            print('-='*30+'-')


if __name__ == '__main__':
    Solution().test()
