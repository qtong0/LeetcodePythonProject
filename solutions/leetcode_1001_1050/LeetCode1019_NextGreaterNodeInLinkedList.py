# Definition for singly-linked list.
class ListNode:
    def __init__(self, x, next=None):
        self.val = x
        self.next = next


class Solution:
    def nextLargerNodes(self, head: ListNode):
        stack = []
        node = self.reverse(head)
        res = []
        while node:
            while stack and stack[-1] <= node.val:
                stack.pop()
            if stack:
                res.insert(0, stack[-1])
            else:
                res.insert(0, 0)
            stack.append(node.val)
            node = node.next
        return res

    def reverse(self, node):
        if not node or not node.next:
            return node
        p1, p2 = node, node.next
        p1.next = None
        while p1 and p2:
            tmp = p2.next
            p2.next = p1
            p1 = p2
            p2 = tmp
        return p1

    def test(self):
        testCases = [
            ListNode(2, ListNode(1, ListNode(5))),
            ListNode(1, ListNode(7, ListNode(5, ListNode(1, ListNode(9, ListNode(2, ListNode(5, ListNode(1)))))))),
        ]
        for head in testCases:
            res = self.nextLargerNodes(head)
            print('res: %s' % res)
            print('-='*30+'-')


if __name__ == '__main__':
    Solution().test()
