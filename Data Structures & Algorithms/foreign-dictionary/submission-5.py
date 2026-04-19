class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        #Want to map out characters to the words the come before
        adjList = {c:set() for w in words for c in w}

        #Iterate over each pair of words
        for i in range(len(words)-1):
            w1, w2 = words[i], words[i + 1]
            minLen = min(len(w1), len(w2))

            #Find where the first character differs
            for i in range(minLen):
                #ch1 comes for ch2
                if w1[i] != w2[i]:
                    adjList[w1[i]].add(w2[i])
                    break
                #abc, ab -> not valid ordering
                if len(w1) > len(w2) and i == len(w2) - 1:
                    return ""

        #Derive the order using topological sort
        #ch: T or F
        #T = Done
        #F = Visiting
        path = {}
        res = []

        def dp(ch):
            if ch in path:
                return path[ch]

            #Visiting this character
            path[ch] = False

            for child in adjList[ch]:
                if not dp(child):
                    return False

            path[ch] = True
            res.append(ch)
            return True

        for c in adjList:
            if not dp(c):
                return ""

        res.reverse()
        return "".join(res)      