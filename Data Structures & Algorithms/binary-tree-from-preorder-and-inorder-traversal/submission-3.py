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
        
        indexAtPre = [0]

        return self.buildTreeRec(inorderToIndex, preorder, indexAtPre, 0, len(preorder) - 1)

    

    def buildTreeRec(self, inorderToIndex, preorder, preIndex, left, right):
        if left > right:
            return None
        rootVal = preorder[preIndex[0]]
        indexInorder  = inorderToIndex[rootVal]
        root = TreeNode(rootVal)
        preIndex[0] += 1

        root.left = self.buildTreeRec(inorderToIndex, preorder, preIndex, left, indexInorder - 1)
        root.right = self.buildTreeRec(inorderToIndex, preorder, preIndex, indexInorder + 1, right)

        return root
        