from random import randint
from UnionFind import QuickUnionUF
from statistics import mean
size=1000
site= QuickUnionUF(size*size+2)
test=[]
av=0
def percolate(site):
    count=0
    vsite=len(site.id)-1
    vsite1=len(site.id)-2

    while not site.connected(vsite,vsite1):
        open=randint(0,len(site.id)-3)
        while site.sz[open]>1:
            open=randint(0,len(site.id)-3)
        site.union(open,open)
        count+=1
        if (open+1)%size!=0 and site.sz[open+1]>1 and not site.connected(open,open+1):
            site.union(open,open+1)
        if (open)%size!=0 and site.sz[open-1]>1 and not site.connected(open,open-1):
            site.union(open,open-1)
        if (open+size)<len(site.id)-2 and site.sz[open+size]>1 and not site.connected(open,open+size):
            site.union(open,open+size)
        elif open+size>=len(site.id)-2 and not site.connected(open,vsite):
            site.union(open,vsite)
        if open-size>=0 and site.sz[open-size]>1 and not site.connected(open,open-size):
            site.union(open,open-size)
        elif open-size<0 and not site.connected(open,vsite1):
            site.union(open,vsite1)
    return count/(len(site.id)-2)


print(percolate(site))
            



