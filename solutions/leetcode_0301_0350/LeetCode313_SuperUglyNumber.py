from typing import List
import heapq


class Solution:
    # O(N*Log(k))
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        heap = []
        for p in primes:
            heapq.heappush(heap, [p, p, 0])
        nums = [0]*(n + 1)
        nums[0] = 1
        i = 1
        while i < n:
            entry = heapq.heappop(heap)
            num = entry[0]
            prime = entry[1]
            idx = entry[2]
            # remove duplicate
            if num != nums[i-1]:
                nums[i] = num
                i += 1
            heapq.heappush(heap, [prime*nums[idx+1], prime, idx+1])
        return nums[n-1]


    # O(M*N) is TLE, maybe good enough
    def nthSuperUglyNumber_DP_TLE(self, n: int, primes: List[int]) -> int:
        times = [0]*len(primes)
        res = [1]
        for _ in range(n-1):
            minVal = float('inf')
            for i, p in zip(times, primes):
                minVal = min(minVal, res[i]*p)
            res.append(minVal)
            for i in range(len(times)):
                if minVal == res[times[i]]*primes[i]:
                    times[i] += 1
        return res[-1]


    def test(self):
        test_cases = [
            [12, [2,7,13,19]],
            [1, [2,3,5]],
        ]
        for n, primes in test_cases:
            res1 = self.nthSuperUglyNumber(n, primes)
            res2 = self.nthSuperUglyNumber_DP_TLE(n, primes)
            print('res1: %s' % res1)
            print('res2: %s' % res2)
            print('-='*30 + '-')


if __name__ == '__main__':
    Solution().test()
