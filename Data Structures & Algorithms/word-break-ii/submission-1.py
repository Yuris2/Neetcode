class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        res = []
        stack = []

        words = set(wordDict)

        def backtrack(i):

            if i >= len(s):
                res.append(" ".join(stack))
                return

            
            for j in range(i,len(s)):
                if s[i:j + 1] in words:
                    stack.append(s[i:j + 1])
                    backtrack(j + 1)
                    stack.pop()
            #Check if any of the words can be formed from substring index by index
            #I want to go down the rabbit hole, add to current level and check future indexes
            #I want to check other possibilites
        
        backtrack(0)
        return res
        