class Solution:
    def groupAnagrams(self, strs):
        groups = {}

        for word in strs:
            letters = [0] * 26

            for c in word:
                index = ord(c) - ord('a')
                letters[index] += 1
            
            letters = tuple(letters)

            if letters in groups:
                groups[letters].append(word)
            else:
                groups[letters] = [word]
        
        return groups.values()
            
            
            

        