class Solution:

    def encode(self, strs: List[str]) -> str:
        #Encoded string = len(s) + # + str
        encodedStr = ""
        for s in strs:
            encodedStr += str(len(s)) + "#"+ s
        
        return encodedStr

    def decode(self, s: str) -> List[str]:
        res = []
        if len(s) == 0:
            return res
        
        currentIndex = 0

        while currentIndex < len(s):
            index = currentIndex

            while s[index] != '#':
                index += 1
            
            lengthOfStr = s[currentIndex: index]
            lengthOfStr = int(lengthOfStr)

            string = s[index + 1: index + lengthOfStr + 1]
            res.append(string)
            currentIndex = index + lengthOfStr + 1
        
        return res

