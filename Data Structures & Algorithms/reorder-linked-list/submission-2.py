# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        #Split the list into 2
        slow = fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        right = slow.next
        slow.next = None

        #Reverse middle half
        middleHead = None

        while right:
            temp = right.next
            right.next = middleHead
            middleHead = right
            right = temp
        
        #Alternating Merge
        ptr1 = head
        ptr2 = middleHead

        while ptr1 and ptr2:
            #Used to increment the pointers
            temp1 = ptr1.next
            temp2 = ptr2.next
            #Kinda like a zig-zag visualized
            ptr1.next = ptr2
            ptr2.next = temp1
            #Increment pointers
            ptr2 = temp2
            ptr1 = temp1


        
        