import collections
class UnionFind:
    def __init__(self,n):
        self.par = [i for i in range(n + 1)]
        self.rank = [0] * n
    
    def find(self, n):
        if n != self.par[n]:
            self.par[n] = self.find(self.par[n])
        return self.par[n]
    
    def union(self, n1, n2):
        p1, p2 = self.find(n1), self.find(n2)

        if p1 == p2:
            return False
        if self.rank[p1] > self.rank[p2]:
            self.par[p2] = self.par[p1]
            self.rank[p1] += self.rank[p2]
        else:
            self.par[p1] = self.par[p2]
            self.rank[p2] += self.rank[p1]
        
        return True

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        uf = UnionFind(len(accounts) + 1)
        accountIndex = {}
        #Name, rest of elements are emails representing emails 
        #We want to merge accounts (Union Find on the account idx)
        for i, data in enumerate(accounts):
            for a in data[1:]:
                if a in accountIndex:
                    uf.union(i, accountIndex[a])
                else:
                    accountIndex[a] = i
            #Some common email to both accounts
        
        accountsName = defaultdict(list)
        for email, index in accountIndex.items():
            parent = uf.find(index)
            accountsName[parent].append(email)
        
        res = []
        for index, emails in accountsName.items():
            data = [accounts[index][0]]

            for email in sorted(emails):
                data.append(email)

            res.append(data)
        
        return res


        
        #Return the accounts in the following format
            #First element of each account is the name
            #Rest of elements are in lexigraphical order
            #Return email in any order
        