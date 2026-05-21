# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.res = 0

        def dfs(root, maxVal):
            if not root:
                return 

            if root.val >= maxVal:
                self.res += 1

            newMax = max(maxVal, root.val)
            
            dfs(root.left, newMax)
            dfs(root.right, newMax)

        dfs(root, root.val)

        return self.res
                




            
            

