class Solution(object):
    def __init__(self):
        self.dp = {0:0}

    def racecar(self, target: int) -> int:
        if target in self.dp:
            return self.dp[target]
        # Number of bits necessary to represent self in binary.
        n = target.bit_length()
        if 2**n-1 == target:
            self.dp[target] = n
        else:
            self.dp[target] = self.racecar(2**n-1-target)+n+1
            for m in range(n-1):
                self.dp[target] = min(self.dp[target],\
                            self.racecar(target-2**(n-1)+2**m)+n+m+1)
        return self.dp[target]
    
    def test(self):
        testCases = [
            3,
            6,
        ]
        for target in testCases:
            print('target: %s' % target)
            result = self.racecar(target)
            print('result: %s' % result)
            print('-='*30+'-')

if __name__ == '__main__':
    Solution().test()
