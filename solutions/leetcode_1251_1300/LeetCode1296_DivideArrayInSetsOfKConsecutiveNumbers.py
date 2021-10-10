from typing import List
import collections


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


class Solution:
    # Time O(MlogM + MK), M is the number of different cards
    # Easier to understand
    def isPossibleDivide(self, nums: List[int], k: int) -> bool:
        c = collections.Counter(nums)
        for i in sorted(c):
            if c[i] > 0:
                for j in range(k-1, -1, -1):
                    c[i+j] -= c[i]
                    if c[i+j] < 0:
                        return False
        return True


    # In case of K is really big
    def isPossibleDivide_best(self, nums: List[int], k: int) -> bool:
        c = collections.Counter(nums)
        # Need to close queue means that: When the queue size exceeds K,
        # the value poll from the queue tells us how many consecutive sequences we need to close. Example:
        # if A is [2,2,2,3,3,3,3, (no 3 afterward) ...] and k = 2
        # freqMap: {
        #      2: 3
        #      3: 4 -> Pay attention here
        #      ...
        # }
        # Inside the freqMap, at entry with value 3,
        # we will add 1 into the queue because 3 has 1 extra frequency count,
        # and sometimes later on in the future, we will need to close that one sequence.
        need_to_close = []
        # to_take_in means that the frequency count that it is ready to take in for the next consecutive number.
        # If the size of needToClose queue exceeds K,
        # to_take_in may decrease because it needs to save some of its frequency count for the closing sequence.
        last_checked, to_take_in = -1, 0
        for i in sorted(c):
            if to_take_in > c[i] or to_take_in > 0 and i > last_checked + 1:
                return False
            need_to_close.append(c[i] - to_take_in)
            last_checked, to_take_in = i, c[i]
            if len(need_to_close) == k:
                to_take_in -= need_to_close.pop(0)
        return to_take_in == 0


    # My own solution, it's too slow, TLE :(
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
