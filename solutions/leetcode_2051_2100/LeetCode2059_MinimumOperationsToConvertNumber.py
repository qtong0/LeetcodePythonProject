from typing import List


class Solution:
    def minimumOperations(self, nums: List[int], start: int, goal: int) -> int:
        queue = [[goal, 0]]
        visited = set([goal])
        while queue:
            node, d = queue.pop(0)
            for num in nums:
                for nei in [node + num, node - num, node ^ num]:
                    if 0 <= nei <= 1000 and nei not in visited:
                        if nei == start:
                            return d + 1
                        queue.append([nei, d+1])
                        visited.add(nei)
        return -1


    def test(self):
        test_cases = [
            [[1,3], 6, 4],
            [[2,4,12], 2, 12],
            [[3,5,7], 0, -4],
            [[2,8,16], 0, 1],
            [[1], 0, 3],
        ]
        for nums, start, goal in test_cases:
            res = self.minimumOperations(nums, start, goal)
            print('res: %s' % res)
            print('-='*30 + '-')


if __name__ == '__main__':
    Solution().test()
