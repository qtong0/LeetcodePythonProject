class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        sumVal = 0
        product = 1
        while n > 0:
            d = n % 10
            n //= 10
            sumVal += d
            product *= d
        return product-sumVal
