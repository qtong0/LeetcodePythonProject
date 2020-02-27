import random


class Solution:

    def __init__(self, n_rows: int, n_cols: int):
        self.m = n_rows
        self.n = n_cols
        self.remaining = list(range(self.m*self.n))

    def flip(self):
        idx = random.randint(0, len(self.remaining)-1)
        val = self.remaining[idx]
        self.remaining = self.remaining[:idx] + self.remaining[idx+1:]
        i, j = val//self.n, val%self.n
        return [i, j]

    def reset(self) -> None:
        self.remaining = list(range(self.m*self.n))


# Your Solution object will be instantiated and called as such:
# obj = Solution(n_rows, n_cols)
# param_1 = obj.flip()
# obj.reset()
