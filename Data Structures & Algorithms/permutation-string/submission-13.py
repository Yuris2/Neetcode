import collections
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        countS = Counter(s1)
        countW = defaultdict(int)

        for i in range(len(s1)):
            countW[s2[i]] += 1
        
        if countS == countW:
            return True
        
        for i in range(len(s2) - len(s1)):
            countW[s2[i]] -= 1
            if countW[s2[i]] == 0:
                del countW[s2[i]]
            countW[s2[i + len(s1)]] += 1

            if countW == countS:
                return True
        
        return False





        