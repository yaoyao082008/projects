from IndexBinaryHeap_shortestpath import BinaryMinHeap


def shortestPath(source,graph,target,stops):

    if target not in graph :
        raise Exception("target value is not in the graph")
    elif source not in graph:
        raise Exception("starting node not in graph")

    stops+=1
    shortest_dis=BinaryMinHeap()
    previous={}


    for node in graph:
        shortest_dis.insert([node,float('inf')])
        previous[node]=[0,0]

    shortest_dis.update(source,0)


    while len(shortest_dis.storage)>1 and shortest_dis.peek()[0]!=target:
        parent,shortest_parent=shortest_dis.poll()

        for node in graph[parent]:
            child,dis=node
            if child in shortest_dis.map:
                shortest_child=shortest_dis.get_value(child)
                if shortest_child>shortest_parent+dis:
                    shortest_dis.update(child,dis+shortest_parent)
                    previous[child]=[parent,previous[parent][1]+1]

                


    distance=shortest_dis.peek()[1]

    
    return distance

        



