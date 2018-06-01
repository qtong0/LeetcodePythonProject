'''
Created on Jan 22, 2017

@author: MT
'''

class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        numberList = [i+1 for i in range(n)]
        k -= 1
        mod = 1
        for i in range(n):
            mod = mod*(i+1)
        result = ''
        for i in range(n):
            mod = int(mod)/(n-i)
            curInd = int(k)/mod
            k = k % mod
            result += str(numberList[curInd])
            numberList.pop(curInd)
        return result