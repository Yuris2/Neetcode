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
        p1, p2 = self.find(n1), self.find(n2)

        if p1 == p2:
            return False
        if self.rank[p1] > self.rank[p2]:
            self.rank[p2] += self.rank[p1]
            self.par[p2] = p1
        else:
            self.rank[p1] += self.rank[p2]
            self.par[p1] = p2
        
        return True

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        #Two accounts belong to the same person if they share an email
        n = len(accounts)
        #Union Find (accounts)
        uf = UnionFind(n)
        emailIndex = {}
        #UF, email:index

        #Iterate thorugh each email, index
        for i, account in enumerate(accounts):
            for email in account[1:]:
                #If we have seen this email before
                if email in emailIndex:
                    #Union with index of previously seen email
                    i2 = emailIndex[email]
                    uf.union(i,i2)
                else:
                     #Add to emailToIndex
                    emailIndex[email] = i
        accountIndex = defaultdict(list)
        #Iterate through each email, index and find the representative account
        for email, index in emailIndex.items():
            #map accountIndex:[email]
            rep = uf.find(index)
            accountIndex[rep].append(email)
        
        res = []
        #Iterate through accountIndex
        for accountNumber, emails in accountIndex.items():
            data = [accounts[accountNumber][0]]
            #Format res
            for email in sorted(emails):
                data.append(email)
            res.append(data)
        
        return res
        
        #Return the accounts s.t
            #[name, email1, email2, ...] s.t emails are sorted
        