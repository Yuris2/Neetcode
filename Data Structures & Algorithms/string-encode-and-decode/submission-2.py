class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res = res + str(len(s)) +"#"+s
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        lastIndex = 0

        while lastIndex < len(s):
            index = lastIndex
            while s[index] != '#':
                index += 1
            
            lengthOfStr = s[lastIndex:index]
            lengthOfStr = int(lengthOfStr)
            string = s[index + 1: index + lengthOfStr + 1]
            res.append(string)
            lastIndex = index + lengthOfStr + 1
        
        return res
