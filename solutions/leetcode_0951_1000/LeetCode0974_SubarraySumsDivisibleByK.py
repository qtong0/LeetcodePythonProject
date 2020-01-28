class Solution:
    def subarraysDivByK(self, A, K: int) -> int:
        arr = [0]
        for num in A:
            arr.append((arr[-1] + num) % K)
        counter = {}
        for num in arr:
            counter[num] = counter.get(num, 0)+1
        return sum(v*(v-1)//2 for v in counter.values())

    def test(self):
        testCases = [
            [
                [4,5,0,-2,-3,1],
                5,
            ],
            [
                [5],
                9,
            ],
        ]
        for arr, k in testCases:
            res = self.subarraysDivByK(arr, k)
            print('res: %s' % res)
            print('-='*30+'-')


if __name__ == '__main__':
    Solution().test()
