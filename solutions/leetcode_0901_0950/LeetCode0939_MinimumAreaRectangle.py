class Solution(object):
    def minAreaRect(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        hashmapx, hashmapy = {}, {}
        for x, y in points:
            hashmapx[x] = hashmapx.get(x, []) + [y]
            hashmapy[y] = hashmapy.get(y, []) + [x]
        res = float('inf')
        for x, arr in hashmapx.items():
            if len(arr) >= 2:
                n = len(arr)
                for i in range(n):
                    for j in range(i):
                        y1, y2 = arr[i], arr[j]
                        common = set(hashmapy[y1]) & set(hashmapy[y2])
                        if common:
                            for x2 in common:
                                if x2 != x:
                                    res = min(res, abs(x2-x)*abs(y2-y1))
        return res if res != float('inf') else 0
