class UnionFind:
    def __init__(self, n):
        self.rank = [1] * n
        self.par = [i for i in range(n)]
    
    def find(self, n):
        if self.par[n] != n:
            self.par[n] = self.find(self.par[n])
        return self.par[n]
    
    def union(self,n1,n2):
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
        n = len(accounts)
        uf = UnionFind(n)
        emailToIndex = {}

        for i, account in enumerate(accounts):
            for email in account[1:]:
                if email in emailToIndex:
                    idx = emailToIndex[email]
                    uf.union(i,idx)
                else:
                    emailToIndex[email] = i
        
        indexToEmails = defaultdict(list)
        for email, i in emailToIndex.items():
            idx = uf.find(i)
            indexToEmails[idx].append(email)
        
        res = []
        for index, emails in indexToEmails.items():
            data = [accounts[index][0]]

            for email in sorted(emails):
                data.append(email)
            
            res.append(data)
        
        return res





        