# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        #preorder = [3, 9, 20, 15, 7]
        #               p
        #inorder  = [9, 3, 15, 20, 7]
        #            l  i           r

        #                   3
        #

        inorderIndex = {}

        for i, elem in enumerate(inorder):
            inorderIndex[elem] = i

        self.pre = 0
        #Bounds for left/right subtree in inorder
        def dfs(l,r):
            if l > r:
                return None

            val = preorder[self.pre]
            node = TreeNode(val)

            i = inorderIndex[val]
            self.pre += 1

            node.left = dfs(l,i - 1)
            node.right = dfs(i + 1, r)

            return node
        
        return dfs(0, len(preorder) - 1)

        