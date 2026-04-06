class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        #Multiply the product of num1 and num2
            #No leading 0's except if 0
        #Res should be a string
        m,n = len(num1), len(num2)
        res = [0] * (m + n)

        if num1 == '0' or num2 == '0':
            return '0'

        #Multiplying each possible digit pair (i,j)
        for i in range(len(num1)):
            for j in range(len(num2)):
                digit1 = ord(num1[i]) - ord('0')
                digit2 = ord(num2[j]) - ord('0')
                res[i + j + 1] += (digit1 * digit2)
        
        #Resolving each carry
        carry = 0
        for i in range(len(res) - 1, -1, -1):
            res[i] += carry
            carry = res[i] // 10
            if res[i] > 9:
                res[i] = res[i] % 10
        
        while res and res[0] == 0:
            res.pop(0)
        
        return "".join(str(dig) for dig in res)
                

        