class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        adjList = {c:set() for w in words for c in w}

        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i + 1]
            minLen = min(len(w1), len(w2))

            for j in range(minLen):
                if w1[j] != w2[j]:
                    adjList[w1[j]].add(w2[j])
                    break
                if len(w1) > len(w2) and j == len(w2) - 1:
                    return ""
        
        #c: True/ False
        path = {}
        res = []

        def dfs(ch):
            if ch in path:
                return path[ch]
            
            path[ch] = False

            for c in adjList[ch]:
                if not dfs(c):
                    return False
            
            path[ch] = True
            res.append(ch)

            return True
        
        for c in adjList:
            if not dfs(c):
                return ""
        
        res.reverse()
        return "".join(res)
        