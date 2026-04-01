class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        delimiter = '#'

        for s in strs:
            res += str(len(s)) + delimiter + s
        
        return res
    '''
    #read = 0
    #ptr = 1
    #string = s[2:4]
    3#yay2#no
    '''
    def decode(self, s: str) -> List[str]:
        res = []
        read = 0
        length = len(s)

        while read < len(s):
            ptr = read
            length = ""
            
            #Finding the lenght/num of chars after
            #delimiter
            while s[ptr] != '#':
                length += s[ptr]
                ptr += 1
            
            length = int(length)
            #Read so characters after the delimiter
            string = s[ptr + 1: ptr + length + 1]

            #Add character to string and adjust pointers
            res.append(string)
            read = ptr + length + 1
        
        return res

            

