class Solution:
    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s)) + "#"+ s
        return res

    def decode(self, s: str) -> List[str]:
        res = []

        if not s:
            return res

        index = 0
        while index < len(s):
            currentIndex = index

            while s[currentIndex] != '#':
                currentIndex += 1
            
            lengthOfStr = s[index:currentIndex]
            string = s[currentIndex + 1: currentIndex + int(lengthOfStr) + 1]
            res.append(string)

            index = currentIndex + int(lengthOfStr) + 1
        
        return res 

            

