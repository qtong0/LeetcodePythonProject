class Solution(object):
    def nextClosestTime(self, time: str) -> str:
        hour, minute = time.split(':')

        nums = sorted(set(hour + minute))
        two_digit_values = [a+b for a in nums for b in nums]

        i = two_digit_values.index(minute)
        if i + 1 < len(two_digit_values) and two_digit_values[i+1] < '60':
            return hour + ':' + two_digit_values[i+1]

        i = two_digit_values.index(hour)
        if i + 1 < len(two_digit_values) and two_digit_values[i+1] < '24':
            return two_digit_values[i+1] + ':' + two_digit_values[0]

        return two_digit_values[0] + ':' + two_digit_values[0]


    # My own solution, go through minute by minute to check
    def nextClosestTime_own_slow(self, time):
        """
        :type time: str
        :rtype: str
        """
        arr = list(time[:2]+time[3:])
        hh = int(''.join(arr[:2]))
        mm = int(''.join(arr[2:]))
        charSet = set(arr)
        if len(charSet) == 1:
            return time
        for i in range(1, 24*60):
            valid, res = self.increaseAndCheck(hh, mm, i, charSet)
            if valid:
                return res
        return time
    
    def increaseAndCheck(self, hh, mm, i, charSet):
        mm += i
        if mm >= 60:
            carry = mm//60
            mm = mm%60
        else:
            carry = 0
        hh += carry
        if hh >= 24:
            hh -= 24
        res = str(hh) if len(str(hh))==2 else '0'+str(hh)
        res += ':'
        res += str(mm) if len(str(mm))==2 else '0'+str(mm)
        for c in res:
            if c != ':' and c not in charSet:
                return False, res
        return True, res


    def test(self):
        testCases = [
            '19:34',
            '23:59',
        ]
        for time in testCases:
            print('time: %s' % time)
            result = self.nextClosestTime(time)
            print('result: %s' % result)
            print('-='*30+'-')


if __name__ == '__main__':
    Solution().test()
