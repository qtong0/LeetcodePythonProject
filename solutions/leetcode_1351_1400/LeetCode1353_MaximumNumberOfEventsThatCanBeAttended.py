from typing import List
import heapq


class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        events.sort()
        total_days = max(event[1] for event in events)
        heap = []
        day, res, idx = 1, 0, 0
        while day <= total_days:
            # if no events are available to attend today, let time flies to the next available event.
            if idx < len(events) and not heap:
                day = events[idx][0]

            # all events starting from today are newly available, add them to the heap
            while idx < len(events) and events[idx][0] <= day:
                heapq.heappush(heap, events[idx][1])
                idx += 1

            # if the event at top already ended, then discard it
            while heap and heap[0] < day:
                heapq.heappop(heap)

            # attend the event that will end earliest
            if heap:
                heapq.heappop(heap)
                res += 1
            elif idx >= len(events):
                break
            
            day += 1
        return res


    def test(self):
        test_cases = [
            [[1,2],[2,3],[3,4]],
            [[1,2],[2,3],[3,4],[1,2]],
            [[1,4],[4,4],[2,2],[3,4],[1,1]],
            [[1,2],[1,2],[3,3],[1,5],[1,5]],
            [[1,5],[1,5],[1,5],[2,3],[2,3]],
            [[1,100000]],
        ]
        for events in test_cases:
            res = self.maxEvents(events)
            print('res: %s' % res)
            print('-='*30 + '-')


if __name__ == '__main__':
    Solution().test()
