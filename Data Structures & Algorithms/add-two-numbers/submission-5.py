# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummyNode = ListNode()
        
        curr = dummyNode
        ptr1, ptr2 = l1, l2
        carry = 0

        while ptr1 or ptr2 or carry != 0:
            v1, v2 = 0,0
            if ptr1:
                v1 = ptr1.val
            if ptr2:
                v2 = ptr2.val
            
            value = v1 + v2 + carry
            carry = value // 10
            digit = value % 10

            curr.next = ListNode(digit)
            curr = curr.next

            if ptr1:
                ptr1 = ptr1.next
            if ptr2:
                ptr2 = ptr2.next
        
        return dummyNode.next




        