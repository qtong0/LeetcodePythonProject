# Brief explanation. Record the prefix for multiplication and summation.
#
# when we look at a number x,
# for example,
# append x, add a1, mul b1, add a2, mul b2, add a3, mul b3
# (((x + a1) * b1 + a2) * b2 + a3) * b3
# for the final value of x, it doesn't matter if we appended other numbers of not.
#
# Let's expand it, we have
# b1 * b2 * b3 * x + b1 * b2 * b3 * a1 + b2 * b3 * a2 + b3 * a3
#
# so a1 is the inc when we first see the number!
# when we multiply b1 after a1, the output of the term a1 should also be multiplied by b1,
# but how do we get b1? It is calculated by (b1 * b2 * b3) // (b2 * b3) as recorded in the prefix multiplications.
#
class Fancy:

    def __init__(self):
        self.arr = []
        self.add = [0]
        self.mul = [1]


    def append(self, val: int) -> None:
        self.arr.append(val)
        self.add.append(self.add[-1])
        self.mul.append(self.mul[-1])


    def addAll(self, inc: int) -> None:
        self.add[-1] += inc


    def multAll(self, m: int) -> None:
        self.add[-1] = self.add[-1] * m % (10 ** 9 + 7)
        self.mul[-1] = self.mul[-1] * m % (10 ** 9 + 7)


    def getIndex(self, idx: int) -> int:
        if idx >= len(self.arr):
            return -1
        MOD = 10 ** 9 + 7
        m = self.mul[-1] * pow(self.mul[idx], MOD-2, MOD)
        inc = self.add[-1] - self.add[idx] * m
        return (self.arr[idx] * m + inc) % MOD



# Your Fancy object will be instantiated and called as such:
# obj = Fancy()
# obj.append(val)
# obj.addAll(inc)
# obj.multAll(m)
# param_4 = obj.getIndex(idx)
