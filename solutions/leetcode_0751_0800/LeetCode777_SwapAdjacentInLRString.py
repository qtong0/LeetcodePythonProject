class Solution(object):
    def canTransform(self, start: str, end: str) -> bool:
        if len(start) != len(end):
            return False
        arr_start = [(idx, c) for idx, c in enumerate(start) if c in 'LR']
        arr_end = [(idx, c) for idx, c in enumerate(end) if c in 'LR']
        if len(arr_start) != len(arr_end):
            return False

        for (i, cs), (j, ce) in zip(arr_start, arr_end):
            if cs != ce:
                return False
            if cs == 'L':
                if i < j:
                    return False
            if ce == 'R':
                if i > j:
                    return False
        return True


    # The following BFS solution is TLE
    def canTransform_bfs_TLE(self, start: str, end: str) -> bool:
        visited = set([start])
        queue = [start]
        while queue:
            s = queue.pop()
            if s == end:
                return True
            for i in range(len(s)-1):
                if s[i:i+2] in ('XL', 'RX'):
                    newS = s[:i]+s[i:i+2][::-1]+s[i+2:]
                    if newS not in visited:
                        visited.add(newS)
                        queue.append(newS)
        return False


    def test(self):
        testCases = [
            [
                "RLX",
                "XLR",
            ],
            [
                "RXXLRXRXL",
                "XRLXXRRLX",
            ],
            [
                "XXRXXLXXXX",
                "XXXXRXXLXX",
            ],
        ]
        for start, end in testCases:
            print('start: %s' % start)
            print('end: %s' % end)
            result = self.canTransform(start, end)
            print('result: %s' % result)
            print('-='*30+'-')


if __name__ == '__main__':
    Solution().test()
