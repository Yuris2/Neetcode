# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummyNode = ListNode()
        curr = dummyNode

        p1, p2 = l1, l2
        carry = 0

        while p1 or p2 or carry != 0:
            v1 = v2 = 0

            if p1:
                v1 = p1.val
            if p2:
                v2 = p2.val
            
            res = v1 + v2 + carry
            digit = res % 10
            carry = res // 10

            newNode = ListNode()
            newNode.val = digit
            curr.next = newNode

            if p1:
                p1 = p1.next
            if p2:
                p2 = p2.next
            curr = curr.next
        
        return dummyNode.next
