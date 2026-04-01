class Solution:
    def addBinary(self, a: str, b: str) -> str:
        m = len(a) - 1
        n = len(b) - 1
        carry = 0
        res = []

        while m >= 0 or n >= 0 or carry > 0:
            if m >= 0:
                add1 = int(a[m])
            else:
                add1 = 0
            
            if n >= 0:
                add2 = int(b[n])
            else: 
                add2 = 0
            
            val = add1 + add2 + carry
            res.append(str(val % 2))
            carry = val // 2

            m -= 1
            n -= 1
            
        res.reverse()
        return "".join(res)
            