# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        fast = slow = head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        
        #break the linked list
        ptr2 = slow.next
        slow.next = None

        #Reverse the second head
        head2 = None
        while ptr2:
            temp = ptr2.next
            ptr2.next = head2
            head2 = ptr2
            ptr2 = temp
        
        head1 = head

        while head1 and head2:
            temp1 = head1.next
            temp2 = head2.next

            head1.next = head2
            head2.next = temp1

            head1 = temp1
            head2 = temp2
        

        