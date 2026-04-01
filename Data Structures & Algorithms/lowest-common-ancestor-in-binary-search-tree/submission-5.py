# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        currentNode = root
        while currentNode:
            if currentNode.val < p.val and currentNode.val < q.val:
                currentNode = currentNode.right
            elif currentNode.val > p.val and currentNode.val > q.val:
                currentNode = currentNode.left
            else:
                return currentNode
        
        return None
        