class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        leftIndex = []
        remove = set()

        for i,c in enumerate(s):
            if c == ')':
                if leftIndex and leftIndex[-1] < i:
                    leftIndex.pop()
                else:
                    remove.add(i)
            elif c == '(':
                leftIndex.append(i)
        
        for i in leftIndex:
            remove.add(i)
        
        res = []

        for i,c in enumerate(s):
            if i in remove:
                continue
            res.append(c)
        
        return "".join(res)            



        

        