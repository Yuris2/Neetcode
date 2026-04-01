# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return root
        
        if key < root.val:
            #Go left
            root.left = self.deleteNode(root.left, key)
        elif key > root.val:
            #Go right
            root.right = self.deleteNode(root.right, key)
        else:
            #We found the node
            if not root.left:
                return root.right
            elif not root.right:
                return root.left

            #Delete the min value in the right subtree          
            cur = root.right
            while cur.left:
                cur = cur.left
            #Deleting the node by swapping values and deleting the old node
            root.val = cur.val
            #returns none since there is no left, which essentially deletes the node
            root.right = self.deleteNode(root.right, root.val)

        return root

        