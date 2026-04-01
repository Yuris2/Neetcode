class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = {}

        while (len(strs) > 0):

            lastWord = strs.pop()
            letters = [0] * 26

            for c in lastWord:
                index = ord(c) - ord('a')
                letters[index] += 1
            
            lettersKey = tuple(letters)

            if lettersKey in dic:
                dic[lettersKey].append(lastWord)
            else:
                dic[lettersKey] = [lastWord]

        return dic.values()

            
        