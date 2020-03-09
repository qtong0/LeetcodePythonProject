class Solution(object):
    def hasGroupsSizeX(self, deck):
        """
        :type deck: List[int]
        :rtype: bool
        """
        if not deck: return False
        hashmap = {}
        for num in deck:
            hashmap[num] = hashmap.get(num, 0)+1
        counts = list(hashmap.values())
        minVal = min(counts)
        for x in range(2, minVal+1):
            found = True
            for count in counts:
                if count % x != 0:
                    found = False
                    break
            if found:
                return True
        return False
