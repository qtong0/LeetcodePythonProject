# """
# This is ArrayReader's API interface.
# You should not implement it, or speculate about its implementation
# """
class ArrayReader:
   def get(self, index: int) -> int:
       pass


class Solution:
    def search(self, reader, target):
        """
        :type reader: ArrayReader
        :type target: int
        :rtype: int
        """
        if reader.get(0) == target:
            return 0

        # search boundaries
        l, r = 0, 1
        while reader.get(r) < target:
            l = r
            r <<= 1

        # binary search
        while l <= r:
            mid = (l+r)//2
            num = reader.get(mid)
            if num == target:
                return mid
            elif num > target:
                r = mid-1
            else:
                l = mid+1
        return -1
