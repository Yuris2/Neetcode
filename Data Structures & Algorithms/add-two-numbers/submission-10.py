# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummyNode = ListNode()
        ptr = dummyNode
        carry = 0

        p1, p2 = l1, l2

        while p1 or p2 or carry:
            v1,v2 = 0,0

            if p1:
                v1 = p1.val
            if p2:
                v2 = p2.val
            
            res = v1 + v2 + carry

            digit = res % 10
            carry = res // 10

            ptr.next = ListNode(digit)
            ptr = ptr.next

            if p1:
                p1 = p1.next
            if p2:
                p2 = p2.next

        return dummyNode.next            
        