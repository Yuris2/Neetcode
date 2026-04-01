# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        tail = dummy
        while list1 and list2:
            if list1.val > list2.val:
                tail.next = list2
                list2 = list2.next
            else:
                tail.next = list1
                list1 = list1.next
            tail = tail.next
        
        if list1:
            tail.next = list1
        elif list2:
            tail.next = list2
        
        return dummy.next



        # RUN WHILE BOTH NODES ARE NOT NONE
        # 1. Create a dummy node, with a tail.
        # 2. While both nodes are not None:
        # - Compare the values of the two nodes, identify the larger one.
        # - Add the smaller/equal one to the linked list.
        # – Go to the next value in the list node you just added.
        # 3. Add any remaining values from the nonempty list.
        # 4. Return the tail of the linked list.
        
                