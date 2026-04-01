class Solution:
    def compress(self, chars: List[str]) -> int:
        write = 0
        read = 0

        while read < len(chars):
            groupLength = read

            while groupLength < len(chars) and chars[groupLength] == chars[read]:
                groupLength += 1
            
            chars[write] = chars[read]
            write += 1

            length = groupLength - read

            if length > 1:
                for dig in str(length):
                    chars[write] = dig
                    write += 1
            
            read = groupLength
                        
        return write
        