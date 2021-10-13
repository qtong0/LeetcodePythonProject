from typing import List
import bisect

"""
### !!! JAVA TreeMap Solution !!! ###

public int jobScheduling(int[] startTime, int[] endTime, int[] profit) {
    int n = startTime.length;
    int[][] jobs = new int[n][3];
    for(int i = 0; i < n; i++) {
        jobs[i] = new int[] {startTime[i], endTime[i], profit[i]};
    }
    Arrays.sort(jobs, (a, b) -> a[1]-b[1]);
    TreeMap<Integer, Integer> dp = new TreeMap<>();
    dp.put(0, 0);
    for (int[] job: jobs) {
        int cur = dp.floorEntry(job[0]).getValue() + job[2];
        if (cur > dp.lastEntry().getValue()) {
            dp.put(job[1], cur);
        }
    }
    return dp.lastEntry().getValue();
}

"""

class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        arr = sorted(zip(startTime, endTime, profit), key=lambda v: v[1])
        dp = [[0, 0]]
        for s, e, p in arr:
            i = bisect.bisect(dp, [s+1]) - 1
            if dp[i][1] + p > dp[-1][1]:
                dp.append([e, dp[i][1] + p])
        return dp[-1][1]


    # Own DFS only, WORST SOLUTION
    def jobScheduling_DFS_SLOWEST(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        arr = sorted([s, e, p] for s, e, p in zip(startTime, endTime, profit))
        return self.dfs(arr, 0, 0)

    def dfs(self, arr, curr_profit, idx):
        if idx >= len(arr):
            return curr_profit
        s, e, p = arr[idx]
        j = idx+1
        while j < len(arr) and arr[j][0] < e:
            j += 1
        res = curr_profit
        res = max(res, p + self.dfs(arr, curr_profit, j))
        res = max(res, self.dfs(arr, curr_profit, idx+1))
        return res

    def test(self):
        test_cases = [
            [[1,2,3,3], [3,4,5,6], [50,10,40,70]],
            [[1,2,3,4,6], [3,5,10,6,9], [20,20,100,70,60]],
            [[1,2,3,3], [3,4,5,6], [50,10,40,70]],
            [[1,1,1], [2,3,4], [5,6,4]],
        ]
        for startTime, endTime, profit in test_cases:
            res = self.jobScheduling(startTime, endTime, profit)
            print('res: %s' % res)
            print('-='*30 + '-')


if __name__ == '__main__':
    Solution().test()
