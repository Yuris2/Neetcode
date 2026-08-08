# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        inorderIndex = {}
        for i, val in enumerate(inorder):
            inorderIndex[val] = i

        self.pre= 0
        
        def dfs(l,r):
            if l > r:
                return None
            
            val = preorder[self.pre]
            node = TreeNode(val)
            self.pre += 1

            index = inorderIndex[val]
            node.left = dfs(l, index - 1)
            node.right = dfs(index + 1, r)

            return node
        
        return dfs(0, len(preorder) - 1)
        #Preorder = [root, left, right]
        #Inorder = [left, root, right]
        