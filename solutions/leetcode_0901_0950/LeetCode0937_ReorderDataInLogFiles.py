class Solution(object):
    def reorderLogFiles(self, logs):
        """
        :type logs: List[str]
        :rtype: List[str]
        """
        tosort = []
        nosort = []
        for log in logs:
            arr = log.split(' ')
            if all(s.isdigit() for s in arr[1:]):
                nosort.append(log)
            else:
                tosort.append([arr[1:], arr[0], log])
        res = [arr[-1] for arr in sorted(tosort)]
        res += nosort
        return res
