class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False
    
    def addWord(self, word):
        curr = self
        for ch in word:
            if ch not in curr.children:
                curr.children[ch] = TrieNode()
            curr = curr.children[ch]
        curr.endOfWord = True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        R,C = len(board), len(board[0])
        root = TrieNode()
        res = set()

        for w in words:
            root.addWord(w)
        
        seen = set()
        def back(r,c,node, word):
            if r < 0 or c < 0 or r >= R or c >= C:
                return
            ch = board[r][c]

            if (r,c) in seen or ch not in node.children:
                return
            
            word += ch
            node = node.children[ch]

            if node.endOfWord:
                res.add(word)
            
            seen.add((r,c))
            back(r+1,c,node, word)
            back(r,c+1,node, word)
            back(r-1,c,node, word)
            back(r,c-1,node, word)

            seen.remove((r,c))
        
        for r in range(R):
            for c in range(C):
                back(r,c,root, "")
        
        return list(res)

            



        
        