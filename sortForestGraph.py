



def go_through_cycle(graph,root):
    stack=[root]
    while stack:
        parent=stack.pop()
        for child in graph[parent]:
            stack.append(child)
            if child==root:
                return True

def DFS(graph,root,visited):
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
                return added,True

    return added,False

def DFS_rec(graph,parent,visited,result):
    
    for child in graph[parent]:
        if child not in visited:
            visited.add(child)
            result.append(child)
            return DFS_rec(graph,child,visited,result)
        elif go_through_cycle(graph,child):
            return result,True
    return result,False




def sort(graph):
    visited={''}
    output=[]
    for node in graph:
        if node not in visited:
            visited.add(node)
            result,cycle=DFS_rec(graph,node,visited,[node])
            if cycle==True:
                print('cycle detected!')
                return True
            output.append(result)

    return output






# graph={
#     'i':[],
#     'j':[],
#     #graph1
#     'b':['d','e'],
#     'c':['d','b'],
#     'd':['f'],
#     'e':[],
#     'a':['b','c'],
#     #graph2
#     'f':['b','h'],
#     'h':['g'],
#     'g':['i','j']
#     }
gcycle={
    'a' : ['b', 'c'],
    'f': [],
    'e': ['a', 'f'],
    'b': [],
    'c': ['e']
    }


output=sort(gcycle)

if output != True:
    output.reverse()
    print(output)