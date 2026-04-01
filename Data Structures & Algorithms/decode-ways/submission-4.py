class Solution:
    def numDecodings(self, s: str) -> int:

        #Decode a string of digits
        #Given some string of digits
        #Only add 1 if we found a way to decode the string
        def back(i):
        #Brute Force Algo
            #While we are in the string

            if i >= len(s):
                return 1
            if s[i] == '0':
                return 0
            #1. Any single digit number can be mapped
            res = 0
            res += back(i + 1)

            if (i + 1) < len(s):
                if s[i] == '1' or (s[i] == '2' and int(s[i + 1]) < 7):
                    res += back(i + 2)

            return res
        
        return back(0)



        #Convert it into an integer
            #Represents number of ways you can map to
            #a letter combination

        