class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        #Pattern
            #Using python functions to convert and operate
            #on numerical strings, rudimentary operations
        
        #General Idea
            #Create an array w/len(max(result)) using ord to parse
            #and multiply each number from 1 and 2 together. Deal
            #with carries at the end
        
        n,m = len(num1), len(num2)
        res = [0] * (n + m)

        if num1 == '0' or num2 == '0':
            return '0'

        for i in range(n - 1, -1, -1):
            for j in range(m - 1, -1, -1):
                d1 = ord(num1[i]) - ord('0')
                d2 = ord(num2[j]) - ord('0')

                res[i + j + 1] += (d1 * d2)
        
        carry = 0

        for i in range(len(res) - 1, -1, -1):
            res[i] += carry
            carry = res[i] // 10

            if res[i] > 9:
                res[i] = res[i] % 10

        while res and res[0] == 0:
            res.pop(0)
        
        return "".join(str(d) for d in res)
        