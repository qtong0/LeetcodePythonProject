from typing import List
import collections


class Solution:
    def isPossibleDivide(self, nums: List[int], k: int) -> bool:
        c = collections.Counter(nums)
        start = []
        last_checked, opened = -1, 0
        for i in sorted(c):
            if opened > c[i] or opened > 0 and i > last_checked + 1:
                return False
            start.append(c[i] - opened)
            last_checked, opened = i, c[i]
            if len(start) == k:
                opened -= start.pop(0)
        return opened == 0

    """
    ### Java TreeMap Solution! ###
    
    public boolean isPossibleDivide(int[] nums, int k) {
        Map<Integer, Integer> counter = new TreeMap<>();
        for (int num: nums) {
            counter.put(num, counter.getOrDefault(num, 0) + 1);
        }
        Queue<Integer> start = new LinkedList<>();
        int last_checked = -1, opened = 0;
        for (int num: counter.keySet()) {
            if ((opened > 0 && num > last_checked + 1) || opened > counter.get(num)) {
                return false;
            }
            start.add(counter.get(num) - opened);
            last_checked = num;
            opened = counter.get(num);
            if (start.size() == k) {
                opened -= start.remove();
            }
        }
        return opened == 0;
    }
    
    """


    def isPossibleDivide_own_TLE(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        if n % k != 0:
            return False
        nums.sort()
        m = n//k
        dp = [[None, 0] for _ in range(m)]
        for num in nums:
            i = 0
            while i < m and dp[i][0] and (dp[i][0] != num-1 or dp[i][1] == k):
                i += 1
            if i < m:
                dp[i][1] += 1
                dp[i][0] = num
            else:
                return False
        return True

    def test(self):
        test_cases = [
            [[1,2,3,3,4,4,5,6], 4],
            [[3,2,1,2,3,4,3,4,5,9,10,11], 3],
            [[3,3,2,2,1,1], 3],
            [[1,2,3,4], 3],
        ]
        for nums, k in test_cases:
            res = self.isPossibleDivide(nums, k)
            print('res: %s' % res)
            print('-='*30+'-')


if __name__ == '__main__':
    Solution().test()
