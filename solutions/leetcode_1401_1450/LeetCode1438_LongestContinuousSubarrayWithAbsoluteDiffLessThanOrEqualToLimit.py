from typing import List
import heapq


class Solution:
    # Sliding window - two deques solution
    # Best - Time(O), Space(O)
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        max_deque = []
        min_deque = []
        j = 0
        res = 0
        for i, num in enumerate(nums):
            while max_deque and num > max_deque[-1]:
                max_deque.pop()
            while min_deque and num < min_deque[-1]:
                min_deque.pop()
            max_deque.append(num)
            min_deque.append(num)
            if max_deque[0] - min_deque[0] > limit:
                # The biggest difference is over the limit; so remove A[i] from the window.
                # Why do we check only maxd[0]/mind[0] to remove A[i]?
                # Take maxd as an example. In order for A[i] to be present in maxd,
                # A[i] >= A[x], where x = i+1...j. In other words, it has to be the biggest element or
                # it would have already been removed. The biggest element would be in maxd[0].
                # Similar explanation applies for mind.
                if max_deque[0] == nums[j]:
                    max_deque.pop(0)
                if min_deque[0] == nums[j]:
                    min_deque.pop(0)
                # The new window for consideration is A[i+1]...A[j].
                j += 1
            # At every iteration of j, the window size for consideration is from A[i..j]. Its size is j+1-i.
            # At every iteration, an element is added to the window and possibly removed only if the window contains
            # elements with max difference > limit.
            # So the window size only grows monotonically but never shrinks in size. The window grows only if all the elements in
            # the window satisfy the max difference <= limit.
            # Therefore, the last window size in the iteration(when j=len(A)-1) holds the maximum size of the window with max diff <= limit.
            # However, it must be noted that the window in consideration at the last iteration may not really be the window
            # which has the max diff <= limit.
            # This doesn't matter since all we are interested in is the window size and not really the elements in the window.
            res = max(res, i-j+1)
        return res

    # sliding window - using max heap and min heap
    # Not best, but easier to understand
    # Time: O(N*Log(N))
    # Space: O(N)
    def longestSubarray_heap(self, nums: List[int], limit: int) -> int:
        max_heap, min_heap = [], []
        res = 0
        j = 0
        for i, num in enumerate(nums):
            heapq.heappush(max_heap, [-num, i])
            heapq.heappush(min_heap, [num, i])
            while -max_heap[0][0] - min_heap[0][0] > limit:
                j = min(max_heap[0][1], min_heap[0][1]) + 1
                while max_heap[0][1] < j:
                    heapq.heappop(max_heap)
                while min_heap[0][1] < j:
                    heapq.heappop(min_heap)
            res = max(res, i-j+1)
        return res


    def test(self):
        test_cases = [
            [[8,2,4,7], 4],
            [[10,1,2,4,7,2], 5],
            [[4,2,2,2,4,4,2,2], 0],
        ]
        for nums, limit in test_cases:
            res = self.longestSubarray(nums, limit)
            res_2 = self.longestSubarray_heap(nums, limit)
            print('res: %s' % res)
            print('res: %s' % res_2)
            print('-='*30 + '-')


if __name__ == '__main__':
    Solution().test()
