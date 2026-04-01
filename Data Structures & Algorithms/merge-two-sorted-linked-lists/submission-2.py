# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummyNode = ListNode()
        dummyPtr = dummyNode

        while list1 and list2:
            if list1.val < list2.val:
                dummyPtr.next = list1
                list1 = list1.next
            else:
                dummyPtr.next = list2
                list2 = list2.next
            
            dummyPtr = dummyPtr.next
        
        if list1:
            dummyPtr.next = list1
        else:
            dummyPtr.next = list2
        
        return dummyNode.next
        