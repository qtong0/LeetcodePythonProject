import heapq


class Solution:
    def assignTasks(self, servers: list[int], tasks: list[int]) -> list[int]:
        avail = []
        nonavail = []
        for i, w in enumerate(servers):
            heapq.heappush(avail, [w, i, 0])
        res, i = [], 0
        for i, task_time in enumerate(tasks):
            while nonavail and nonavail[0][0] <= i:
                t, w, idx = heapq.heappop(nonavail)
                heapq.heappush(avail, [w, idx, t])
            if avail:
                w, idx, t = heapq.heappop(avail)
                res.append(idx)
                heapq.heappush(nonavail, [i+task_time, w, idx])
            else:
                t, w, idx = heapq.heappop(nonavail)
                res.append(idx)
                heapq.heappush(nonavail, [t+task_time, w, idx])
        return res

    def test(self):
        test_cases = [
            [[3,3,2], [1,2,3,2,1,2]],
            [[5,1,4,3,2], [2,1,2,4,5,2,1]],
            [[10,63,95,16,85,57,83,95,6,29,71], [70,31,83,15,32,67,98,65,56,48,38,90,5]],
            [[31,96,73,90,15,11,1,90,72,9,30,88], [87,10,3,5,76,74,38,64,16,64,93,95,60,79,54,26,30,44,64,71]],
        ]
        for servers, tasks in test_cases:
            res_1 = self.assignTasks(servers, tasks)
            print('res_1: %s' % res_1)
            print('-='*30 + '-')


if __name__ == '__main__':
    Solution().test()
