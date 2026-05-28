# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        res = []
        self.pre = 0

        def dfs(node):
            if not node:
                res.append("N")
                return 
            
            res.append(str(node.val))
            dfs(node.left)
            dfs(node.right)
        
        dfs(root)
        return "|".join(res)

        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        stream = data.split("|")
        self.pre = 0

        def dfs():
            ch = stream[self.pre]
            if ch == "N":
                self.pre += 1
                return None
            
            node = TreeNode(int(ch))
            self.pre += 1
            node.left = dfs()
            node.right = dfs()

            return node
        
        return dfs()
            

