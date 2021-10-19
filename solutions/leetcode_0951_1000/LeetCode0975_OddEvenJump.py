from typing import List


class Solution:
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
public class LeetCode0975_OddEvenJump {
    public int oddEvenJumps(int[] A) {
        int n = A.length;
        if (n <= 1) return n;
        boolean[] odd = new boolean[n];
        boolean[] even = new boolean[n];
        odd[n-1] = even[n-1] = true;

        TreeMap<Integer, Integer> vals = new TreeMap();
        vals.put(A[n-1], n-1);
        for (int i = n-2; i >= 0; i--) {
            int v = A[i];
            if (vals.containsKey(v)) {
                odd[i] = even[vals.get(v)];
                even[i] = odd[vals.get(v)];
            } else {
                Integer lower = vals.lowerKey(v);
                Integer higher = vals.higherKey(v);
                if (lower != null) {
                    even[i] = odd[vals.get(lower)];
                }
                if (higher != null) {
                    odd[i] = even[vals.get(higher)];
                }
            }
            vals.put(v, i);
        }
        int res = 0;
        for (boolean b: odd) {
            if (b) res++;
        }
        return res;
    }
}

"""



if __name__ == '__main__':
    Solution().test()
