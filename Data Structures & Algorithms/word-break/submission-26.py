class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        #We want to see if we can build the current string with the words in 
        #the dictionary
        words = set(wordDict)
        cache = {}

        def back(i):
            if i >= len(s):
                return True
            if i in cache:
                return cache[i]
            
            for j in range(i, len(s)):
                if s[i:j + 1] in words:
                    res = back(j + 1)
                    if res:
                        cache[i] = True
                        return True
            
            cache[i] = False
            return False
        
        return back(0)

        #Step 1.
        #   Have a starting point called i
        #Step 2.
        #   Scan right from i until we found a word that is present in the dict
        #Step 2b. 
        #   If we find a word that is present in the dict:
        #       Update our starting point (1.)
        #Step 3.
        #   #If our pointer hits the end of the string:
                #We can construct and return True
            #If not:
                #Return False
        