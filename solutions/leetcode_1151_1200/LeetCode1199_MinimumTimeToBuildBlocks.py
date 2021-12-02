from typing import List
import heapq


class Solution:
    # Huffman's Algorithm
    def minBuildTime(self, blocks: List[int], split: int) -> int:
        heapq.heapify(blocks)
        while len(blocks) > 1:
            x = heapq.heappop(blocks)
            y = heapq.heappop(blocks)
            heapq.heappush(blocks, y + split)
        return heapq.heappop(blocks)


    def test(self):
        test_cases = [
            [[1], 1],
            [[1,2], 5],
            [[1,2,3], 1],
        ]
        for blocks, split in test_cases:
            res = self.minBuildTime(blocks, split)
            print('res: %s' % res)
            print('-='*30 + '-')


if __name__ == '__main__':
    Solution().test()
