# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        inorderToIndex = {}
        for i in range(len(inorder)):
            inorderToIndex[inorder[i]] = i

        preorderIndex = [0]

        return self.buildTreeRecursion(inorderToIndex, preorder, preorderIndex, 0, len(preorder) - 1)
    
    def buildTreeRecursion(self, inorderToIndex, preorder, preIndex, left, right):
        if left > right:
            return None

        rootVal = preorder[preIndex[0]]
        preIndex[0] += 1
        root = TreeNode(rootVal)
        index = inorderToIndex[rootVal]

        root.left = self.buildTreeRecursion(inorderToIndex, preorder, preIndex, left, index - 1)
        root.right = self.buildTreeRecursion(inorderToIndex, preorder, preIndex, index + 1, right)

        return root
        