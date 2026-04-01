class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 0
        res = []
        index = 0
        digits.reverse()

        while index < len(digits):
            digit = digits[index]
            digit += 1
            index += 1

            carry = digit // 10
            digit = digit % 10

            res.append(digit)
            if carry == 0:
                break
        
        while index < len(digits):
            res.append(digits[index])
            index += 1
        
        if carry != 0:
            res.append(carry)

        
        res.reverse()
        return res
        