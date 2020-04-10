import heapq


class Solution:
    def carPooling(self, trips, capacity: int) -> bool:
        heap = []
        trips.sort(key=lambda t: t[1])
        nums = 0
        for trip in trips:
            while heap and heap[0][0] <= trip[1]:
                nums -= heapq.heappop(heap)[1]
            nums += trip[0]
            heapq.heappush(heap, [trip[2], trip[0]])
            if nums > capacity:
                return False
        return True

    def test(self):
        testCases = [
            [
                [[2,1,5],[3,3,7]], 4,
            ],
            [
                [[2,1,5],[3,3,7]], 5,
            ],
            [
                [[2,1,5],[3,5,7]], 3,
            ],
            [
                [[3,2,7],[3,7,9],[8,3,9]], 11,
            ],
            [
                [[9,3,4],[9,1,7],[4,2,4],[7,4,5]], 23,
            ]
        ]
        for trips, capacity in testCases:
            res = self.carPooling(trips, capacity)
            print('res: %s' % res)
            print('-='*30 + '-')


if __name__ == '__main__':
    Solution().test()
