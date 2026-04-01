# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        def dfs(node, maxValuePath):
            if not node:
                return 0
            
            res = 0

            if node.val >= maxValuePath:
                res += 1
            
            maxValuePath = max(maxValuePath, node.val)
            
            res += dfs(node.left, maxValuePath)
            res += dfs(node.right, maxValuePath)

            return res
        
        return dfs(root, -2e9)