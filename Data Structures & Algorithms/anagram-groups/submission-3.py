class Solution:
    def groupAnagrams(self, strs):
        res = []
        groups = {}

        for s in strs:
            counter = [0] * 26

            for c in s:
                index = ord(c) - ord('a')
                counter[index] += 1
            
            counter = tuple(counter)

            if counter in groups:
                groups[counter].append(s)
            else:
                groups[counter] = [s]
        
        return groups.values()
            
            
            

        