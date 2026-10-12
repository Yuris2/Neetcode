class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hM = defaultdict(list) # [countArr of chars and freqs] : arr[strs that match]

        for s in strs:
            countArr = [0] * 26
            for c in s:
                countArr[ord(c) - ord("a")] += 1
            hM[tuple(countArr)].append(s)
        
        return list(hM.values())


