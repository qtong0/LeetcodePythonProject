from typing import List
import random
import bisect


class MajorityChecker:

    def __init__(self, arr: List[int]):
        hashmap = {}
        for i, num in enumerate(arr):
            hashmap[num] = hashmap.get(num, []) + [i]
        self.arr = arr
        self.hashmap = hashmap

    # Random pick 20 times, because there are at most 10^4 queries and 2^20 is much larger
    # O(20*Log(N)) same as O(LogN*LogN)
    # just need to pick k times and then let 2^k >> n
    def query(self, left: int, right: int, threshold: int) -> int:
        for _ in range(20):
            a = self.arr[random.randint(left, right)]
            l = bisect.bisect_left(self.hashmap[a], left)
            r = bisect.bisect_right(self.hashmap[a], right)
            if r - l >= threshold:
                return a
        return -1


# Your MajorityChecker object will be instantiated and called as such:
# obj = MajorityChecker(arr)
# param_1 = obj.query(left,right,threshold)


if __name__ == '__main__':
    obj = MajorityChecker([1, 1, 2, 2, 1, 1])
    print(obj.query([0, 5, 4]))
    print(obj.query([0, 3, 3]))
    print(obj.query([2, 3, 2]))
