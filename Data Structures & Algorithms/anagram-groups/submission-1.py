class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = {}

        while len(strs) != 0:
            lastString = strs.pop()

            #Barcode kinda thing
            letters = [0] * 26
            for c in lastString:
                letter = ord(c) - ord('a')
                letters[letter] += 1
            
            letterKey = tuple(letters)

            if letterKey in dic:
                dic[letterKey].append(lastString)
            else:
                dic[letterKey] = [lastString]
        
        return dic.values()
        