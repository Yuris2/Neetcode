# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        #Identifying the middle of the list
        slow = fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        middleHead = slow.next
        slow.next = None

        #Reversing the Linked List
        l = None
        r = middleHead

        while r:
            temp = r.next
            r.next = l
            l = r
            r = temp
        
        firstHalf = head
        middleHead = l
        #Alternating Values
        while firstHalf and middleHead:
            temp1 = firstHalf.next
            temp2 = middleHead.next

            firstHalf.next = middleHead
            middleHead.next = temp1

            firstHalf = temp1
            middleHead = temp2
        



        