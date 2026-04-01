# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        vals = []
        cur = head
        while cur is not None:
            vals.append(cur.val)
            cur = cur.next
        if vals == []:
            return None
        start = ListNode()
        cur = start
        while vals != []:
            cur.val = vals.pop()
            if vals != []:
                cur.next = ListNode()
            cur = cur.next
        return start

        