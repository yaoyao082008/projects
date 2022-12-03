from IndexBinaryHeap_shortestpath import BinaryMinHeap
import time
start=time.time()

def shortestPath(source,graph,target,stops):
    shortest_dis=BinaryMinHeap()
    previous={}
    for node in graph:
        if source==node:
            shortest_dis.insert([node,0])
        else:
            shortest_dis.insert([node,float('inf')])

        previous[node]=[0,0]


    while len(shortest_dis.storage)>1 and shortest_dis.peek()[0]!=target:
        shortest_parent=shortest_dis.peek()[1]
        parent=shortest_dis.poll()[0]

        for node in graph[parent]:
            child,dis=node
            if child in shortest_dis.map:
                shortest_child=shortest_dis.get_value(child)
                if shortest_child>shortest_parent+dis:
                    shortest_dis.update(child,dis+shortest_parent)
                    previous[child]=[parent,previous[parent][1]+1]



    destinaton=shortest_dis.peek()

    # while new_stops>stops:
    #     prevprev=previous[previous[destinaton[0]][0]][0]

    #     for n in graph[node]:
    #         if n[0]==prevprev:
    #             pass
    return destinaton,previous

        



graph={
    'a':[['b',2],['d',8]],
    'b':[['a',2],['d',5],['e',6]],
    'c':[['e',9],['f',3]],
    'd':[['a',8],['b',5],['e',3],['f',2]],
    'e':[['b',6],['d',3],['f',1],['c',9]],
    'f':[['d',2],['e',1],['c',3]],
    #'g':[['b',2],['f',5]]

}

shortest,prev=shortestPath('a',graph,'c',2)

end=time.time()


print(shortest)
print(prev)
print(end-start)