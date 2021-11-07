from typing import List


class SparseVector:
    def __init__(self, nums: List[int]):
        self.length = len(nums)
        self.hashmap = {}
        for i, num in enumerate(nums):
            if num:
                self.hashmap[i] = num

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        hashmap1, hashmap2 = self.hashmap, vec.hashmap
        if len(hashmap1) > len(hashmap2):
            hashmap1, hashmap2 = hashmap2, hashmap1
        res = 0
        for i, num in hashmap1.items():
            if i in hashmap2:
                res += num * hashmap2[i]
        return res


# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)
