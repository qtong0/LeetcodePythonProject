class Solution:
    def countTriplets(self, A) -> int:
        if not A:return 0
        n = len(A)
        res = 0
        hashmap = {}
        for i in range(n):
            for j in range(n):
                v = A[i] & A[j]
                hashmap[v] = hashmap.get(v, 0)+1
        for i in range(n):
            for v, count in hashmap.items():
                if v & A[i] == 0:
                    res += hashmap[v]
        return res
