
class QuickUnionUF:
    def __init__(self,size):
        self.id=[]
        self.sz=[]
        for i in range(size):
            self.id.append(i)
            self.sz.append(1)
    
    def root(self,i):
        while i!=self.id[i]:
            self.id[i]=self.id[self.id[i]]
            i=self.id[i]
        return i
    def connected(self,p,q):
        return self.root(p)==self.root(q)
    def union(self,p,q):
        p=self.root(p)
        q=self.root(q)
        if self.sz[p]<self.sz[q]:
            self.id[p]=q
            self.sz[q]+=self.sz[p]
        else:
            self.id[q]=p
            self.sz[p]+=self.sz[q]




