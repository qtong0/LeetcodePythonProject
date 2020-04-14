import bisect


class ExamRoom(object):

    def __init__(self, N):
        """
        :type N: int
        """
        self.rowNum = N
        self.arr = []

    def seat(self):
        """
        :rtype: int
        """
        if not self.arr:
            res = 0
        else:
            d, res = self.arr[0], 0
            for i in range(0, len(self.arr)-1):
                a, b = self.arr[i], self.arr[i+1]
                if (b-a)//2 > d:
                    d, res = (b-a)//2, (b+a)//2
            if self.rowNum - 1 - self.arr[-1] > d:
                res = self.rowNum-1
        # bisect.insort(self.l, res)
        self.bisect_insort(self.arr, res)
        return res

    def bisect_insort(self, arr, res):
        l, r = 0, len(arr)
        while l < r:
            mid = (l+r)//2
            if arr[mid] <= res:
                l = mid+1
            else:
                r = mid
        arr.insert(l, res)

    def leave(self, p):
        """
        :type p: int
        :rtype: None
        """
        self.arr.remove(p)

# Your ExamRoom object will be instantiated and called as such:
# obj = ExamRoom(N)
# param_1 = obj.seat()
# obj.leave(p)


if __name__ == '__main__':
    examRoom = ExamRoom(10)
    print(examRoom.seat())
    print(examRoom.seat())
    print(examRoom.seat())
    print(examRoom.seat())
    examRoom.leave(4)
    print(examRoom.seat())
