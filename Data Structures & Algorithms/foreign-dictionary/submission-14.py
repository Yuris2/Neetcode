class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        adjList = {c:set() for w in words for c in w}
        res = ""

        for i in range(len(words) - 1):
            w1,w2 = words[i], words[i + 1]
            minLen = min(len(w1), len(w2))

            for j in range(minLen):
                if w1[j] != w2[j]:
                    adjList[w1[j]].add(w2[j])
                    break
                if len(w1) > len(w2) and j == len(w2) - 1:
                    return res

        res = []
        visit = set()
        done = set()

        def dp(ch):
            if ch in done:
                return True
            if ch in visit:
                return False

            visit.add(ch)

            for c in adjList[ch]:
                if not dp(c):
                    return False
            
            visit.remove(ch)
            res.append(ch)
            done.add(ch)
            
            return True
        
        for c in adjList:
            if not dp(c):
                return ""
        
        res.reverse()
        return "".join(res)
            
                 