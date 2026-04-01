# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        dic = {}

        ptr = head

        while ptr:
            if ptr.val in dic:
                return True
            
            dic[ptr.val] = 1

            ptr = ptr.next
        
        return False
            
        

        