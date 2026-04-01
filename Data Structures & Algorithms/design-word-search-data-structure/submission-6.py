class TrieNode():
    def __init__(self):
        self.children = {}
        self.endOfWord = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()
        

    def addWord(self, word: str) -> None:
        curr = self.root
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.endOfWord = True

    def search(self, word: str) -> bool:

        def dfs(j, root):
            curr = root

            for i in range(j,len(word)):
                ch = word[i]

                if ch == '.':
                    #Skipping a level, and running the search on all letters
                    for c in curr.children.values():
                        if dfs(i + 1, c):
                            return True
                    return False
                else:
                    if ch not in curr.children:
                        return False
                    curr = curr.children[ch]
            return curr.endOfWord
        
        return dfs(0, self.root)
        
