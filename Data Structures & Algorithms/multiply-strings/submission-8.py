class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        #If num1 == 0 or num2 == 0: result will always be 0
        if num1 == '0' or num2 == '0':
            return '0'

        n,m = len(num1), len(num2)
        res = [0] * (n + m)

        #How do we multiply:
        #Iterate digit by digit backwards
        for i in range(n - 1, -1, -1):
            for j in range(m - 1, -1, -1):
                    #Use the ord function to extract ind. digits
                d1 = ord(num1[i]) - ord('0')
                d2 = ord(num2[j]) - ord('0')
                #Set the result of (i + j) equal to prod of digits
                res[i + j + 1] += d1 * d2
                #Deal with carries after finishing multiplication
        #Deal with carries
        carry = 0
        #Iterate over each digit backwards adding carry
        for i in range(len(res) - 1, -1, -1):
            #Extract Carry (//10)
            res[i] += carry
            carry = res[i] // 10
            #If greater than = 10
            if res[i] >= 10:
                #Extract Last Digit (%10)
                res[i] = res[i] % 10

        #Clean the result
        while res and res[0] == 0:
            #Remove '0' from front of array
            res.pop(0)
        #Join the array
        return "".join(str(d) for d in res)

        #12 * 21

        #[2,2]
            
        