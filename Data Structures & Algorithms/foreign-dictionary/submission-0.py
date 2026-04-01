import collections

class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        adjList = {c: set() for w in words for c in w}

        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i + 1]
            minLen = min(len(w1), len(w2))
            #Edge case
            if len(w1) > len(w2) and w1[:minLen] == w2[:minLen]:
                return ""  
            #Find which characters are different
            for j in range(minLen):
                if w1[j] != w2[j]:
                    #Assume w1[j] comes before w2[j]
                    adjList[w1[j]].add(w2[j])
                    break

        #False = Done, True = Still Visiting
        seen = {}    
        res = []

        #Post order traversal
        def dfs(letter):
            if letter in seen:
                return seen[letter]
            
            seen[letter] = True

            for neigh in adjList[letter]:
                if dfs(neigh):
                    return True
            
            seen[letter] = False
            res.append(letter)
        
        for c in adjList:
            if dfs(c):
                return ""
        
        res.reverse()
        return "".join(res)

            


            

