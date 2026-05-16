class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        countToStrings = defaultdict(list)

        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord("a")] += 1
            
            countToStrings[tuple(count)].append(s)

        return list(countToStrings.values())



        
