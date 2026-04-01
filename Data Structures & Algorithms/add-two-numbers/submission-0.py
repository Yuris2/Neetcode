# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummyNode = ListNode()
        cur = dummyNode

        carry = 0
        while l1 or l2 or carry != 0:
            v1, v2 = 0,0
            if l1:
                v1 = l1.val
            if l2:
                v2 = l2.val
        
            value = carry + v1 + v2
            carry = value // 10
            value = value % 10
            cur.next = ListNode(value)

            #Increment pointers
            cur = cur.next
            if l1:
                l1 = l1.next

            if l2:
                l2 = l2.next

        return dummyNode.next
            
        