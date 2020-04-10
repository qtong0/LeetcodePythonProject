import heapq


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val, nextNode=None):
        self.val = val
        self.next = nextNode


class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        heap = []
        for node in lists:
            if node:
                heapq.heappush(heap, (node.val, id(node), node))
        dummy = ListNode(-1)
        prev = dummy
        while heap:
            _, _, node = heapq.heappop(heap)
            if node.next:
                heapq.heappush(heap, (node.next.val, id(node.next), node.next))
            prev.next = node
            prev = node
        return dummy.next
    
    def test(self):
        testCases = [
            [
                ListNode(-1, ListNode(-1, ListNode(-1))),
                ListNode(-2, ListNode(-2, ListNode(-1))),
            ],
        ]
        for lists in testCases:
            node = self.mergeKLists(lists)
            while node:
                print('%s -> ' % node.val, end='')
                node = node.next
            print('')
            print('-='*30+'-')


if __name__ == '__main__':
    Solution().test()
