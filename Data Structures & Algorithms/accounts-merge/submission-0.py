import collections
class UnionFind:
    def __init__(self, numAccounts):
        self.par = [i for i in range(numAccounts)]
        self.rank = [1] * numAccounts
    
    def find(self, n):
        if n != self.par[n]:
            self.par[n] = self.find(self.par[n])
        return self.par[n]
    
    def union(self, n1, n2):
        p1, p2 = self.find(n1), self.find(n2)

        if p1 == p2:
            return False
        
        if self.rank[p1] > self.rank[p2]:
            self.par[p2] = p1
            self.rank[p1] += self.rank[p2]
        else:
            self.par[p1] = p2
            self.rank[p2] += self.rank[p1]
        
        return True

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        uf = UnionFind(len(accounts))
        
        emailToAccount = {}
        #Email to Account Index
        for i, e in enumerate(accounts):
            #Skip name
            for email in e[1:]:
                #Two accounts have same email
                if email in emailToAccount:
                    #Union two accounts that have same email
                    uf.union(i,emailToAccount[email])
                else:
                    emailToAccount[email] = i
        
        #Now we have our DSU set up, now we want to map
        #account index to list of emails
        emailGroups = defaultdict(list)


        for email, index in emailToAccount.items():
            leader = uf.find(index)
            emailGroups[leader].append(email)
        
        res = []
        for index, emails in emailGroups.items():
            data = []
            data.append(accounts[index][0])

            for e in sorted(emails):
                data.append(e)
            
            res.append(data)
        return res
        
            
        