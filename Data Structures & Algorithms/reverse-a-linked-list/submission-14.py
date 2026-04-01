# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None # base case -> list empty
        
        newHead = head # assume the head is the new head until proven otherwise
        if head.next: # if head.next exists
            newHead = self.reverseList(head.next) # reverse the rest of the list
            head.next.next = head # reverses the original pointer
        head.next = None

        return newHead
        
