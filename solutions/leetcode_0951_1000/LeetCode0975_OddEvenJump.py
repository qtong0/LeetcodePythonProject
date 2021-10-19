from typing import List


class Solution:
    # O(N*log(N))
    def oddEvenJumps(self, arr: List[int]) -> int:
        n = len(arr)
        next_higher, next_lower = [0]*n, [0]*n

        stack = []
        for a, i in sorted([a, i] for i, a in enumerate(arr)):
            while stack and stack[-1] < i:
                next_higher[stack.pop()] = i
            stack.append(i)

        stack = []
        for a, i in sorted([-a, i] for i, a in enumerate(arr)):
            while stack and stack[-1] < i:
                next_lower[stack.pop()] = i
            stack.append(i)

        higher, lower = [0]*n, [0]*n
        higher[-1] = lower[-1] = 1
        for i in range(n-2, -1, -1):
            higher[i] = lower[next_higher[i]]
            lower[i] = higher[next_lower[i]]
        return sum(higher)



    def test(self):
        test_cases = [
            [10,13,12,14,15],
            [2,3,1,1,4],
        ]
        for arr in test_cases:
            res = self.oddEvenJumps(arr)
            print('res: %s' % res)
            print('-='*30 + '-')



# Another solution is using TreeMap:

"""
    public int oddEvenJumps(int[] arr) {
        int n = arr.length;
        int res = 1;
        boolean higher[] = new boolean[n];
        boolean lower[] = new boolean[n];
        higher[n-1] = lower[n-1] = true;
        TreeMap<Integer, Integer> treeMap = new TreeMap<>();
        treeMap.put(arr[n-1], n-1);
        for(int i = n-2; i >= 0; i--) {
            Map.Entry<Integer, Integer> hi = treeMap.ceilingEntry(arr[i]);
            Map.Entry<Integer, Integer> lo = treeMap.floorEntry(arr[i]);
            if (hi != null) {
                higher[i] = lower[(int)hi.getValue()];
            }
            if (lo != null) {
                lower[i] = higher[(int)lo.getValue()];
            }
            if (higher[i]) {
                res++;
            }
            treeMap.put(arr[i], i);
        }
        return res;
    }
"""



if __name__ == '__main__':
    Solution().test()
