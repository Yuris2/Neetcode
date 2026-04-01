# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        mergedList = ListNode()
        headPtr = mergedList

        while list1 and list2:
            if list1.val < list2.val:
                headPtr.next = list1
                list1 = list1.next
            else:
                headPtr.next = list2
                list2 = list2.next
            
            headPtr = headPtr.next
        
        if list1:
            headPtr.next = list1
        elif list2:
            headPtr.next = list2
        
        return mergedList.next
        