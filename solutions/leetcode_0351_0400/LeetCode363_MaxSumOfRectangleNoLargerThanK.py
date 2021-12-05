class Solution(object):
    def maxSumSubmatrix(self, matrix, k):
        pass
    
    # still not working!
    def maxSumSubmatrixBinarySearch(self, matrix, k):
        import bisect
        if not matrix or not matrix[0]:
            return 0
        m, n = len(matrix), len(matrix[0])
        areas = [[0]*n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0: areas[i][j] = matrix[i][j]
                if i == 0 and j != 0: areas[i][j] = matrix[i][j]+areas[i][j-1]
                if i != 0 and j == 0: areas[i][j] = matrix[i][j]+areas[i-1][j]
                if i != 0 and j != 0:
                    areas[i][j] = areas[i][j-1]+areas[i-1][j]+areas[i-1][j-1]+matrix[i][j]
        maxVal = float('-inf')
        for r1 in range(m):
            for r2 in range(r1, m):
                sortedlist = [0]
                for c in range(n):
                    area = areas[r2][c]
                    if r1-1>=0:
                        area -= areas[r2][c]
                    ind = bisect.bisect_left(sortedlist, area-k)
                    if ind < len(sortedlist):
                        maxVal = max(maxVal, area-sortedlist[ind])
                    bisect.insort_left(sortedlist, area)
        return maxVal

"""

class Solution {
    // TreeMap solution
    public int maxSumSubmatrix(int[][] matrix, int k) {
		if (matrix == null || matrix.length == 0 || matrix[0].length == 0)
			return 0;
		int rows = matrix.length;
		int cols = matrix[0].length;
		int[][] areas = new int[rows][cols];
		for (int r = 0; r < rows; r++) {
			for (int c = 0; c < cols; c++) {
				int area = matrix[r][c];
				if (r-1 >= 0) {
					area += areas[r-1][c];
				}
				if (c-1 >= 0) {
					area += areas[r][c-1];
				}
				if (r-1 >= 0 && c-1 >= 0) {
					area -= areas[r-1][c-1];
				}
				areas[r][c] = area;
			}
		}
		int max = Integer.MIN_VALUE;
		for (int r1 = 0; r1 < rows; r1++) {
			for (int r2 = r1; r2 < rows; r2++) {
				TreeSet<Integer> tree = new TreeSet<>();
				tree.add(0);
				for (int c = 0; c < cols; c++) {
					int area = areas[r2][c];
					if (r1-1 >= 0) {
						area -= areas[r1-1][c];
					}
					Integer ceiling = tree.ceiling(area-k);
					if (ceiling != null) {
						max = Math.max(max, area-ceiling);
					}
					tree.add(area);
				}
			}
		}
		return max;
	}
    
    // Merge Sort solution!
    public int maxSumSubmatrix_mergeSort(int[][] matrix, int k) {
		int m = matrix.length;
		int n = matrix[0].length;
		int res = Integer.MIN_VALUE;
		long[] sum = new long[m+1];
		for (int i = 0; i < n; i++) {
			long[] sumInRow = new long[m];
			for (int j = i; j < n; j++){
				for (int p = 0; p < m; p++) {
					sumInRow[p] += matrix[p][j];
					sum[p+1] = sum[p]+sumInRow[p];
				}
				res = Math.max(res, mergeSort(sum, 0, m+1, k));
				if (res == k) return k;
			}
		}
		return res;
    }
	
	private int mergeSort(long[] sum, int start, int end, int k) {
		if (end == start+1) return Integer.MIN_VALUE;
		int mid = start + (end-start)/2;
		int cnt = 0;
		int ans = mergeSort(sum, start, mid, k);
		if (ans==k) return k;
		ans = Math.max(ans,  mergeSort(sum, mid, end, k));
		if (ans==k) return k;
		long[] cache = new long[end-start];
		for (int i = start, j = mid, p = mid; i < mid; i++) {
			while (j < end && sum[j] - sum[i] <= k) j++;
			if (j-1 >= mid) {
				ans = Math.max(ans, (int)(sum[j-1]-sum[i]));
				if (ans == k) return k;
			}
			while (p < end && sum[p] < sum[i]) {
				cache[cnt++] = sum[p++];
			}
			cache[cnt++] = sum[i];
		}
		System.arraycopy(cache, 0, sum, start, cnt);
		return ans;
	}
}

"""