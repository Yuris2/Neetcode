# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
#preorder = [root, left, right]
#inorder = [left, root, right]
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        index = {}

        for i, elem in enumerate(inorder):
            index[elem] = i
        
        self.pre = 0
        def dfs(l,r):
            if l > r:
                return None
            
            rootVal = preorder[self.pre]
            node = TreeNode(rootVal)
            self.pre += 1

            idx = index[rootVal]
            node.left = dfs(l,idx - 1)
            node.right = dfs(idx + 1, r)

            return node
        
        return dfs(0, len(preorder) - 1)
        