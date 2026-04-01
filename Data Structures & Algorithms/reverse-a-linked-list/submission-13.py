# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# 2 pointers
# the first pointer is at prev, second is curr. initialize as null and head
# iterative loop that runs while curr is NOT null. while curr:
# once curr is null, it has reached the end 

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev, curr = None, head

        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        return prev