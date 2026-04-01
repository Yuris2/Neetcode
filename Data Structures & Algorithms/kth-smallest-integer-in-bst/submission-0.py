# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stack = []
        node = root

        while node or stack:
            #Getting to the bottom left most
            while node:
                stack.append(node)
                node = node.left
            
            #Going back to the current Node
            node = stack.pop()
            k -= 1

            if k == 0:
                return node.val
            
            #Adding a right node to stack if presnet
            node = node.right
        
        return -1


            





        
        


                
