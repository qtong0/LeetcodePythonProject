from typing import List


class Solution(object):
    def wordsTyping(self, sentence: List[str], rows: int, cols: int) -> int:
        n = len(sentence)
        times = [0]*n
        nextInd = [0]*n
        for i in range(n):
            ind = i
            curLen = 0
            time = 0
            while curLen+len(sentence[ind])<=cols:
                curLen += len(sentence[ind])+1
                ind += 1
                if ind == len(sentence):
                    ind = 0
                    time += 1
            nextInd[i] = ind
            times[i] = time
        ind = 0
        res = 0
        for _ in range(rows):
            res += times[ind]
            ind = nextInd[ind]
        return res
    
    def test(self):
        testCases = [
            (["hello", "world"], 2, 8),
            (["a", "bcd", "e"], 3, 6),
            (["I", "had", "apple", "pie"], 4, 5),
        ]
        for sentence, rows, cols in testCases:
            print('sentence: %s' % sentence)
            print('rows: %s' % rows)
            print('cols: %s' % cols)
            result = self.wordsTyping(sentence, rows, cols)
            print('result: %s' % result)
            print('-='*20+'-')


if __name__ == '__main__':
    Solution().test()
