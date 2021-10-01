import bisect


class SnapshotArray(object):

    def __init__(self, length: int):
        self.arr = [[[-1, 0]] for _ in range(length)]
        self.snap_id = 0

    def set(self, index: int, val: int) -> None:
        self.arr[index].append([self.snap_id, val])

    def snap(self) -> int:
        self.snap_id += 1
        return self.snap_id - 1

    def get(self, index: int, snap_id: int) -> int:
        i = bisect.bisect_left(self.arr[index], [snap_id+1]) - 1
        return self.arr[index][i][1]

# use Java TreeMap Instead

"""

class SnapshotArray {

    TreeMap<Integer, Integer>[] snap;
    int numSnaps = 0;

    public SnapshotArray(int length) {
        snap = new TreeMap[length];
        for(int i = 0; i < length; i++) {
            snap[i] = new TreeMap<>();
        }
    }

    public void set(int index, int val) {
        snap[index].put(numSnaps, val);
    }

    public int snap() {
        return numSnaps++;
    }

    public int get(int index, int snap_id) {
        Integer val = snap[index].get(snap_id);
        if (val != null) return val;

        Integer earlierSnapId = snap[index].lowerKey(snap_id);
        if (earlierSnapId != null) {
            return snap[index].get(earlierSnapId);
        }
        return 0;
    }

}

"""

# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)
