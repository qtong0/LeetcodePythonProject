from typing import List


class Solution:
    # !!! Can-Do Binary Search !!!
    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort()
        l, r = 1, position[-1] - position[0]
        while l < r:
            mid = (l + r) // 2
            if self.canDo(position, m, mid):
                l = mid + 1
            else:
                r = mid
        max_dist = position[-1] - position[0]
        return l - 1 if l < max_dist else max_dist

    def canDo(self, pos, m, force):
        prev = 0
        for i, p in enumerate(pos):
            if i == 0 or prev + force <= p:
                prev = p
                m -= 1
                if m <= 0:
                    return True
        return m <= 0

    def test(self):
        test_cases = [
            [[1, 2, 3, 4, 7], 3],
            [[5, 4, 3, 2, 1, 1000000000], 2],
        ]
        for position, m in test_cases:
            res = self.maxDistance(position, m)
            print('res: %s' % res)
            print('-=' * 30 + '-')


if __name__ == '__main__':
    Solution().test()
