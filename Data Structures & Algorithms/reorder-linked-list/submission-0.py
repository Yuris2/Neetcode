# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        #Slow/Fast Ptr
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        secondHalf = slow.next
        slow.next = None

        #Reversed Second Half of LL
        prev = None
        curr = secondHalf

        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        
        #Merged the two sortedLists
        firstHalf = head
        secondHalf = prev

        while secondHalf and firstHalf:
            temp1 = firstHalf.next
            temp2 = secondHalf.next
            
            #Alternating approach
            firstHalf.next = secondHalf
            secondHalf.next = temp1

            firstHalf = temp1
            secondHalf = temp2
        




        