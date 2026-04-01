# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
    #When we split from a node we can't get its parents
        res = [root.val]

        def dfs(root):
            #Base Case
            if not root:
                return 0
            
            leftMax = max(0,dfs(root.left))
            rightMax = max(0, dfs(root.right))

            #Max value with a split
            res[0] = max(res[0], root.val + leftMax + rightMax)

            #Max value without a split
            return root.val + max(leftMax, rightMax)
        
        dfs(root)
        return res[0]
