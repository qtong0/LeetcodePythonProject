class Solution(object):
    def threeSumMulti(self, A, target):
        """
        :type A: List[int]
        :type target: int
        :rtype: int
        """
        hashmap = {}
        for num in A:
            hashmap[num] = hashmap.get(num, 0)+1
        res = 0
        MOD = 10**9+7
        nums = list(hashmap.keys())
        for i in range(len(nums)):
            a = nums[i]
            if a*3 == target and hashmap[a] >= 3:
                res += (hashmap[a]*(hashmap[a]-1)*(hashmap[a]-2)) // 6
            for j in range(i+1, len(nums)):
                b = nums[j]
                if a*2 + b == target and hashmap[a] >= 2:
                    res += (hashmap[a]*(hashmap[a]-1)//2*hashmap[b]) % MOD
                if a + 2*b == target and hashmap[b] >= 2:
                    res += (hashmap[b]*(hashmap[b]-1)//2*hashmap[a]) % MOD
                for k in range(j+1, len(nums)):
                    c = nums[k]
                    if a + b + c == target:
                        res += (hashmap[a]*hashmap[b]*hashmap[c]) % MOD
        return res % MOD

    def test(self):
        testCases = [
            [[1,1,2,2,3,3,4,4,5,5], 8],
            [[1,1,2,2,2,2], 5],
        ]
        for arr, target in testCases:
            res = self.threeSumMulti(arr, target)
            print('res: %s' % res)
            print('-='*30+'-')


if __name__ == '__main__':
    Solution().test()
