class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        arr = [0]*26
        for c in tiles:
            arr[ord(c) - ord('A')] += 1
        self.res = set()
        self.length = len(tiles)
        self.dfs(arr, '')
        return len(self.res)

    def dfs(self, arr, curr):
        if curr:
            self.res.add(curr)
        for i in range(len(arr)):
            if arr[i]:
                arr[i] -= 1
                self.dfs(arr, curr + chr(ord('A') + i))
                arr[i] += 1


    def test(self):
        test_cases = [
            'AAB',
            'AAABBC',
            'V',
        ]
        for tiles in test_cases:
            res = self.numTilePossibilities(tiles)
            print('res: %s' % res)
            print('-='*30 + '-')


if __name__ == '__main__':
    Solution().test()
