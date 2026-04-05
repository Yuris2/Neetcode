class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        #Split into as many substrings as possible
        #Each letter in the string has to be present in its substring
        #And not present in any other substring

        #Return a list of the size of the substrings in order
        #Which they occur

        #Solution Intuition
        occ = {}
        res = []

        for i in range(len(s)):
            occ[s[i]] = i
        #We want to find the last occurence of every letter
        far = 0
        #Starting point of substring
        prevEnd = 0
        #Iterate through the string, keep track of the  (Greedy)
        for i in range(len(s)):
            far = max(far, occ[s[i]])

            if i == far:
                res.append(far - prevEnd + 1)
                prevEnd = i + 1
        
        return res
        #furthest jump that we can have based on the letter
        #Whenever we hit the futhest jump, entire substring
        #Start again until end of string
        