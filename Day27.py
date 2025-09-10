from collections import deque, defaultdict

def shortest_path(V, edges, start, end):

    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)  
    
    
    visited = set()
    queue = deque([(start, 0)])  
    
    
    while queue:
        node, dist = queue.popleft()
        
        if node == end:
            return dist
        
        if node in visited:
            continue
        visited.add(node)
        
        for neighbor in graph[node]:
            if neighbor not in visited:
                queue.append((neighbor, dist + 1))
    
 
    return -1

print(shortest_path(5, [[0,1],[0,2],[1,3],[2,3],[3,4]], 0, 4))  
print(shortest_path(3, [[0,1],[1,2]], 0, 2))                    
print(shortest_path(4, [[0,1],[1,2]], 2, 3))                    
  
