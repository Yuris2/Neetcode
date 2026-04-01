class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = len(digits)

        for i in range(n -1, -1 , -1):
            #Carry flag == 0
            if digits[i] < 9:
                digits[i] += 1
                return digits
            #Carry 
            else:
                digits[i] = 0
        
        return [1] + digits
        