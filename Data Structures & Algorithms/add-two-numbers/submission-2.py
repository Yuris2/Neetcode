# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        ptr1, ptr2 = l1, l2
        dummyNode = ListNode()
        curr = dummyNode
        carry = 0

        while ptr1 or ptr2 or carry != 0:
            val1, val2 = 0,0
            if ptr1:
                val1 = ptr1.val
            if ptr2:
                val2 = ptr2.val

            totalSum = val1 + val2 + carry
            digit = totalSum % 10
            carry = totalSum // 10

            curr.next = ListNode(digit)
            curr = curr.next

            if ptr1:
                ptr1 = ptr1.next
            if ptr2:
                ptr2 = ptr2.next
        
        return dummyNode.next






        