import heapq


class KthLargest(object):

    def __init__(self, k, nums):
        """
        :type k: int
        :type nums: List[int]
        """
        self.heap1 = []
        self.heap2 = []
        self.k = k
        for num in nums:
            heapq.heappush(self.heap1, -num)
        for _ in range(k-1):
            val = heapq.heappop(self.heap1)
            heapq.heappush(self.heap2, -val)

    def add(self, val):
        """
        :type val: int
        :rtype: int
        """
        if not self.heap1 or val >= -self.heap1[0]:
            heapq.heappush(self.heap2, val)
            while len(self.heap2) > self.k-1:
                val = heapq.heappop(self.heap2)
                heapq.heappush(self.heap1, -val)
        else:
            heapq.heappush(self.heap1, -val)
            while len(self.heap2) < self.k-1:
                val = heapq.heappop(self.heap1)
                heapq.heappush(self.heap2, -val)
        return -self.heap1[0]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)

if __name__ == '__main__':
    l = KthLargest(3,[4,5,8,2])
    print(l.add(3))
    print(l.add(5))
    print(l.add(10))
    print(l.add(9))
    print(l.add(4))

    print('-='*30+'-')
    l = KthLargest(3, [5,-1])
    print(l.add(2))
    print(l.add(1))
    print(l.add(-1))
    print(l.add(3))
    print(l.add(4))
