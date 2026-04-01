# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        #Recursive Approach Just like in class
        if root:
            #Swapping Left and Right elements of subtree
            temp = root.left
            root.left = root.right
            root.right = temp

            #Recursive call on subtrees
            self.invertTree(root.left)
            self.invertTree(root.right)
        else:
            return None
        
        return root
            
        