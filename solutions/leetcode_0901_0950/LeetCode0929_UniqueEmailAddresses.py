class Solution(object):
    def numUniqueEmails(self, emails):
        """
        :type emails: List[str]
        :rtype: int
        """
        hashset = set()
        for email in emails:
            hash = self.getHash(email)
            hashset.add(hash)
        return len(hashset)

    def getHash(self, s):
        res = ''
        skip = False
        for i, c in enumerate(s):
            if c == '@':
                res += s[i:]
                return res
            elif c == '+':
                skip = True
            elif not skip and c != '.':
                res += c
        return res
