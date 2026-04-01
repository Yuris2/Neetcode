import collections

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)

        for s in strs:
            ordS = [0] * 26

            for c in s:
                ordS[ord(c) - ord('a')] += 1
            
            key = tuple(ordS)

            groups[key].append(s)
        
        return list(groups.values())

        