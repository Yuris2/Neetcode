# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        #Root, Left, Right 
        self.pre = 0
        #Left, Root, Right
        inorderIndex = {}
        for i, elem in enumerate(inorder):
            inorderIndex[elem] = i
        
        def dfs(l,r):
            if l > r:
                return None
            
            elem = preorder[self.pre]
            node = TreeNode(elem)

            self.pre += 1
            mid = inorderIndex[elem]

            node.left = dfs(l, mid - 1)
            node.right = dfs(mid + 1, r)

            return node
        
        return dfs(0, len(preorder) - 1)
        