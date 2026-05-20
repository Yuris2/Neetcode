import collections
class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        adjList = {c:set() for w in words for c in w}

        for i in range(len(words) - 1):
            w1,w2 = words[i], words[i + 1]
            minLen = min(len(w1), len(w2))

            for i in range(minLen):
                if w1[i] != w2[i]:
                    adjList[w1[i]].add(w2[i])
                    break
                if len(w1) > len(w2) and i == len(w2) - 1:
                    return ""
        
        seen = set()
        done = set()

        res = []

        def dfs(c):
            if c in done:
                return True
            if c in seen:
                return False
            
            seen.add(c)

            for child in adjList[c]:
                if not dfs(child):
                    return False
            
            seen.remove(c)
            done.add(c)
            res.append(c)
            return True
        
        for c in adjList:
            if not dfs(c):
                return ""
        
        res.reverse()
        return "".join(res)

        