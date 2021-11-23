from functools import lru_cache


class Solution:
    def getLengthOfOptimalCompression(self, s: str, k: int) -> int:
        # this decorator automatically use memo with key = (start, last, last_count, left)
        @lru_cache(None)
        def counter(start, last, last_count, left): #count the cost of compressing from the start
            if left < 0:
                return float('inf') # this is impossible
            if start >= len(s):
                return 0
            if s[start] == last:
                # we have a stretch of the last_count of the same chars, what is the cost of adding one more?
                incr = 1 if last_count == 1 or last_count == 9 or last_count == 99 else 0
                # no need to delete here, if we have a stretch of chars like 'aaaaa' - we delete it from the beginning in the else delete section
                return incr + counter(start+1, last, last_count+1, left) # we keep this char for compression
            else:
                # keep this char for compression - it will increase the result length by 1 plus the cost of compressing the rest of the string
                keep_counter = 1 + counter(start+1, s[start], 1, left)
                # delete this char
                del_counter =  counter(start + 1, last, last_count, left - 1)
            return min(keep_counter, del_counter)
        return counter(0, "", 0, k)


class Solution_another:
    # DFS + Memorization - should be good enough
    def getLengthOfOptimalCompression(self, s: str, k: int) -> int:
        n = len(s)
        self.addLen = set([1, 9, 99])
        self.dp = [[[[0]*(k+1) for _ in range(n+1)] for _ in range(27)] for _ in range(n+1)]
        return self.dfs(s, 0, chr(ord('a')+26), 0, k)


    def dfs(self, s, idx, c, count, k):
        if k < 0:
            return float('inf')
        if idx >= len(s):
            return 0
        if self.dp[idx][ord(c)-ord('a')][count][k]:
            return self.dp[idx][ord(c)-ord('a')][count][k]
        if s[idx] == c:
            res = self.dfs(s, idx+1, c, count+1, k) + (1 if count in self.addLen else 0)
        else:
            res = min(
                self.dfs(s, idx+1, s[idx], 1, k) + 1,
                self.dfs(s, idx+1, c, count, k-1),
            )
        self.dp[idx][ord(c)-ord('a')][count][k] = res
        return res


    def test(self):
        test_cases = [
            ["aaabcccd", 2],
            ["aabbaa", 2],
            ["aaaaaaaaaaa", 0],
        ]
        for s, k in test_cases:
            res = self.getLengthOfOptimalCompression(s, k)
            print('res: %s' % res)
            print('-='*30 + '-')


if __name__ == '__main__':
    Solution_another().test()
