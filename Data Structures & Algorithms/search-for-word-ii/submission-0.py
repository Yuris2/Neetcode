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
        res, seen = set(), set()
        #Populating the TrieNode
        root = TrieNode()

        for w in words:
            root.addWord(w)

        def backtrack(r,c, trieNode ,word):
            if r < 0 or c < 0 or r >= R or c >= C:
                return
            if (r,c) in seen or board[r][c] not in trieNode.children:
                return

            seen.add((r,c))
            trieNode = trieNode.children[board[r][c]]
            word += board[r][c]

            if trieNode.endOfWord:
                res.add(word)
 
            backtrack(r+1,c,trieNode,word)
            backtrack(r,c+1,trieNode,word)
            backtrack(r-1,c,trieNode,word)
            backtrack(r,c-1,trieNode,word)

            seen.remove((r,c))
        
        for r in range(R):
            for c in range(C):
                backtrack(r,c, root, "")

        return list(res)
        

        
        