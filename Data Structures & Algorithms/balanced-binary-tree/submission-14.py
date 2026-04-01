# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def balanceHelper(root):
            if not root:
                return (True, 0)
            
            l_info = balanceHelper(root.left)
            r_info = balanceHelper(root.right)

            return (l_info[0] and r_info[0] and 
            abs(l_info[1] - r_info[1]) <= 1, 
            1 + max(l_info[1], r_info[1]))
        return balanceHelper(root)[0]
        

        
        