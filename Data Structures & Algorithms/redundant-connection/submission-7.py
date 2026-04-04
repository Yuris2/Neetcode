class UnionFind:
    def __init__(self, num):
        self.par = [i for i in range(num + 1)]
        self.rank = [1] * (num + 1)
    
    def find(self, n):
        if n != self.par[n]:
            self.par[n] = self.find(self.par[n])
        return self.par[n]
    
    def union(self, n1, n2):
        p1, p2 = self.find(n1), self.find(n2)

        if p1 == p2:
            return False
        
        #Union By Rank
        if self.rank[p1] > self.rank[p2]:
            self.par[p2] = self.par[p1]
            self.rank[p1] += self.rank[p2]
        else:
            self.par[p1] = self.par[p2]
            self.rank[p2] += self.rank[p1]
        
        return True

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        #Given a graph that contains no cycles consisting of n - 1 edges
        #Add an additional edges and now a cycle exists
        #Return the edget that can be removed to remove cycle
        uf = UnionFind(len(edges))

        for n1, n2 in edges:
            if not uf.union(n1, n2):
                return [n1,n2]

        #Solution Intuition
            #Use a Data Structure (Union Find) that allows us to track edges
            #We can union edges together to create a disjoint set
            #If the element already belongs to the same set, that edge introduced a cycle
        