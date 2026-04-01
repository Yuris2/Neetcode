# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = fast = head

        #Find halfway split of the list
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        secondHalf = slow.next
        slow.next = None

        #Reverse the second half
        prev, curr = None, secondHalf

        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        
        firstHalf = head
        secondHalf = prev

        while firstHalf and secondHalf:
            tmp1 = firstHalf.next
            tmp2 = secondHalf.next

            firstHalf.next = secondHalf
            secondHalf.next = tmp1

            firstHalf = tmp1
            secondHalf = tmp2
        
        