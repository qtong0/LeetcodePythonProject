class Solution:
    def mergeStones(self, stones, K: int) -> int:
        mem = {}
        return self.helper(stones, K, mem)

    def helper(self, stones, k, mem):
        if not stones: return 0
        hash = str(stones)
        if hash in mem:
            return mem[hash]
        if len(stones) == 1:
            mem[hash] = 0
            return 0
        if len(stones) < k:
            mem[hash] = -1
            return -1
        sumVals = [0]
        for i, num in enumerate(stones):
            sumVals.append(num+sumVals[-1])
        minVal = float('inf')
        for i in range(len(stones)-k+1):
            sumVal = sumVals[i+k] - sumVals[i]
            res = self.helper(stones[:i] + [sumVal] + stones[i+k:], k, mem)
            if res != -1:
                minVal = min(minVal, sumVal+res)
        res = minVal if minVal != float('inf') else -1
        mem[hash] = res
        return res

    def test(self):
        testCases = [
            [[3,2,4,1], 2],
            [[3,2,4,1], 3],
            [[3,5,1,2,6], 3],
            [
                [16,43,87,30,4,98,12,30,47,45,32,4,64,14,24,84,86,51,11,22,4],
                2,
            ],
        ]
        for stones, k in testCases:
            res = self.mergeStones(stones, k)
            print('res: %s' % res)
            print('-='*30+'-')


if __name__ == '__main__':
    Solution().test()
