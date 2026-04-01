# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        #Approach
        #1.     Run a recursive algorith. Swap left and right nodes
        #2      Run on children
        #3.     Return root

        if root:
            temp = root.left
            root.left = root.right
            root.right = temp

            #Recursive calls
            self.invertTree(root.left)
            self.invertTree(root.right)
        
        return root

        