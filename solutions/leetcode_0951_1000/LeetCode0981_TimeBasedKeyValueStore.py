class TimeMap:

    def __init__(self):
        self.hashmap = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.hashmap:
            self.hashmap[key] = [(timestamp, value)]
        else:
            self.hashmap[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key in self.hashmap:
            arr = self.hashmap[key]
            n = len(arr)
            l, r = 0, n
            while l < r:
                mid = (l+r) // 2
                if arr[mid][0] <= timestamp:
                    l = mid+1
                else:
                    r = mid
            return '' if r == 0 else arr[r-1][1]
        else:
            return ''

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)


if __name__ == '__main__':
    tm = TimeMap()
    tm.set('foo', 'bar', 1)
    print(tm.get('foo', 1))
    print(tm.get('foo', 3))
    tm.set('foo', 'bar2', 4)
    print(tm.get('foo', 4))
    print(tm.get('foo', 5))
