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
        
        currIndex = 0
        while currIndex < len(s):
            index = currIndex
            #Look for the #
            while s[index] != '#':
                index += 1
            
            lengthOfStr = int(s[currIndex:index])
            string = s[index + 1:index + lengthOfStr + 1]
            currIndex = index + lengthOfStr + 1

            res.append(string)
            #Read characters past delimeter
            #Add to result
        return res
