class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False
    
    def addWord(self, w):
        curr = self
        for c in w:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.endOfWord = True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        #Given a list of strings, return all words that are present in the grid
        #Same cell cannot be used more than once in a word
        R,C = len(board), len(board[0])
        trie = TrieNode()

        for c in words:
            trie.addWord(c)
        
        seen = set()
        res = set()

        def back(r,c,root,word):
            if r < 0 or r >= R or c < 0 or c >= C:
                return

            ch = board[r][c]
            if (r,c) in seen or ch not in root.children:
                return
            
            root = root.children[ch]
            word += ch
            seen.add((r,c))

            if root.endOfWord:
                res.add(word)

            back(r+1,c,root, word)
            back(r,c+1,root, word)
            back(r-1,c,root, word)
            back(r,c-1,root, word)

            seen.remove((r,c))
            
        for r in range(R):
            for c in range(C):
                back(r,c,trie,"")
        
        return list(res)
            
        #Solution Intuition
            #Go through each letter
                #Check if the letter matches the starting letter of a word
                #Check directions and continue if it matches the next letter
                #If we have built a word, add it to a list
        