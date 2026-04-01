# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        ptr1, ptr2 = list1, list2

        dummyNode = ListNode()
        curr = dummyNode

        while ptr1 and ptr2:
            if ptr1.val < ptr2.val:
                curr.next = ptr1
                ptr1 = ptr1.next
            else:
                curr.next = ptr2
                ptr2 = ptr2.next
            curr = curr.next
        
        if ptr1:
            curr.next = ptr1
        elif ptr2:
            curr.next = ptr2
        
        return dummyNode.next
