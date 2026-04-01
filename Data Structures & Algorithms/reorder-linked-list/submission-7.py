# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = fast = head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        
        secondHalf = slow.next
        slow.next = None

        prev,curr = None, secondHalf

        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
       
        ptr1 = head
        ptr2 = prev

        while ptr1 and ptr2:
            temp1 = ptr1.next
            temp2 = ptr2.next

            ptr1.next = ptr2
            ptr2.next = temp1

            ptr1 = temp1
            ptr2 = temp2


        