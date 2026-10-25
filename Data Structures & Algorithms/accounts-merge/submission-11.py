class UnionFind:
    def __init__(self, n):
        self.par = [i for i in range(n + 1)]
        self.rank = [1] * (n + 1)
    
    def find(self, n):
        if n != self.par[n]:
            self.par[n] = self.find(self.par[n])
        return self.par[n]
    
    def union(self, n1, n2):
        p1, p2 = self.find(n1), self.find(n2)

        if p1 == p2:
            return False
        elif self.rank[p1] > self.rank[p2]:
            self.par[p2] = self.par[p1]
            self.rank[p1] += self.rank[p2]
        else :
            self.par[p1] = self.par[p2]
            self.rank[p2] += self.rank[p1]
        
        return True

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        uf = UnionFind(len(accounts))
        emailIndex = {}
        #Accounts[i] = [name, emails]
        for i,account in enumerate(accounts):
            for email in account[1:]:
                #Map Email to the i
                if email in emailIndex:
                    #Link the indices together
                    uf.union(i, emailIndex[email])
                else:
                    emailIndex[email] = i

        #With this mapping [email:index]
        accountIndex = defaultdict(list)
        #Create maping of index: list of emails
        for email, idx in emailIndex.items():
            index = uf.find(idx)
            accountIndex[index].append(email)
        
        res = []

        for index, meta in accountIndex.items():
            data = [accounts[index][0]]

            for email in sorted(meta):
                data.append(email)
            
            res.append(data)
        
        return res
        #Merge, name and emails in sorted order
        #With this mapping, create the output
        