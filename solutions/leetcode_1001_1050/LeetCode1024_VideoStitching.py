from typing import List


class Solution:
    # Sort
    # Checking max_reach, like Jump Game II
    #
    def videoStitching(self, clips: List[List[int]], T: int) -> int:
        clips.sort(key=lambda a: [a[0], -a[1]])
        res, end, max_reach = 0, 0, 0
        i = 0
        while i < len(clips) and end < T:
            res += 1
            while i < len(clips) and clips[i][0] <= end:
                max_reach = max(max_reach, clips[i][1])
                i += 1
            if end == max_reach:
                return -1
            end = max_reach
        return res if end >= T else -1


    # Sort
    # checking prev_end and end
    #
    def videoStitching_another(self, clips: List[List[int]], T: int) -> int:
        clips.sort(key=lambda a: [a[0], -a[1]])
        res = 0
        prev_end, end = -1, 0
        for c in clips:
            if end >= T:
                return res
            if c[0] > end:
                return -1
            if prev_end < c[0] <= end:
                res += 1
                prev_end = end
            end = max(end, c[1])
        return res if end >= T else -1


    def test(self):
        test_cases = [
            [[[0,1],[1,2]], 5],
            [[[0, 4], [2, 6], [4, 7], [6, 9]], 9],
            [[[0,2],[4,6],[8,10],[1,9],[1,5],[5,9]], 10],
            [[[0,1],[6,8],[0,2],[5,6],[0,4],[0,3],[6,7],[1,3],[4,7],[1,4],[2,5],[2,6],[3,4],[4,5],[5,7],[6,9]], 9],
            [[[0,4],[2,8]], 5],
        ]
        for clips, t in test_cases:
            res = self.videoStitching(clips, t)
            print('res: %s' % res)
            print('-='*30 + '-')


if __name__ == '__main__':
    Solution().test()
