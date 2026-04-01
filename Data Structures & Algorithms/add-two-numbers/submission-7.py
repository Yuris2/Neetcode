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
        v1 = l1
        v2 = l2

        while v1 or v2 or carry != 0:
            d1 = d2 = 0

            if v1:
                d1 = v1.val
            if v2:
                d2 = v2.val
            
            res = d1 + d2 + carry
            digit = res % 10
            carry = res // 10

            ptr.next = ListNode(digit)

            if v1:
                v1 = v1.next
            if v2:
                v2 = v2.next
            ptr = ptr.next
        
        return dummyNode.next



        