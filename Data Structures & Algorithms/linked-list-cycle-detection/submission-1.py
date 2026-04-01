# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        heads = set()
        ptr = head

        while ptr:
            if ptr.val in heads:
                return True
            else:
                heads.add(ptr.val)
            
            ptr = ptr.next
        
        return False
            
        

        