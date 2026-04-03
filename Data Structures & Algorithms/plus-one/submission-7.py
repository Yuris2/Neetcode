class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        #Array of digits
        #Digits[i] = ith digit of large integer
        #Ordered from most to least significant digit
        #[1,2,3,4]


        #How Do We Add One to Numbers?
            #Add to the Least Significant Bit
                #If their is a carry
                    #Set Value == 0
                    #Carry 1
                #Else:
                    #Add one and we are done
        
        #Do we need to keep track of a carry flag?
            #Not with one because we can see the Carry 1 Value
        
        #Algorithm
        #Iterate from LSD -> MSD:
        for i in range(len(digits) - 1, -1, -1):
            #Check if a carry will occur (digit == 9):
            #Yes
            if digits[i] == 9:
                #Set the digit == 0
                digits[i] = 0
                #Run to next digit
            else:
                digits[i] += 1
                return digits
        
        return [1] + digits
        #If we have iterated through all numbers, we have a carry
        #Return [1] + digit
        