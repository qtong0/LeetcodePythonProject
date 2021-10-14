class Solution:
    # Will always return to original spot as long as it's not the original direction
    def isRobotBounded(self, instructions: str) -> bool:
        x, y = 0, 0
        dirs = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        d = 0
        for c in instructions:
            if c == 'R':
                d = (d+1) % 4
            elif c == 'L':
                d = (d+3) % 4
            else:
                x += dirs[d][0]
                y += dirs[d][1]
        return (x, y) == (0, 0) or d != 0

    def test(self):
        test_cases = [
            'GGLLGG',
            'GG',
            'GL',
            'GLRLLGLL',
            'LRRRRLLLRL',
        ]
        for instructions in test_cases:
            res = self.isRobotBounded(instructions)
            print('res: %s' % res)
            print('-='*30 + '-')


if __name__ == '__main__':
    Solution().test()
