# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        #preorder traversal
        res = []
        def dfs(node):
            if not node:
                res.append("N")
                return None
            
            rootVal = node.val
            res.append(str(rootVal))
            dfs(node.left)
            dfs(node.right)

            return node
        
        dfs(root)
        return "|".join(res)

        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        stream = data.split("|")
        self.pre = 0

        def dfs():
            elem = stream[self.pre]
            if elem == "N":
                self.pre += 1
                return None
            
            root = TreeNode(elem)
            self.pre += 1
            root.left = dfs()
            root.right = dfs()

            return root
        
        return dfs()
