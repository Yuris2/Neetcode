# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        stream = []

        def preorder(root):
            if not root:
                stream.append("N")
                return None
            
            stream.append(str(root.val) )
            preorder(root.left)
            preorder(root.right)

            return root
        
        preorder(root)
        return "|".join(stream)
        


        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        data = data.split("|")
        self.pre = 0

        def dfs():
            if data[self.pre] == "N":
                self.pre += 1
                return None
            
            rootVal = data[self.pre]
            root = TreeNode(rootVal)
            self.pre += 1

            root.left = dfs()
            root.right = dfs()

            return root
        
        return dfs()
