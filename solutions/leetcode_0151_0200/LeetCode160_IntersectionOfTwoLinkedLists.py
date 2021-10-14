# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x, nextNode):
        self.val = x
        self.next = nextNode


class Solution(object):
    # two runners
    # O(N+M)
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        n1, n2 = headA, headB
        while n1 != n2:
            n1 = n1.next if n1 else headB
            n2 = n2.next if n2 else headA
        return n1


    def getIntersectionNode_own(self, headA, headB):
        lenA = self.getLength(headA)
        lenB = self.getLength(headB)
        if not lenA or not lenB: return None
        if lenA < lenB:
            headA, headB = headB, headA
        diff = abs(lenA-lenB)
        while diff and headA:
            headA = headA.next
            diff -= 1
        while headA and headB:
            if headA == headB:
                return headA
            headA = headA.next
            headB = headB.next
        return None
    
    def getLength(self, head):
        length = 0
        while head:
            head = head.next
            length += 1
        return length
