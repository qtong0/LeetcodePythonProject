from sortedcontainers import SortedDict


# Two TreeMaps
# TC: O(N*Log(N))
# SC: O(N)
#
class StockPrice:

    def __init__(self):
        self.tpdict = SortedDict()
        self.ptdict = SortedDict()

    def update(self, timestamp: int, price: int) -> None:
        if timestamp not in self.tpdict:
            self.tpdict[timestamp] = price
            if price not in self.ptdict:
                self.ptdict[price] = set()
            self.ptdict[price].add(timestamp)
        else:
            prevp = self.tpdict[timestamp]
            self.tpdict[timestamp] = price
            self.ptdict[prevp].remove(timestamp)
            if not self.ptdict[prevp]:
                del self.ptdict[prevp]
            if price not in self.ptdict:
                self.ptdict[price] = set()
            self.ptdict[price].add(timestamp)

    def current(self) -> int:
        return self.tpdict.peekitem(-1)[1]

    def maximum(self) -> int:
        return self.ptdict.peekitem(-1)[0]

    def minimum(self) -> int:
        return self.ptdict.peekitem(0)[0]


"""
// Java Version

public class LeetCode2034_StockPriceFluctuation {
    TreeMap<Integer, Integer> tpMap;
    TreeMap<Integer, Set<Integer>> ptMap;

    public LeetCode2034_StockPriceFluctuation() {
        tpMap = new TreeMap<>();
        ptMap = new TreeMap<>();
    }

    public void update(int timestamp, int price) {
        if (tpMap.containsKey(timestamp)) {
            int prevPrice = tpMap.get(timestamp);
            Set<Integer> priceSet = ptMap.get(prevPrice);
            priceSet.remove(timestamp);
            if (priceSet.isEmpty()) {
                ptMap.remove(prevPrice);
            }
        }
        ptMap.putIfAbsent(price, new HashSet<>());
        ptMap.get(price).add(timestamp);
        tpMap.put(timestamp, price);
    }

    public int current() {
        return tpMap.lastEntry().getValue();
    }

    public int maximum() {
        return ptMap.lastKey();
    }

    public int minimum() {
        return ptMap.firstKey();
    }

}

"""

# Your StockPrice object will be instantiated and called as such:
# obj = StockPrice()
# obj.update(timestamp,price)
# param_2 = obj.current()
# param_3 = obj.maximum()
# param_4 = obj.minimum()


if __name__ == '__main__':
    obj = StockPrice()
    obj.update(1, 10)
    obj.update(2, 5)
    print(obj.current())
    print(obj.maximum())
    obj.update(1, 3)
    print(obj.maximum())
    obj.update(4, 2)
    print(obj.minimum())
