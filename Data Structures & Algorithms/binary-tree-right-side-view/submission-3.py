# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        queue = []

        if root:
            queue.append(root)

        while queue:
            res.append(queue[-1].val)

            n = len(queue)
            
            for i in range(n):
                node = queue.pop(0)

                if node.left:
                    queue.append(node.left)
                
                if node.right:
                    queue.append(node.right)
        
        return res

        