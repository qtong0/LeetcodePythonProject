from typing import List


class Solution:
    def maxBoxesInWarehouse(self, boxes: List[int], warehouse: List[int]) -> int:
        boxes.sort(reverse=True)
        n = len(boxes)
        m = len(warehouse)
        smaller = [0]*m
        for i, h in enumerate(warehouse):
            if i == 0:
                smaller[i] = h
            else:
                smaller[i] = min(smaller[i-1], h)
        res = 0
        i = n-1
        for j in range(m-1, -1, -1):
            if smaller[j] >= boxes[i]:
                i -= 1
                res += 1
            if i == -1:
                return len(boxes)
        return res


    def test(self):
        test_cases = [
            [[4,3,4,1], [5,3,3,4,1]],
            [[1,2,2,3,4], [3,4,1,2]],
            [[1,2,3], [1,2,3,4]],
            [[4,5,6], [3,3,3,3,3]],
            [[2,3], [6,5,5,4,4,1,1,1,1,1,1,1,1,1,1,1]],
        ]
        for boxes, warehouse in test_cases:
            res = self.maxBoxesInWarehouse(boxes, warehouse)
            print('res: %s' % res)
            print('-='*30 + '-')


if __name__ == '__main__':
    Solution().test()
