# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        inorderMap = {}
        for index, value in enumerate(inorder):
            inorderMap[value] = index
        
        preOrderIndex = [0]
        
        return self.buildTreeRecursion(inorderMap, preorder, preOrderIndex, 0, len(preorder) - 1)
    
    def buildTreeRecursion(self, inorderMap, preorder, index, left, right):
        if left > right:
            return None
        rootVal = preorder[index[0]]
        index[0] += 1
        rootIndex = inorderMap[rootVal]
        root = TreeNode(rootVal)

        root.left = self.buildTreeRecursion(inorderMap, preorder, index, left, rootIndex - 1)
        root.right = self.buildTreeRecursion(inorderMap, preorder, index, rootIndex + 1, right)

        return root


        