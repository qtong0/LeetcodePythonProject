import collections


class Solution(object):
    def largestComponentSize(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        B = []
        for num in A:
            facs = []
            d = 2
            while d * d <= num:
                if num % d == 0:
                    while num % d == 0:
                        num //= d
                    facs.append(d)
                d += 1
            if num > 1 or not facs:
                facs.append(num)
            B.append(facs)

        primes = list({p for facs in B for p in facs})
        prime_to_index = {p: i for i, p in enumerate(primes)}

        n = len(primes)
        roots = list(range(n))
        for facs in B:
            for num in facs:
                root1 = self.find(roots, prime_to_index[facs[0]])
                root2 = self.find(roots, prime_to_index[num])
                roots[root1] = root2
        count = collections.Counter(self.find(roots, prime_to_index[facs[0]]) for facs in B)
        return max(count.values())

    def find(self, roots, node):
        while roots[node] != node:
            node = roots[node]
        return node

    def test(self):
        testCases = [
            [2,3,6,7,4,12,21,39],
            [1,2,3,4,5,6,7,8,9],
        ]
        for arr in testCases:
            res = self.largestComponentSize(arr)
            print('res: %s' % res)
            print('-='*30 + '-')


if __name__ == '__main__':
    Solution().test()
