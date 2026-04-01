# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

#[Left, Root, Right]
#Pre
#[Root, Left, Right]
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        inorderIndex = {}
        for i, elem in enumerate(inorder):
            inorderIndex[elem] = i
        
        self.pre = 0

        def dfs(l,r):
            if l > r:
                return None
            
            rootVal = preorder[self.pre]
            node = TreeNode(rootVal)
            self.pre += 1

            mid = inorderIndex[rootVal]
            node.left = dfs(l, mid - 1)
            node.right = dfs(mid + 1, r)

            return node

        return dfs(0, len(preorder) - 1)
        