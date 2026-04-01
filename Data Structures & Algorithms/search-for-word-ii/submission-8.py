class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False
    
    def addWord(self, word):
        curr = self
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.endOfWord = True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        R,C = len(board), len(board[0])
        root = TrieNode()

        for word in words:
            root.addWord(word)
        
        res = set()
        seen = set()

        def back(r,c,node,word):
            if r < 0 or c < 0 or r >= R or c >= C:
                return 
            if board[r][c] not in node.children or (r,c) in seen:
                return
            
            node = node.children[board[r][c]]
            word += board[r][c]

            if node.endOfWord:
                res.add(word)
            
            seen.add((r,c))
            
            back(r + 1, c, node, word)
            back(r - 1, c, node, word)
            back(r, c + 1, node, word)
            back(r, c - 1, node, word)

            seen.remove((r,c))

            return
        
        for r in range(R):
            for c in range(C):
                back(r,c,root, "")
        
        return list(res)

            


        