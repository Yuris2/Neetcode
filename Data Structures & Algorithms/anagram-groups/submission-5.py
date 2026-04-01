class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = []
        group = {}

        for s in strs:
            word = [0] * 26

            for c in s:
                word[ord(c) - ord('a')] += 1
            
            word = tuple(word)

            if word in group:
                group[word].append(s)
            else:
                group[word] = [s]
        
        return list(group.values())


        