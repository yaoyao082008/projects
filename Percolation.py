from UnionFind import QuickUnionUF
from random import randint
size=10
site=QuickUnionUF(size**2)


def virtual_site(size,site):
    first=0
    last=len(site.id)-1
    itr=last-1
    for i in range(1,size):
        site.union(first,i)
        site.sz[i]=size
        site.union(last,itr)
        site.sz[itr]=size
        itr-=1
    return site

site=virtual_site(size,site)


print()

def percolate(site):
    first=0
    last=len(site.id)-1
    count=0
    while not site.connected(first,last):
        open=randint(first+size,last-size+1)
        while site.sz[open]>1:
            open=randint(first+size,last-size+1)
        site.union(open,open)
        count+=1
        if (open+1)%size!=0 and site.sz[open+1]>1:
            if not site.connected(open,open+1):
                site.union(open,open+1)
        if open%size!=0 and site.sz[open-1]>1:
            if not site.connected(open,open-1):
                site.union(open,open-1)
        if open + size <size**2 and site.sz[open+size]>1:
            if not site.connected(open,open+size):
                site.union(open,open+size)
        if open-size>=0 and site.sz[open-size]>1:
            if not site.connected(open,open-size):
                site.union(open,open-size)
    return count/(size*size-size*2)

#for i in range(10000):
print(percolate(site))

            



