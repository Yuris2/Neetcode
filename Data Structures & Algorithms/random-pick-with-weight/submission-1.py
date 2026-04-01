class Solution:
    # [1,3,3,3]
    # [1,4]
    def __init__(self, w: List[int]):
        total = 0
        self.prefix = []

        for n in w:
            total += n
            self.prefix.append(total)
        
        self.total = total
        

    def pickIndex(self) -> int:
        choice = random.randint(1,self.total)
        l,r = 0, len(self.prefix) - 1

        while l < r:
            m = (l + r) // 2

            if self.prefix[m] < choice:
                l = m + 1
            else:
                r = m
        
        return r
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()