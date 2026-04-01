import collections
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = []
        counter = defaultdict(list)

        for s in strs:
            barcode = [0] * 26

            for c in s:
                letter = ord(c) - ord('a')
                barcode[letter] += 1
            
            counter[tuple(barcode)].append(s)
        
        for item in counter.values():
            res.append(item)
        
        return list(res)
            

        