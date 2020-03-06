import heapq


class Solution(object):
    def kthSmallestPrimeFraction(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: List[int]
        """
        # Use Java PriorityQueue comparator
        pq = [(A[0] / float(A[i]), 0, i) for i in range(len(A) - 1, 0, -1)]

        for _ in range(K-1):
            frac, i, j = heapq.heappop(pq)
            i += 1
            if i < j:
                heapq.heappush(pq, (A[i] / float(A[j]), i, j))

        return A[pq[0][1]], A[pq[0][2]]

    def test(self):
        testCases = [
            [ [1, 2, 3, 5], 3 ],
            [ [1, 7], 1 ],
        ]
        for arr, k in testCases:
            print('arr: %s' % arr)
            print('k: %s' % k)
            res = self.kthSmallestPrimeFraction(arr, k)
            print('res: %s' % list(res))
            print('-='*30+'-')

"""

class Solution {
    public int[] kthSmallestPrimeFraction(int[] A, int K) {
        int[] arr = A;
		int n = arr.length;
        PriorityQueue<int[]> pq = new PriorityQueue<>(new Comparator<int[]>(){
        	@Override
        	public int compare(int[] o1, int[] o2) {
        		int s1 = arr[o1[0]]*arr[o2[1]];
        		int s2 = arr[o2[0]]*arr[o1[1]];
        		return s1-s2;
        	}
        });
        for (int i = 0; i < n-1; i++) {
        	pq.add(new int[] {i, n-1});
        }
        for (int i = 0; i < K-1; i++) {
        	int[] pop = pq.remove();
        	if (pop[1]-1 > pop[0]) {
        		pop[1]--;
        		pq.add(pop);
        	}
        }
        int[] peek = pq.peek();
        return new int[]{arr[peek[0]], arr[peek[1]]};
    }
}

"""


if __name__ == '__main__':
    Solution().test()
