import heapq


# Definition for an interval.
class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e


class Solution(object):
    def employeeFreeTime(self, schedule: '[[Interval]]') -> '[Interval]':
        heap = []
        for i, arr in enumerate(schedule):
            heapq.heappush(heap, [arr[0].start, i, 0])
        res = []
        prev = heap[0][0]
        while heap:
            curr, i, j = heapq.heappop(heap)
            if curr > prev:
                res.append(Interval(prev, curr))
            prev = max(prev, schedule[i][j].end)
            if j + 1 < len(schedule[i]):
                heapq.heappush(heap, [schedule[i][j+1].start, i, j+1])
        return res
    
    def test(self):
        testCases = [
            [
                [[1,2],[5,6]],
                [[1,3]],[[4,10]],
            ],
            [
                [[1,3],[6,7]],[[2,4]],
                [[2,5],[9,12]],
            ],
        ]
        for schedule in testCases:
            print('schedule: %s' % schedule)
            arr = []
            for arr0 in schedule:
                arr.append([Interval(inter[0], inter[1]) for inter in arr0])
            schedule = arr
            result = self.employeeFreeTime(schedule)
            res = [[inter.start, inter.end] for inter in result]
            print('result: %s' % res)
            print('-='*30+'-')


if __name__ == '__main__':
    Solution().test()
