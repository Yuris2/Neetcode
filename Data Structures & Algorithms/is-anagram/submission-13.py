# the two strings are anagrams if:
    # they have the same characters
    # each character has the same amount of instances
# that means that we can immediately check if they aren't anagrams
    # check if the lengths of the two strings aren't equal immediately
# create hashmaps for both string inputs
    # hashmaps will have the characters of strings as keys
    # number of instances for each character will be values
# iterate through each character of the strings
    # add + 1 to the value of a key for each instance
    # initialize the default value for each key as 0
# check if the length of the hashmaps (how many keys) AREN'T equal
    # this will tell you instantly that they aren't anagrams
# check if the hashmaps are equal
    #return True


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        countS, countT = {}, {}
        
        for i in range(len(s)):
            countS[s[i]] = countS.get(s[i],0) + 1
            countT[t[i]] = countT.get(t[i],0) + 1
        
        return countS == countT
        
    
