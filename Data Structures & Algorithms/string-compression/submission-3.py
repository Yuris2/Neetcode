class Solution:
    def compress(self, chars: List[str]) -> int:
        #Pointer that we writ to
        l = 0
        #Pointer that reads the characters
        r = 0

        #Keep track that the pointer is in range and equal to 
        while r < len(chars):
        #character that we are reading
            c = chars[r]
            length = 0

            while r < len(chars) and chars[r] == c:
                length += 1
                r += 1
            
            chars[l] = c
            l += 1

            if length > 1:
                for d in str(length):
                    chars[l] = d
                    l += 1
            
        return l





        #If the length > 1:
            #Write the digit to every write position
            #Increment write by one

                    


            
            


            

            


        