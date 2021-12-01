from typing import List


class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        n = len(boxes)
        left = [0]*n
        count = 0
        sum_val = 0
        for i in range(n):
            sum_val += count
            left[i] = sum_val
            if boxes[i] == '1':
                count += 1
        right = [0]*n
        sum_val = 0
        count = 0
        for i in range(n-1, -1, -1):
            sum_val += count
            right[i] = sum_val
            if boxes[i] == '1':
                count += 1
        res = [0]*n
        for i in range(n):
            res[i] = left[i] + right[i]
        return res


    def test(self):
        test_cases = [
            '1111',
            '110',
            '001011',
        ]
        for boxes in test_cases:
            res = self.minOperations(boxes)
            print('res: %s' % res)
            print('-='*30 + '-')


if __name__ == '__main__':
    Solution().test()
