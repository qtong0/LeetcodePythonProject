# """
# This is Master's API interface.
# You should not implement it, or speculate about its implementation
# """
class Master:
    def guess(self, word: str) -> int:
        pass


# open solutions (interactive problem)
# other than the following two solutions, we can also
# 1) pass all the words in wordlist as it is
# 2) or randomize the wordlist first
class Solution(object):

    # Minimax solution
    def findSecretWord_minimax(self, wordlist: list[str], master: 'Master') -> None:
        n = 0
        while n < 6:
            hashmap = {}
            for w1 in wordlist:
                for w2 in wordlist:
                    if self.match(w1, w2):
                        if w1 not in hashmap:
                            hashmap[w1] = 0
                        hashmap[w1] += 1
            guess = min(wordlist, key=lambda w: hashmap[w])
            n = master.guess(guess)
            wordlist = [w for w in wordlist if self.match(w, guess) == n]

    def findSecretWord(self, wordlist: list[str], master: 'Master') -> None:
        n = 0
        best = 0
        while n < 6:
            count = [[0]*26 for _ in range(6)]
            for word in wordlist:
                for i in range(6):
                    count[i][ord(word[i]) - ord('a')] += 1
            for w in wordlist:
                score = 0
                for i in range(6):
                    score += count[i][ord(w[i]) - ord('a')]
                if score > best:
                    guess = w
                    best = score
            n = master.guess(guess)
            wordlist = [word for word in wordlist if self.match(word, guess) == n]

    def match(self, w1, w2):
        matches = 0
        for c1, c2 in zip(w1, w2):
            if c1 == c2: matches += 1
        return matches

    def test(self):
        testCases = [

        ]
        for wordlist, master in testCases:
            result = self.findSecretWord(wordlist, master)
            print('result: %s' % result)


if __name__ == '__main__':
    Solution().test()
