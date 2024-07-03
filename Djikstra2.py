def dijkstra(graph, start):
    # Dictionary to keep track of the shortest distance from the start node to each node
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    print(distances)
    
    # Set to keep track of visited nodes
    visited = set()
    
    while len(visited) < len(graph):
        # Find the node with the shortest tentative distance that hasn't been visited
        min_distance = float('inf')
        min_node = None
        for node in graph:
            if node not in visited and distances[node] < min_distance:
                min_distance = distances[node]
                min_node = node
        
        # Mark the chosen node as visited
        visited.add(min_node)
        
        # Update distances to neighbors of the chosen node
        for neighbor, weight in graph[min_node].items():
            distance = distances[min_node] + weight
            # If the new path to the neighbor is shorter, update the distance
            if distance < distances[neighbor]:
                distances[neighbor] = distance
    
    return distances

# Example graph represented as an adjacency list
graph = {
    'A': {'B': 5, 'C': 3},
    'B': {'A': 5, 'C': 2, 'D': 1},
    'C': {'A': 3, 'B': 2, 'D': 4, 'E': 2},
    'D': {'B': 1, 'C': 4, 'E': 3, 'F': 6},
    'E': {'C': 2, 'D': 3, 'F': 7},
    'F': {'D': 6, 'E': 7}
}

start_node = 'A'
shortest_distances = dijkstra(graph, start_node)
print("Shortest distances from node", start_node + ":")
for node, distance in shortest_distances.items():
    print(node + ":", distance)
