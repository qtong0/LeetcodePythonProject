class Solution(object):
    def leastInterval_another(self, tasks, n: int) -> int:
        arr = [0]*26
        for t in tasks:
            arr[ord(t)-ord('A')] += 1
        arr.sort()
        i = 25
        while i >= 0 and arr[i]==arr[-1]:
            i -= 1
        return max(len(tasks), (arr[-1]-1)*(n+1)+25-i)


    def leastInterval(self, tasks, n: int) -> int:
        import heapq
        hashmap = {}
        for task in tasks:
            hashmap[task] = hashmap.get(task, 0)+1
        heap = []
        for count in hashmap.values():
            heapq.heappush(heap, -count)
        res = 0
        cycle = n+1
        while heap:
            worktime = 0
            queue = []
            for i in range(cycle):
                if heap:
                    queue.append(heapq.heappop(heap))
                    worktime += 1
            for cnt in queue:
                cnt = -cnt
                if cnt - 1 > 0:
                    heapq.heappush(heap, -(cnt-1))
            res += cycle if heap else worktime
        return res


    def leastInterval_OWN(self, tasks, n: int) -> int:
        import heapq
        hashmap = {}
        for task in tasks:
            hashmap[task] = hashmap.get(task, 0)+1
        heap = []
        for c, count in hashmap.items():
            heapq.heappush(heap, (-count, c))
        res = 0
        queue = []
        while heap:
            count, c = heapq.heappop(heap)
            queue.append((-count, c))
            if len(queue) > n:
                res += len(queue)
                while queue:
                    count, c = queue.pop(0)
                    count -= 1
                    if count > 0:
                        heapq.heappush(heap, (-count, c))
            if not heap:
                count0 = len(queue)
                while queue:
                    count, c = queue.pop(0)
                    count -= 1
                    if count > 0:
                        heapq.heappush(heap, (-count, c))
                if not heap:
                    res += count0
                else:
                    res += n+1
        return res
    
    def test(self):
        testCases = [
            [
                ['A', 'A', 'A', 'B', 'B', 'B'],
                2,
            ],
            [
                ['A','A','A','A','A','A','B','C','D','E','F','G'],
                2,
            ],
        ]
        for tasks, n in testCases:
            print('tasks: %s' % tasks)
            print('n: %s' % n)
            result = self.leastInterval(tasks, n)
            result2 = self.leastInterval_OWN(tasks, n)
            print('result: %s' % result)
            print('result2: %s' % result2)
            print('-='*30+'-')


if __name__ == '__main__':
    Solution().test()
