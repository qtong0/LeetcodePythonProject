from typing import List


class Solution:
    def largestMultipleOfThree(self, digits: List[int]) -> str:
        sum_val = 0
        arr = [[] for _ in range(3)]
        digits.sort()
        for d in digits:
            arr[d%3].append(d)
            sum_val += d
        if sum_val % 3 == 0:
            digits = digits[::-1]
        elif sum_val % 3 == 1:
            if arr[1]:
                to_remove = arr[1][0]
                digits.remove(to_remove)
                digits = digits[::-1]
            elif len(arr[2]) >= 2:
                to_removes = arr[2][:2]
                digits.remove(to_removes[0])
                digits.remove(to_removes[1])
                digits = digits[::-1]
            else:
                return ''
        else:
            if arr[2]:
                to_remove = arr[2][0]
                digits.remove(to_remove)
                digits = digits[::-1]
            elif len(arr[1]) >= 2:
                to_removes = arr[1][:2]
                digits.remove(to_removes[0])
                digits.remove(to_removes[1])
                digits = digits[::-1]
            else:
                return ''
        if not digits:
            return ''
        res = ''.join(str(d) for d in digits)
        res = res.lstrip('0')
        return res if res else '0'

    def test(self):
        test_cases = [
            [8,1,9],
            [8,6,7,1,0],
            [1],
            [0,0,0,0,0,0],
        ]
        for digits in test_cases:
            res = self.largestMultipleOfThree(digits)
            print('res: %s' % res)
            print('-='*30 + '-')


if __name__ == '__main__':
    Solution().test()
