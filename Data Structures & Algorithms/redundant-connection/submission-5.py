class UnionFind:
    def __init__(self, n):
        self.par = [i for i in range(n + 1)]
        self.rank = [1] * (n + 1)
    
    def find(self, n):
        if n != self.par[n]:
            self.par[n] = self.find(self.par[n])
        return self.par[n]

    
    def union(self, n1, n2):
        p1,p2 = self.find(n1), self.find(n2)

        if p1 == p2:
            return False
        
        if self.rank[p1] > self.rank[p2]:
            self.rank[p1] += self.rank[p2]
            self.par[p2] = self.par[p1]
        else:
            self.rank[p2] += self.rank[p1]
            self.par[p1] = self.par[p2]
        
        return True


class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        uf = UnionFind(len(edges))

        for n1, n2 in edges:
            if not uf.union(n1,n2):
                return [n1,n2]
        
        