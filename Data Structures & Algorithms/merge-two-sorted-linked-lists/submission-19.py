# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


# both lists are sorted
# while both lists exist, compare nodes at same index from both lists
# less of the 2 will be added to the output list
# each time this addition happens, increment the proper list
# edge case: account for if lists are different size
# outside of the original conditions, if a list is existing then append the rest of it
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        tail = dummy

        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next
        
        tail.next = list1 or list2

        return dummy.next






