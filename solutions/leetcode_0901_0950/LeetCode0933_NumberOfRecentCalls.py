class RecentCounter(object):

    def __init__(self):
        self.deque = []

    def ping(self, t):
        """
        :type t: int
        :rtype: int
        """
        self.deque.append(t)
        while self.deque and t-self.deque[0] > 3000:
            self.deque.pop(0)
        return len(self.deque)


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)
