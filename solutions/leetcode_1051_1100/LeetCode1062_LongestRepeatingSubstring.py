class Solution:
    # binary search solution
    def longestRepeatingSubstring(self, S: str) -> int:
        l, r = 1, len(S)
        while l <= r:
            mid = (l+r)//2
            if self.search(S, mid):
                l += 1
            else:
                r -= 1
        return l-1

    def search(self, s, l):
        seen = set()
        for start in range(0, len(s)-l+1):
            tmp = s[start:start+l]
            if tmp in seen:
                return True
            seen.add(tmp)
        return False

    # O(n^2) slow
    def longestRepeatingSubstring_OWN_SLOW(self, S: str) -> int:
        n = len(S)
        hashmap = {}
        maxLen = 0
        for i in range(n):
            for j in range(i):
                sub = S[j:i+1]
                hashmap[sub] = hashmap.get(sub, 0)+1
                if hashmap[sub] > 1:
                    maxLen = max(maxLen, len(sub))
        return maxLen
