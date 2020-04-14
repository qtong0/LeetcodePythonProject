import heapq

class SummaryRanges:

    def __init__(self):
        self.intervals = []

    def addNum(self, val):
        heapq.heappush(self.intervals, (val, [val, val]))

    def getIntervals(self):
        stack = []
        while self.intervals:
            idx, cur = heapq.heappop(self.intervals)
            if not stack:
                stack.append((idx, cur))
            else:
                _, prev = stack[-1]
                if prev[1] + 1 >= cur[0]:
                    prev[1] = max(prev[1], cur[1])
                else:
                    stack.append((idx, cur))
        self.intervals = stack
        return list(map(lambda x: x[1], stack))



class SummaryRanges_own(object):
    def __init__(self):
        self.intervals = []
    
    def addNum(self, val):
        if not self.intervals:
            self.intervals.append([val, val])
        else:
            result = []
            newInterval = [val, val]
            for interval in self.intervals:
                if newInterval[1] < interval[0]-1:
                    result.append(newInterval)
                    newInterval = interval
                elif newInterval[0] <= interval[1]+1:
                    newInterval = [min(interval[0], newInterval[0]), \
                                   max(interval[1], newInterval[1])]
                else:
                    result.append(interval)
            result.append(newInterval)
            self.intervals = result
    
    def getIntervals(self):
        return self.intervals
