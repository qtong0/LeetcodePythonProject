import bisect


class RangeModule(object):

    def __init__(self):
        # self.X is a sorted list of coorditations used by add/remove
        self.X = [0, 10**9]
        # self.track is tracking where it might start / stop
        self.track = [False]*2

    def addRangeHelper(self, left, right, track=True):
        def index(x):
            i = bisect.bisect_left(self.X, x)
            if self.X[i] != x:
                self.X.insert(i, x)
                self.track.insert(i, self.track[i-1])
            return i
        i = index(left)
        j = index(right)
        self.X[i:j] = [left]
        self.track[i:j] = [track]

    def addRange(self, left: int, right: int) -> None:
        self.addRangeHelper(left, right, True)

    def queryRange(self, left: int, right: int) -> bool:
        i = bisect.bisect(self.X, left)-1
        j = bisect.bisect_left(self.X, right)
        return all(self.track[i:j])

    def removeRange(self, left: int, right: int) -> None:
        self.addRangeHelper(left, right, False)


class RangeModule_another(object):

    def __init__(self):
        self.track = []

    def addRange(self, left: int, right: int) -> None:
        start = bisect.bisect_left(self.track, left)
        end = bisect.bisect_right(self.track, right)

        subtrack = []
        if start % 2 == 0:
            subtrack.append(left)
        if end % 2 == 0:
            subtrack.append(right)

        self.track[start:end] = subtrack

    def queryRange(self, left: int, right: int) -> bool:
        start = bisect.bisect_right(self.track, left)
        end = bisect.bisect_left(self.track, right)

        return start == end and start % 2 == 1

    def removeRange(self, left: int, right: int) -> None:
        start = bisect.bisect_left(self.track, left)
        end = bisect.bisect_right(self.track, right)

        subtrack = []
        if start % 2 == 1:
            subtrack.append(left)
        if end % 2 == 1:
            subtrack.append(right)

        self.track[start:end] = subtrack


if __name__ == '__main__':
    rangeModule = RangeModule()
    print(rangeModule.addRange(55,62))
    print(rangeModule.addRange(1,29))

    l = [1,2,3,4]
    print(l[1:3])
    l[1:3] = [False]
    print(l)

