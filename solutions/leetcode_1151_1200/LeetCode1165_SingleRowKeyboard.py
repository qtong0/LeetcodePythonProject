class Solution:
    def calculateTime(self, keyboard: str, word: str) -> int:
        hashmap = {}
        for i, k in enumerate(keyboard):
            hashmap[k] = i
        res = 0
        prev = 0
        for c in word:
            idx = hashmap[c]
            res += abs(idx-prev)
            prev = idx
        return res
