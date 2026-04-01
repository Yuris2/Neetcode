# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        #Global Variable for the diameter to be updated
        self.diameter = 0

        #Returns the height of the tree
        #Input = TreeNode()
        def dfs(root):
            if root:
                #Taking the height of left and tree ST
                leftHeight = dfs(root.left)
                rightHeight = dfs(root.right)

                #Checking if the diameter is greater than the global var
                self.diameter = max(self.diameter, leftHeight + rightHeight)

                #Returning the height of the tree at a current Node
                return 1 + max(leftHeight, rightHeight)
            else:
                return 0
        
        dfs(root)
        return self.diameter

        