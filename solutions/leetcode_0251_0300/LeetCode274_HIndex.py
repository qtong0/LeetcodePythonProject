from typing import List


class Solution(object):
    def hIndex(self, citations: List[int]) -> int:
        length = len(citations)
        count = [0]*(length+1)
        for c in citations:
            if c > length:
                count[length] += 1
            else:
                count[c] += 1
        total = 0
        for i in range(length, -1, -1):
            total += count[i]
            if total >= i:
                return i
        return 0
    
    def test(self):
        testCases = [
            [3, 0, 6, 1, 5],
        ]
        for citations in testCases:
            print('citations: %s' % (citations))
            result = self.hIndex(citations)
            print('result: %s' % (result))
            print('-='*20+'-')


if __name__ == '__main__':
    Solution().test()
