# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import collections
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        if not root:
            return res
        
        queue = deque()
        queue.append((root, 0))
        colToNode = defaultdict(list)

        minCol, maxCol = 0,0

        while queue:
            for i in range(len(queue)):
                node, col = queue.popleft()

                minCol = min(col, minCol)
                maxCol = max(col, maxCol)

                colToNode[col].append(node.val)

                if node.left:
                    queue.append((node.left, col - 1))
                
                if node.right:
                    queue.append((node.right, col + 1))
        
        for i in range(minCol, maxCol + 1):
            res.append(colToNode[i])
        
        return res


        