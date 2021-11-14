from collections import defaultdict
from typing import List


class DetectSquares:

    def __init__(self):
        self.xmap = defaultdict(list)
        self.cnt = defaultdict(int)


    def add(self, point: List[int]) -> None:
        x, y = point
        self.xmap[x].append(y)
        self.cnt[(x, y)] += 1


    def count(self, point: List[int]) -> int:
        x1, y1 = point
        res = 0
        for y2 in self.xmap[x1]:
            if y2 == y1:
                continue
            sideLen = abs(y2 - y1)

            # Case: p3, p4 points are on the left side
            x3, y3 = x1 - sideLen, y2
            x4, y4 = x1 - sideLen, y1
            res += self.cnt[(x3, y3)] * self.cnt[(x4, y4)]

            # Case: p3, p4 points are on the right side
            x3, y3 = x1 + sideLen, y2
            x4, y4 = x1 + sideLen, y1
            res += self.cnt[(x3, y3)] * self.cnt[(x4, y4)]

        return res


# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)


if __name__ == '__main__':
    ds = DetectSquares()
    ds.add([3, 10])
    ds.add([11, 2])
    ds.add([3, 2])
    print(ds.count([11, 10]))
    print(ds.count([14, 8]))
    ds.add([11, 2])
    print(ds.count([11, 10]))
