class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        adjList = {c:set() for w in words for c in w}

        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i + 1]
            minLen = min(len(w1), len(w2))

            for i in range(minLen):
                if w1[i] != w2[i]:
                    adjList[w1[i]].add(w2[i])
                    break
                #a,b,c => a,b
                if len(w1) > len(w2) and i == len(w2) - 1:
                    return ""
        
        res = []
        #c = True, False
        #True = Done, False = Visiting
        path = {}

        def dfs(ch):
            if ch in path:
                return path[ch]
            
            path[ch] = False

            for c in adjList[ch]:
                if not dfs(c):
                    return False

            res.append(ch)
            path[ch] = True
            return True
        
        for c in adjList:
            if not dfs(c):
                return ""
        
        res.reverse()
        return "".join(res)

        