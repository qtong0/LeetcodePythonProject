from typing import List


class Solution(object):
    def largestTimeFromDigits(self, arr: List[int]) -> str:
        arr.sort(reverse=True)
        res = self.dfs(arr, '')
        if res:
            return res[:2] + ':' + res[2:]
        return ''

    def dfs(self, arr, curr):
        if len(curr) == 4:
            return curr
        res = None
        for i, num in enumerate(arr):
            if len(curr) == 0:
                if num <= 2:
                    res = self.dfs(arr[:i] + arr[i+1:], curr + str(num))
            elif len(curr) == 1:
                if curr + str(num) <= '23':
                    res = self.dfs(arr[:i] + arr[i+1:], curr + str(num))
            elif len(curr) == 2:
                if num <= 6:
                    res = self.dfs(arr[:i] + arr[i+1:], curr + str(num))
            elif len(curr) == 3:
                if curr[-1] + str(num) <= '59':
                    res = self.dfs(arr[:i] + arr[i+1:], curr + str(num))
            if res:
                return res


    def largestTimeFromDigits_own_slow(self, arr: List[int]) -> str:
        for num in range(24*60-1, -1, -1):
            mins = num % 60
            hours = num // 60
            tmp = '%02d%02d' % (hours, mins)
            if sorted(''.join(str(num0) for num0 in arr)) == sorted(tmp):
                return tmp[:2] + ':' + tmp[2:]
        return ''


    def test(self):
        testCases = [
            [1,2,3,4],
        ]
        for arr in testCases:
            res = self.largestTimeFromDigits(arr)
            print('res: %s' % res)
            print('-='*30+'-')


if __name__ == '__main__':
    Solution().test()
