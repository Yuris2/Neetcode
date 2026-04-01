class UnionFind:
    def __init__(self, accounts):
        self.rank = [1] * (accounts)
        self.par = [n for n in range(accounts)]
    
    def find(self, n):
        if n != self.par[n]:
            self.par[n] = self.find(self.par[n])
        return self.par[n]
    
    def union(self, n1, n2):
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
        #If we have seen an email
        res = []
        emailToIndex = {}

        for i, emails in enumerate(accounts):
            #Go through the emails
            for email in emails[1:]:
                #We have found a merged email
                if email in emailToIndex:
                    idx = emailToIndex[email]
                    uf.union(i, idx)
                else:
                    emailToIndex[email] = i
        
        accountList = defaultdict(list)

        for email, index in emailToIndex.items():
            head = uf.find(index)
            accountList[head].append(email)
        
        for head, emails in accountList.items():
            data = [accounts[head][0]]
            for email in sorted(emails):
                data.append(email)
            res.append(data)
        return res
        #Name: email1, email2, email3
        #Common Email = Same Person
        #Name Not Necessarily Same Person

        #After Merging
        #[Name, Emails in Sorted Order]


        