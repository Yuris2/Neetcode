# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        curr = dummy

        carry = 0
        p1,p2 = l1, l2

        while p1 or p2 or carry > 0:
            v1, v2 = 0,0
            if p1:
                v1 = p1.val 
            if p2:
                v2 = p2.val
            
            total = v1 + v2 + carry
            carry = total // 10
            digit = total % 10

            node = ListNode(digit)
            curr.next = node
            curr = curr.next
            
            if p1:
                p1 = p1.next
            if p2:
                p2 = p2.next
        
        return dummy.next


        