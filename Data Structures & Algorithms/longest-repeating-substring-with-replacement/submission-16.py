class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        #Return the length of the longest substring with k replacements
        #Sliding Window Approach
        #Keep track of the count of each character
        counter = {}
        res = 0
        #With a start and end pointer
        start = 0
        #Check if the current size of the window < max count + k:
        for end in range(len(s)):
            counter[s[end]] = 1 + counter.get(s[end],0)
            #Case 2 (No):
                #Adjust the window until yes
            while (end - start + 1) > max(counter.values()) + k:
                counter[s[start]] -= 1
                start += 1

            #Compare result
            res = max(res, end - start + 1)
        
        return res

        
        #Return the max

                
        