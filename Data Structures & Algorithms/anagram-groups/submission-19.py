class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        countMap = defaultdict(list) # count arrays -> list of strs

        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord("a")] += 1
            countMap[tuple(count)].append(s)
    
        res = list(countMap.values())

        return res

        


