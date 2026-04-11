import collections
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)

        for s in strs:
            letters = [0] * 26

            for c in s:
                letter = ord(c) - ord('a')
                letters[letter] += 1
            
            letters = tuple(letters)

            groups[letters].append(s)
        
        return list(groups.values())
        