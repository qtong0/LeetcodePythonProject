class Cashier:

    def __init__(self, n: int, discount: int, products, prices):
        self.count = 0
        self.n = n
        self.discount = discount
        self.priceMap = {}
        for product, price in zip(products, prices):
            self.priceMap[product] = price


    def getBill(self, product, amount) -> float:
        self.count += 1
        totalPrice = 0
        for p, a in zip(product, amount):
            totalPrice += a*self.priceMap[p]
        if self.count % self.n == 0:
            totalPrice = totalPrice - totalPrice*self.discount/100
        return totalPrice


# Your Cashier object will be instantiated and called as such:
# obj = Cashier(n, discount, products, prices)
# param_1 = obj.getBill(product,amount)
