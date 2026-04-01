import collections
class UnionFind:
    def __init__(self, n):
        self.par = [i for i in range(n)]
        self.rank = [1] * n
    
    def find(self, n):
        if n != self.par[n]:
            self.par[n] = self.find(self.par[n])
        return self.par[n]
    
    def union(self, n1, n2):
        p1,p2 = self.find(n1), self.find(n2)

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
        emailToIndex = {}

        #Create our union find data structure
        for i, account in enumerate(accounts):
            for email in account[1:]:
                if email in emailToIndex:
                    idx = emailToIndex[email]
                    uf.union(i, idx)
                else:
                    emailToIndex[email] = i
        
        accountToEmail = defaultdict(list)

        for email, index in emailToIndex.items():
            head = uf.find(index)
            accountToEmail[head].append(email)
        
        res = []
        for idx, emails in accountToEmail.items():
            data = []
            data.append(accounts[idx][0])

            for email in sorted(emails):
                data.append(email)
        
            res.append(data)
        return res
 