# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        #Essentially we are doing a in-order traversal and decremnting k
        #Brute-Force Approach, Add all elements to an array and then sort the array

        self.elem = None
        self.curr = k

        def dfs(root):
            if not root:
                return
            
            dfs(root.left)
            self.curr -= 1
            if self.curr == 0:
                self.elem = root.val
                return
            
            dfs(root.right)

            return
        
        dfs(root)
        return self.elem