from typing import List


class Solution:
    # Own DFS
    def maxScoreWords(self, words: List[str], letters: List[str], score: List[int]) -> int:
        hashmap = {}
        for c in letters:
            hashmap[c] = hashmap.get(c, 0) + 1
        return self.dfs(hashmap, words, 0, score)

    def dfs(self, hashmap, words, curr, score):
        if not words:
            return curr
        first = words[0]
        res = curr
        if self.wordExists(first, hashmap):
            new_map = dict(hashmap)
            word_score = self.getScore(first, new_map, score)
            res = max(res, curr + word_score + self.dfs(new_map, words[1:], curr, score))
        res = max(res, self.dfs(hashmap, words[1:], curr, score))
        return res

    def wordExists(self, word, hashmap):
        word_map = {}
        for c in word:
            word_map[c] = word_map.get(c, 0) + 1
        for c in word_map:
            if c not in hashmap or word_map[c] > hashmap[c]:
                return False
        return True

    def getScore(self, word, hashmap, score):
        res = 0
        for c in word:
            hashmap[c] -= 1
            res += score[ord(c) - ord('a')]
        return res

    def test(self):
        test_cases = [
            [["dog","cat","dad","good"], ["a","a","c","d","d","d","g","o","o"], [1,0,9,5,0,0,3,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,0,0,0,0]],
            [["xxxz","ax","bx","cx"], ["z","a","b","c","x","x","x"], [4,4,4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,5,0,10]],
            [["leetcode"], ["l","e","t","c","o","d"], [0,0,1,1,1,0,0,0,0,0,0,1,0,0,1,0,0,0,0,1,0,0,0,0,0,0]],
        ]
        for words, letters, score in test_cases:
            res = self.maxScoreWords(words, letters, score)
            print('res: %s' % res)
            print('-='*30 + '-')


if __name__ == '__main__':
    Solution().test()
