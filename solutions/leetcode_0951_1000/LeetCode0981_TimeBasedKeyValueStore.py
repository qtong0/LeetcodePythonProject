import bisect


class TimeMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.hashmap = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.hashmap:
            self.hashmap[key] = [(timestamp, value)]
        else:
            idx = self.find(self.hashmap[key], timestamp)
            self.hashmap[key].insert(idx, (timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key in self.hashmap:
            arr = self.hashmap[key]
            idx = self.find(arr, timestamp)
            if idx < len(arr) and arr[idx][0] == timestamp:
                return arr[idx][1]
            elif idx > 0:
                return arr[idx-1][1]
            else:
                return ''
        else:
            return ''

    def find(self, arr, timestamp):
        return bisect.bisect_left(arr, (timestamp, ''))

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
