class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        adjList = {c:set() for w in words for c in w}

        for i in range(len(words) - 1):
            w1,w2 = words[i], words[i + 1]
            minLen = min(len(w1), len(w2))

            if len(w1) > len(w2) and w1[:minLen] == w2[:minLen]:
                return ""
            else:
                for j in range(minLen):
                    if w1[j] != w2[j]:
                        adjList[w1[j]].add(w2[j])
                        break
        
        #False = Done, True = Visiting
        path = {}
        res = []

        def dfs(char):
            if char in path:
                return path[char]
            
            path[char] = True

            for n in adjList[char]:
                if dfs(n):
                    return True
            
            path[char] = False
            res.append(char)
        
        for char in adjList.keys():
            if dfs(char):
                return ""
        
        res.reverse()
        return "".join(res)


        