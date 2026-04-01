class Solution:
    def addBinary(self, a: str, b: str) -> str:
        m = len(a) - 1
        n = len(b) - 1
        carry = 0
        res = []

        while m >= 0 or n >= 0 or carry > 0:
            val1 = a[m] if m >= 0 else 0
            val2 = b[n] if n >= 0 else 0
            total = int(val1) + int(val2) + carry
            res.append(str(total % 2))
            carry = total // 2
            m -= 1
            n -= 1
        
        res.reverse()
        return "".join(res)

