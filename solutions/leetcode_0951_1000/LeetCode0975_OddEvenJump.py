class Solution:
    def oddEvenJumps(self, A) -> int:
        pass

# Checkout Java TreeMap solution:


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
