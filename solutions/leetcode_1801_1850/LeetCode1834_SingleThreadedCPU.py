import heapq


class Solution:
    def getOrder(self, tasks: list[list[int]]) -> list[int]:
        heap, res, time = [], [], 0
        tasks = sorted([(t[0], t[1], i) for i, t in enumerate(tasks)])
        time = tasks[0][0]
        i = 0
        while len(res) < len(tasks):
            while (i < len(tasks)) and (tasks[i][0] <= time):
                heapq.heappush(heap, [tasks[i][1], tasks[i][2]])
                i += 1
            if heap:
                t_diff, orig_idx = heapq.heappop(heap)
                time += t_diff
                res.append(orig_idx)
            elif i < len(tasks):
                time = tasks[i][0]
        return res


    def test(self):
        test_cases = [
            [[1,2],[2,4],[3,2],[4,1]],
            [[7,10],[7,12],[7,5],[7,4],[7,2]],
        ]
        for tasks in test_cases:
            res = self.getOrder(tasks)
            print('res: %s' % res)
            print('-='*30+'-')


if __name__ == '__main__':
    Solution().test()
