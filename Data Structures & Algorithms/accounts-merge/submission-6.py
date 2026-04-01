class UnionFind:
    def __init__(self, numAccounts):
        self.par = [i for i in range(numAccounts)]
        self.rank = [1] * numAccounts
    
    def find(self, x):
        if x != self.par[x]:
            self.par[x] = self.find(self.par[x])
        return self.par[x]
    
    def union(self, n1, n2):
        p1, p2 = self.find(n1), self.find(n2)

        if p1 == p2:
            return False
        elif self.rank[p1] > self.rank[p2]:
            self.rank[p1] += self.rank[p2]
            self.par[p2] = p1
        else:
            self.rank[p2] += self.rank[p1]
            self.par[p1] = p2
        
        return True

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        uf = UnionFind(len(accounts))
        emailIndex = {}
        #Two accounts belong to the same person if there is a common email between both accounts
        for i, account in enumerate(accounts):
            for email in account[1:]:
                if email in emailIndex:
                    prevIndex = emailIndex[email]
                    uf.union(prevIndex, i)
                else:
                    emailIndex[email] = i
        
        accountIndex = defaultdict(list)

        for email, index in emailIndex.items():
            repIndex = uf.find(index)
            accountIndex[repIndex].append(email)
        
        res = []

        for account, emails in accountIndex.items():
            name = accounts[account][0]
            data = [name]

            for email in sorted(emails):
                data.append(email)
            
            res.append(data)
        
        return res



        #Merge Accounts

        #Name, Emails in sorted Order
        