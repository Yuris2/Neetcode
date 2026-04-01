class Solution:
    def addBinary(self, a: str, b: str) -> str:
        m = len(a) - 1
        n = len(b) - 1
        res = []
        carry = 0

        while m >= 0 or n >= 0 or carry > 0:
            digit1 = a[m] if m >= 0 else 0
            digit2 = b[n] if n >= 0 else 0

            total = int(digit1) + int(digit2) + carry

            res.append(str(total % 2))
            carry = total // 2

            m -= 1
            n -= 1
        
        res.reverse()
        return "".join(res)
