class UnionFind:
    def __init__(self, n):
        self.par = [i for i in range(n)]
        self.rank = [1] * n
    
    def find(self, n):
        if n != self.par[n]:
            self.par[n] = self.find(self.par[n])
        return self.par[n]
    
    def union(self, n1,n2):
        p1,p2 = self.find(n1), self.find(n2)

        if p1 == p2:
            return False
        
        if self.rank[p1] > self.rank[p2]:
            self.par[p2] = self.par[p1]
            self.rank[p1] += self.rank[p2]
        else:
            self.par[p1] = self.par[p2]
            self.rank[p2] += self.rank[p1]
        
        return True
        
import collections
class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        uf = UnionFind(len(accounts))
        #Two accounts = Same Person if they share an email (Merge), but same name could be different people
        #Email=Index
        emailToIndex = {}
        #Go through the accounts and the emails associated with that account
        for i, emails in enumerate(accounts):
            for email in emails[1:]:
            #If we have already seen that email, we merge to the account with that email
                if email in emailToIndex:
                    idx = emailToIndex[email]
                    uf.union(i, idx)    
            #If we have not, store the index of that email
                else:
                    emailToIndex[email] = i

        accountToEmail = defaultdict(list)
        #Go through each email and index:
        for email, index in emailToIndex.items():
            #Given an index: find the representative index/group leader
            leader = uf.find(index)
            #Add email to group leader list
            accountToEmail[leader].append(email)
        
        res = []

        for account, emails in accountToEmail.items():
            data = []
            data.append(accounts[account][0])

            for email in sorted(emails):
                data.append(email)
            res.append(data)
        
        return res




'''
Neet@gmail = 0              0 <- 2          1           3
Alice@gmail = 1             
bob@gmail.com = 2             
neetcode@gmail.com = 3

Get account at index
[["neet", "bob@gmail.com","neet@gmail.com"], ["alice", "alice@gmail.com"]]

'''
        