# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(root, left, right):
            #If we reach the end, we have a valid BST
            if not root:
                return True
            
            #If we violate the BST condition at the current root
            if not (left < root.val < right):
                return False
            
            #Check for the entire left subtree and right subtree
            #All values in left subtree have to be less than current root
            left = dfs(root.left, left, root.val)
            #All values in right subtree have to be greater than current root
            right = dfs(root.right, root.val, right)

            return left and right
        
        #Root can be any value
        return dfs(root, -2e9, 2e9)
        