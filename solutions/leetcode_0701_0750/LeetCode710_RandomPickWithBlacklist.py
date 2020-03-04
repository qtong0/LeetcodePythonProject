import random


class Solution(object):

    def __init__(self, N, blacklist):
        """
        :type N: int
        :type blacklist: List[int]
        """
        self.blacklist = sorted(blacklist)
        self.n = N

    def pick(self):
        """
        :rtype: int
        """
        k = random.randint(0, self.n-len(self.blacklist)-1)
        l, r = 0, len(self.blacklist)-1
        while l < r:
            mid = (l+r+1)//2
            if self.blacklist[mid] - mid > k:
                r = mid-1
            else:
                l = mid
        if l == r and self.blacklist[l]-l <= k:
            return k+l+1
        else:
            return k


# Your Solution object will be instantiated and called as such:
# obj = Solution(N, blacklist)
# param_1 = obj.pick()
