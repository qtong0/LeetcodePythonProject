'''
Created on Jan 23, 2017

@author: MT
'''

class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        hashmap = {}
        for c in t:
            hashmap[c] = hashmap.get(c, 0)+1
        res = ''
        minLen = float('inf')
        left = 0
        hashmapAll = {}
        hashset = set()
        for i, c in enumerate(s):
            if c in hashmap and hashmapAll.get(c, 0)+1 >= hashmap[c]:
                hashset.add(c)
            hashmapAll[c] = hashmapAll.get(c, 0)+1
            while left < i and (s[left] not in hashmap or hashmapAll[s[left]] > hashmap[s[left]]):
                hashmapAll[s[left]] -= 1
                if hashmapAll[s[left]] < hashmap.get(s[left], 0):
                    hashset.discard(s[left])
                if hashmapAll[s[left]] == 0:
                    del hashmapAll[s[left]]
                left += 1
            if len(hashset) == len(hashmap):
                if minLen > i-left+1:
                    minLen = i-left+1
                    res = s[left:i+1]
        return res
    
    def minWindow_orig(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        if len(t) > len(s): return ''
        result = ''
        target = {}
        for c in t:
            if c in target:
                target[c]+=1
            else:
                target[c]=1
        hashmap = {}
        left, count, minLen = 0, 0, len(s)+1
        for i, c in enumerate(s):
            if c in target:
                if c in hashmap:
                    if hashmap[c] < target[c]:
                        count+=1
                    hashmap[c] += 1
                else:
                    hashmap[c] = 1
                    count += 1
            if count == len(t):
                sc = s[left]
                while sc not in hashmap or hashmap[sc] > target[sc]:
                    if sc in hashmap and hashmap[sc] > target[sc]:
                        hashmap[sc] -= 1
                    left += 1
                    sc = s[left]
                if i-left+1 < minLen:
                    result = s[left:i+1]
                    minLen = i-left+1 
        
        return result
    
    def test(self):
        testCases = [
            ('ADOBECODEBANC', 'ABC'),
        ]
        for s, t in testCases:
            print('s: %s' % (s))
            print('t: %s' % (t))
            result = self.minWindow(s, t)
            print('result: %s' % (result))
            print('-='*15 + '-')

Solution().test()