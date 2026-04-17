import collections
class Solution:
    def foreignDictionary(self, words: List[str]) -> str:      
        #Constructing initial adjList. Used to cover char without children
        adjList = {c:set() for w in words for c in w}

        #Iterating over each pair in words to find first differing char:
        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i + 1]
            #Iterating over the minimum length to avoid out of bounds
            n = min(len(w1), len(w2))

            #After first differing char, rest tell u nothing
            for i in range(n):
                if w1[i] != w2[i]:
                    #c1 comes before c2
                    adjList[w1[i]].add(w2[i])
                    break
                #abc, ab (invalid ordering)
                if len(w2) < len(w1) and i == n - 1:
                    return ""
        
        #Nodes we have seen in the current path (False = Visiting, True = Done)
        path = {}
        res = []

        #Post order traversal
        #Append to result if no children
        def dfs(ch):
            if ch in path:
                return path[ch]
            
            path[ch] = False

            for child in adjList[ch]:
                if not dfs(child):
                    return False
            
            path[ch] = True
            res.append(ch)
            return True
        
        for c in adjList:
            if not dfs(c):
                return ""
        
        #a->b->c will be seen as [c,b,a]
        res.reverse()
        return "".join(res)
            
            


        #Foreign language and we are trying to derive the order of letters in the language 
        #The string is already lexographically sorted (small -> greatest)
            #a is smaller than b if
                #first different letter is smaller in a than in b
                #a is a prefix of b
        #Return "", if the order is valid
        #If there are multiple valid orders of letters, return any of them        