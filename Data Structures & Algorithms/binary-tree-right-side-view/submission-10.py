# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import collections 
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        if not root:
            return res
        
        queue = deque()
        queue.append(root)

        while queue:
            last = None
            for _ in range(len(queue)):
                node = queue.popleft()
                last = node.val
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
 
            res.append(last)
        
        return res
        
            


        