class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        minutes_angle = minutes / 60 * 360
        hour_angle = hour / 12 * 360
        hour_angle += (minutes / 60) * (360 / 12)
        angle = abs(minutes_angle-hour_angle)
        return min(angle, 360 - angle)

    def test(self):
        test_cases = [
            [12, 30],
            [3, 30],
            [3, 15],
            [4, 50],
            [12, 0],
        ]
        for hour, minutes in test_cases:
            res = self.angleClock(hour, minutes)
            print('res: %s' % res)
            print('-='*30 + '-')


if __name__ == '__main__':
    Solution().test()
