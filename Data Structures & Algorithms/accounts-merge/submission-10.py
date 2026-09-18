import collections

class UnionFind:
    def __init__(self,n):
        self.rank = [1] * (n + 1)
        self.par = [i for i in range(n + 1)]
    
    def find(self,n):
        if n != self.par[n]:
            self.par[n] = self.find(self.par[n])
        return self.par[n]
    
    def union(self, n1, n2):
        p1,p2 = self.find(n1), self.find(n2)

        if p1 == p2:
            return False
        elif self.rank[p1] > self.rank[p2]:
            self.par[p2] = self.par[p1]
            self.rank[p1] += self.rank[p2]
        else:
            self.par[p1] = self.par[p2]
            self.rank[p2] += self.rank[p1]
        
        return True
    
class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        accountIndex = {}
        uf = UnionFind(len(accounts))

        for i, account in enumerate(accounts):
            for email in account[1:]:
                if email in accountIndex:
                    idx = accountIndex[email]
                    uf.union(i,idx)
                else:
                    accountIndex[email] = i
        
        indexAccount = defaultdict(list)

        for email, i in accountIndex.items():
            rep = uf.find(i)
            indexAccount[rep].append(email)
        
        res = []

        for i,meta in indexAccount.items():
            data = [accounts[i][0]]

            for email in sorted(meta):
                data.append(email)
            
            res.append(data)
        
        return res

        