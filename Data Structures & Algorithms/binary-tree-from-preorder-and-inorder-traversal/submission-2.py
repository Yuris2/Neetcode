# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        mp = {}
        for i, v in enumerate(inorder):
            mp[v] = i
        
        preIndex = [0]

        return self.buildTreeRec(mp, preorder, preIndex, 0, len(preorder) -1)
    
    def buildTreeRec(self, inorder, preorder, indexOfPre, left, right):
        if left > right:
            return None
        
        rootVal = preorder[indexOfPre[0]]
        indexOfPre[0] += 1
        index = inorder[rootVal]
        root = TreeNode(rootVal)

        root.left = self.buildTreeRec(inorder, preorder, indexOfPre, left, index - 1)
        root.right = self.buildTreeRec(inorder, preorder, indexOfPre, index + 1, right)

        return root



        