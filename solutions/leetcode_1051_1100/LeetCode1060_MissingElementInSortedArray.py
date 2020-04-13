class Solution:
    def missingElement(self, nums, k: int) -> int:
        # Return how many numbers are missing until nums[idx]
        missing = lambda idx: nums[idx]-nums[0]-idx

        n = len(nums)
        # if Kth missing number is larger than
        # the last element of the array
        if k > missing(n-1):
            return nums[-1] + k - missing(n-1)

        left, right = 0, n-1
        # find left = right index such that
        # missing(left-1) < k <= missing(left)
        while left < right:
            mid = (left+right)//2
            if missing(mid) < k:
                left = mid+1
            else:
                right = mid
        # Kth missing number is larger than nums[left-1]
        # and smaller than nums[left]
        return nums[left-1] + k - missing(left-1)



    def missingElement_own(self, nums, k: int) -> int:
        for i in range(len(nums)-1):
            if nums[i+1] > nums[i]+1:
                if nums[i+1]-nums[i]-1 < k:
                    k -= nums[i+1]-nums[i]-1
                else:
                    return nums[i]+k
        return nums[-1]+k

    def test(self):
        testCases = [
            [[4,7,9,10], 1],
            [[4,7,9,10], 3],
            [[1,2,4], 3],
            [[1,2,3], 4],
        ]
        for nums, k in testCases:
            res = self.missingElement(nums, k)
            print('res: %s' % res)
            print('-='*30+'-')


if __name__ == '__main__':
    Solution().test()
