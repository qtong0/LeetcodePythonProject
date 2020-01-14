class Solution(object):
    def diStringMatch(self, S):
        """
        :type S: str
        :rtype: List[int]
        """
        i, j = 0, len(S)
        res = []
        for c in S:
            if c == 'I':
                res.append(i)
                i += 1
            else:
                res.append(j)
                j -= 1
        res.append(i)
        return res
