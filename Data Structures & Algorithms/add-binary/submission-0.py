class Solution:
    def addBinary(self, a: str, b: str) -> str:
        res = ""
        carry = 0
        a, b = a[::-1], b[::-1]
        for i in range(max(len(a), len(b))):
            a_digit = int(a[i]) if i < len(a) else 0
            b_digit = int(b[i]) if i < len(b) else 0
            total = a_digit + b_digit + carry
            char = str(total % 2)
            carry = total // 2
            res = char + res
        
        if carry:
            res = "1" + res
        
        return res