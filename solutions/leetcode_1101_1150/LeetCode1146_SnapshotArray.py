class SnapshotArray(object):

    def __init__(self, length: int):
        pass

    def set(self, index: int, val: int) -> None:
        pass

    def snap(self) -> int:
        pass

    def get(self, index: int, snap_id: int) -> int:
        pass

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
