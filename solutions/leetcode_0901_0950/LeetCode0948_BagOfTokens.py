class Solution(object):
    def bagOfTokensScore(self, tokens, P):
        """
        :type tokens: List[int]
        :type P: int
        :rtype: int
        """
        tokens.sort()
        ans = tmp = 0
        while tokens and (P >=  tokens[0] or tmp):
            while tokens and P >= tokens[0]:
                P -= tokens.pop(0)
                tmp += 1
            ans = max(ans, tmp)
            if tokens and tmp:
                P += tokens.pop()
                tmp -= 1
        return ans
