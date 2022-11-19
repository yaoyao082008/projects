

import queue


def go_through_cycle(graph,root):
    stack=[root]
    while stack:
        parent=stack.pop()
        for child in graph[parent]:
            stack.append(child)
            if child==root:
                return True

def depthFirstSearch(graph,root):
    visited=[root]
    stack=[root]
    while stack:
        parent=stack.pop()

        for child in graph[parent]:
            if child not in visited:
                stack.append(child)
                visited.append(child)

    return visited , root

def depthFirstSearchRoot(graph,root,visited):
    stack=[root]
    visited.add(root)
    added=[root]
    while stack:
        parent=stack.pop()

        for child in graph[parent]:
            if child not in visited:
                stack.append(child)
                visited.add(child)
                added.append(child)
            elif go_through_cycle(graph,child):
                return True
                

    return added




def find_root(graph,node):
    visited={''}
    output=[]
    for node in graph:
        if node not in visited:
            added=depthFirstSearchRoot(graph,node,visited)
            if added==True:
                return
            output.append(added)

    return output




def breadthFirstSearch(graph,root):
    visited=[]
    nodes=queue.Queue()
    nodes.put(root)
    visited.append(root)
    output=[]


    while not nodes.empty():
        parent=nodes.get()
        output.append(parent)
        for child in graph[parent]:
            if child not in visited:
                nodes.put(child)
                visited.append(child)
    return output





graph={
    'i':[],
    'j':[],
    #graph1
    'b':['d','e'],
    'c':['d','b'],
    'd':[],
    'e':[],
    'a':['b','c'],
    #graph2
    'f':['g','h'],
    'h':['g'],
    'g':['i','j']
    

    }


output=find_root(graph,'e')
#output.reverse()
for i in range(1,len(output)+1):
    print(output[-i],end='')