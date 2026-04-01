# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        #Find the half way point
        #Reverse the 2nd Half of the List
        #Merge (alternate) both list together

        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        secondHalf = slow.next
        slow.next = None

        l = None
        while secondHalf:
            tmp = secondHalf.next
            secondHalf.next = l
            l = secondHalf
            secondHalf = tmp
        
        #l points to head
        ptr1 = head
        ptr2 = l

        while ptr1 and ptr2:
            tmp1 = ptr1.next
            tmp2 = ptr2.next

            ptr1.next = ptr2
            ptr2.next = tmp1

            ptr1 = tmp1
            ptr2 = tmp2
        
        