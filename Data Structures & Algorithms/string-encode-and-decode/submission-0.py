class Solution:
    def encode(self, strs: List[str]) -> str:
        #Encoded str
        #Length#str
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s
        
        return res

    def decode(self, s: str) -> List[str]:
        #Original Str
        res = []
        if len(s) < 0:
            return res
        
        currentIndex = 0

        while currentIndex < len(s):
            #find the lenth str
            index = currentIndex
            #increment up until the seperator
            while s[index] != "#":
                index += 1
            #length = currentIndex to char right before seperator
            length = int(s[currentIndex: index])
            #Add the str after delimeter with new length
            resStr = s[index + 1: index + 1 + length]
            #Append the string to res
            res.append(resStr)
            #Jumping to next series
            currentIndex = index + 1 + length
        
        return res
