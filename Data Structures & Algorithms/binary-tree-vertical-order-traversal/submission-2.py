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
        colToNode = defaultdict(list)

        if not root:
            return res
        
        queue = deque()
        queue.append((root, 0))

        minRow = 0
        maxRow = 0

        while queue:
            for n in range(len(queue)):
                node, col = queue.popleft()
                colToNode[col].append(node.val)

                minRow = min(minRow, col)
                maxRow = max(maxRow, col)

                if node.left:
                    queue.append((node.left, col - 1))
                if node.right:
                    queue.append((node.right, col + 1))
        
        for col in range(minRow, maxRow + 1):
            res.append(colToNode[col])
        
        return res
        


        