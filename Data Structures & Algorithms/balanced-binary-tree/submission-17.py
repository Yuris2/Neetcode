# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def recursiveHelper(root):
            if not root:
                return [True, 0]
            
            l_info = recursiveHelper(root.left)
            r_info = recursiveHelper(root.right)

            boole = l_info[0] and r_info[0] and abs(r_info[1] - l_info[1]) <= 1

            return [boole, 1 + max(r_info[1], l_info[1])]
        return recursiveHelper(root)[0]


