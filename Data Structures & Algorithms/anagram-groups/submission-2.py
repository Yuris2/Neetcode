class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = {}

        for s in strs:
            letters = [0] * 26

            for c in s:
                index = ord(c) - ord('a')
                letters[index] += 1
            
            lettersKey = tuple(letters)

            if lettersKey in res:
                res[lettersKey].append(s)
            else:
                res[lettersKey] = [s]
        
        return res.values()
        