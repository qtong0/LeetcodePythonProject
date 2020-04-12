# The read4 API is already defined for you.
# @param buf, a list of characters
# @return an integer
def read4(buf):
    pass


class Solution(object):
    def __init__(self):
        self.ptr = 0
        self.cnt = 0
        self.buff = ['']*4
    
    def read(self, buf, n):
        """
        :type buf: Destination buffer (List[str])
        :type n: Maximum number of characters to read (int)
        :rtype: The number of characters read (int)
        """
        idx = 0
        while idx < n:
            if self.ptr == 0:
                self.cnt = read4(self.buff)
            if self.cnt == 0:
                break
            while idx < n and self.ptr < self.cnt:
                buf[idx] = self.buff[self.ptr]
                idx += 1
                self.ptr += 1
            if self.ptr >= self.cnt:
                self.ptr = 0
        return idx
