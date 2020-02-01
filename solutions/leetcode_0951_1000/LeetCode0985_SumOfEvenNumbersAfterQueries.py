class Solution:
    def sumEvenAfterQueries(self, A, queries):
        res = []
        sumVal = sum(num for num in A if num % 2 == 0)
        for val, idx in queries:
            if A[idx] % 2 == 0:
                sumVal -= A[idx]
            A[idx] += val
            if A[idx] % 2 == 0:
                sumVal += A[idx]
            res.append(sumVal)
        return res
