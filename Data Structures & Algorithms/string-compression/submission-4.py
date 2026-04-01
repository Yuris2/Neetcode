class Solution:
    def compress(self, chars: List[str]) -> int:
        write = 0
        read = 0
        #[a,a,a,b,b,b]
        # w     r
        # [a,3,b,3,b,b]
        #      w r
        while read < len(chars):
            length = 0
            ogChar = chars[read]

            while read < len(chars) and chars[read] == ogChar:
                length += 1
                read += 1
            
            chars[write] = ogChar
            write += 1

            if length > 1:
                for dig in str(length):
                    chars[write] = dig
                    write += 1
        
        return write
            


        