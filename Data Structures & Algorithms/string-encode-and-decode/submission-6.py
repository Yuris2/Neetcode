class Solution:
    def encode(self, strs: List[str]) -> str:
        delim = '#'
        res = []

        for s in strs:
            string = str(len(s)) + "#" + s
            res.append(string)

        return "".join(res) 

    def decode(self, s: str) -> List[str]:
        res = []
        ptr = 0

        while ptr < len(s):
            ptr2 = ptr
            while s[ptr2] != '#':
                ptr2 += 1
            length = int(s[ptr:ptr2])
            string = s[ptr2 + 1:ptr2 + length + 1]
            res.append(string)
            ptr = ptr2 + length + 1
        
        return res
