import collections

class UnionFind:
    def __init__(self, num):
        self.par = [i for i in range(num)]
        self.rank = [1] * num
    
    def find(self, n):
        if n != self.par[n]:
            self.par[n] = self.find(self.par[n])
        return self.par[n]

    def union(self,n1,n2):
        p1, p2 = self.find(n1), self.find(n2)

        if p1 == p2:
            return False
        elif self.rank[p1] > self.rank[p2]:
            self.par[p2] = p1
            self.rank[p1] += self.rank[p2]
        else:
            self.par[p1] = p2
            self.rank[p2] += self.rank[p1]
        
        return True
        

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        n = len(accounts)
        uf = UnionFind(n)
        accountToIndex = {}
        #Same person if there is a common email to both accounts
        
        #Populate UF Data Structure
        for i, data in enumerate(accounts):
            for account in data[1:]:
                if account in accountToIndex:
                    originalAccount = accountToIndex[account]
                    uf.union(originalAccount, i)
                else:
                    accountToIndex[account] = i
        
        accountIndex= defaultdict(list)
        #Create a dictionary to store all the list of accounts
        for account, index in accountToIndex.items():
            rep = uf.find(index)
            accountIndex[rep].append(account)
        
        res = []
        for index, emails in accountIndex.items():
            meta = []
            name = accounts[index][0]

            meta.append(name)
            for email in sorted(emails):
                meta.append(email)
            
            res.append(meta)
        
        return res



        