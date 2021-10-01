import bisect


class RangeModule(object):

    def __init__(self):
        self.X = [0, 10**9]
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
    print(rangeModule.removeRange(18,49))
    print(rangeModule.queryRange(6,98))
    print(rangeModule.queryRange(59,71))
    print(rangeModule.removeRange(40,45))
    print(rangeModule.removeRange(4,58))
    print(rangeModule.removeRange(57,69))
    print(rangeModule.removeRange(20,30))
    print(rangeModule.removeRange(1,40))
    print(rangeModule.queryRange(73,93))
    print(rangeModule.removeRange(32,93))
    print(rangeModule.addRange(38,100))
    print(rangeModule.removeRange(50,64))
    print(rangeModule.addRange(26,72))
    print(rangeModule.queryRange(8,74))
    print(rangeModule.queryRange(15,53))
    print(rangeModule.addRange(44,85))
    print(rangeModule.addRange(10,71))
    print(rangeModule.queryRange(54,70))
    print(rangeModule.removeRange(10,45))
    print(rangeModule.queryRange(30,66))
    print(rangeModule.addRange(47,98))
    print(rangeModule.queryRange(1,7))
    print(rangeModule.removeRange(44,78))
    print(rangeModule.removeRange(31,49))
    print(rangeModule.addRange(62,63))
    print(rangeModule.addRange(49,88))
    print(rangeModule.removeRange(47,72))
    print(rangeModule.removeRange(8,50))
    print(rangeModule.removeRange(49,79))
    print(rangeModule.addRange(31,47))
    print(rangeModule.addRange(54,87))
    print(rangeModule.queryRange(77,78))
    print(rangeModule.queryRange(59,100))
    print(rangeModule.queryRange(8,9))
    print(rangeModule.queryRange(50,51))
    print(rangeModule.queryRange(67,93))
    print(rangeModule.removeRange(25,86))
    print(rangeModule.removeRange(8,92))
    print(rangeModule.queryRange(31,87))
    print(rangeModule.addRange(90,95))
    print(rangeModule.addRange(28,56))
    print(rangeModule.addRange(10,42))
    print(rangeModule.queryRange(27,34))
    print(rangeModule.addRange(75,81))
    print(rangeModule.addRange(17,63))
    print(rangeModule.removeRange(78,90))
    print(rangeModule.addRange(9,18))
    print(rangeModule.queryRange(51,74))
    print(rangeModule.removeRange(20,54))
    print(rangeModule.addRange(35,72))
    print(rangeModule.queryRange(2,29))
    print(rangeModule.addRange(28,41))
    print(rangeModule.addRange(17,95))
    print(rangeModule.addRange(73,75))
    print(rangeModule.queryRange(34,43))
    print(rangeModule.addRange(57,96))
    print(rangeModule.queryRange(51,72))
    print(rangeModule.removeRange(21,67))
    print(rangeModule.removeRange(40,73))
    print(rangeModule.removeRange(14,26))
    print(rangeModule.removeRange(71,86))
    print(rangeModule.queryRange(34,41))
    print(rangeModule.removeRange(10,25))
    print(rangeModule.queryRange(27,68))
    print(rangeModule.queryRange(18,32))
    print(rangeModule.removeRange(30,31))
    print(rangeModule.queryRange(45,61))
    print(rangeModule.addRange(64,66))
    print(rangeModule.addRange(18,93))
    print(rangeModule.queryRange(13,21))
    print(rangeModule.removeRange(13,46))
    print(rangeModule.removeRange(56,99))
    print(rangeModule.queryRange(6,93))
    print(rangeModule.addRange(25,36))
    print(rangeModule.removeRange(27,88))
    print(rangeModule.removeRange(82,83))
    print(rangeModule.addRange(30,71))
    print(rangeModule.addRange(31,73))
    print(rangeModule.addRange(10,41))
    print(rangeModule.queryRange(71,72))
    print(rangeModule.queryRange(9,56))
    print(rangeModule.addRange(22,76))
    print(rangeModule.queryRange(38,74))
    print(rangeModule.removeRange(2,77))
    print(rangeModule.queryRange(33,61))
    print(rangeModule.removeRange(74,75))
    print(rangeModule.addRange(11,43))
    print(rangeModule.queryRange(27,75))
