class Solution:
    def longestOnes(self, A, K: int) -> int:
        i = 0
        for j in range(len(A)):
            if A[j] == 0:
                K -= 1
            if K < 0:
                if A[i] == 0:
                    K += 1
                i += 1
        return j-i+1


    def longestOnes_Space(self, A, K: int) -> int:
        queue = []
        res = 0
        left = -1
        for i, num in enumerate(A):
            if num == 0:
                queue.append(i)
                res = max(res, i-left-1)  # Check this first
                if len(queue) > K:
                    left = queue.pop(0)
        res = max(res, len(A)-left-1)
        return res

    def test(self):
        testCases = [
            [[0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], 3],
            [[1,1,1,0,0,0,1,1,1,1,0], 2],
            [[0,0,1,1,1,0,0], 0],
            [[1,1,1,1], 0],
            [[0,0,1,1,1,0,0,1,1,1,1], 0],
            [[0,0,0,1], 4],
            [[0,0,0,1], 2],
            [[1,0,0,0,1,1,0,0,1,1,0,0,0,0,0,0,1,1,1,1,0,1,0,1,1,1,1,1,1,0,1,0,1,0,0,1,1,0,1,1], 8],
        ]
        for arr, k in testCases:
            res = self.longestOnes(arr, k)
            print('res: %s' % res)
            print('-='*30+'-')


if __name__ == '__main__':
    Solution().test()
