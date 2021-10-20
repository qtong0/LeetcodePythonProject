class Solution:
    def tilingRectangle(self, n: int, m: int) -> int:
        if n == m:
            return 1
        if n > m:
            m, n = n, m
        self.res = float('inf')
        self.hashmap = {}
        self.dfs(n, m, [0]*(n+1), 0)
        return self.res

    def dfs(self, n, m, h, cnt):
        if cnt >= self.res:
            return
        isFull = True
        pos = -1
        minH = float('inf')
        for i in range(1, n+1):
            if h[i] < m:
                isFull = False;
            if h[i] < minH:
                pos = i
                minH = h[i]
        if isFull:
            self.res = min(self.res, cnt)

        key, base = 0, m+1
        for i in range(1, n+1):
            key += h[i] * base
            base *= (m+1)
        if key in self.hashmap and self.hashmap[key] <= cnt:
            return
        self.hashmap[key] = cnt

        end = pos
        while end+1 <= n and h[end+1] == h[pos] and (end+1-pos+1+minH) <= m:
            end += 1

        for j in range(end, pos-1, -1):
            curH = j-pos+1
            next_h = list(h)
            for k in range(pos, j+1):
                next_h[k] += curH
            self.dfs(n, m, next_h, cnt+1)


    def test(self):
        test_cases = [
            [2, 3],
            [5, 8],
            [11, 13],
        ]
        for n, m in test_cases:
            res = self.tilingRectangle(n, m)
            print('res: %s' % res)
            print('-='*30 + '-')


if __name__ == '__main__':
    Solution().test()
