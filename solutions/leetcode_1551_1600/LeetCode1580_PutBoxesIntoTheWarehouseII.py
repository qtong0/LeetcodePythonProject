from typing import List


class Solution:
    def maxBoxesInWarehouse(self, boxes: List[int], warehouse: List[int]) -> int:
        boxes.sort()
        p1, p2 = 0, len(warehouse)-1
        res = 0
        for i in range(len(boxes)-1, -1, -1):
            if boxes[i] <= warehouse[p1]:
                p1 += 1
                res += 1
            elif boxes[i] <= warehouse[p2]:
                p2 -= 1
                res += 1
            if p1 > p2:
                break
        return res


    def test(self):
        test_cases = [
            [[1,2,2,3,4], [3,4,1,2]],
            [[3,5,5,2], [2,1,3,4,5]],
            [[1,2,3], [1,2,3,4]],
            [[4,5,6], [3,3,3,3,3]],
        ]
        for boxes, warehouse in test_cases:
            res = self.maxBoxesInWarehouse(boxes, warehouse)
            print('res: %s' % res)
            print('-='*30 + '-')


if __name__ == '__main__':
    Solution().test()
