# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        result = ListNode()
        ptr = result

        carry = 0
        while l1 or l2 or carry != 0:
            #Values that we are going to add
            v1, v2 = 0,0
            #If they are not null
            if l1:
                v1 = l1.val
            if l2:
                v2 = l2.val
            #adding the result   
            res = v1 + v2 + carry
            #Getting the value of the carry
            carry = res // 10
            #Getting the result we are adding to the Linked List
            res = res % 10

            ptr.next = ListNode(res)
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
            
            ptr = ptr.next
        
        return result.next
            

        