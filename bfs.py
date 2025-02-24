from collections import deque

def bfs(graph, start):
    visited = set()
    queue = deque([start])
    result = []

    while queue:
        node = queue.popleft()
        if node not in visited:
            visited.add(node)
            result.append(node)
            queue.extend(graph.get(node, []))
    return result

def dfs(graph, start):
    visited = set()
    stack = [start]
    result = []

    while stack:
        node = stack.pop()
        if node not in visited:
            visited.add(node)
            result.append(node)
            stack.extend(reversed(graph.get(node, [])))  # Reverse to maintain order
    return result

# Combined function to choose BFS or DFS
def traverse(graph, start, method="bfs"):
    if method == "bfs":
        return bfs(graph, start)
    elif method == "dfs":
        return dfs(graph, start)
    else:
        raise ValueError("Invalid method! Choose 'bfs' or 'dfs'.")

# Example usage
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F', 'G'],
    'D': [],
    'E': [],
    'F': [],
    'G': []
}

print("BFS:", traverse(graph, 'A', method="bfs"))  # Output: ['A', 'B', 'C', 'D', 'E', 'F', 'G']
print("DFS:", traverse(graph, 'A', method="dfs"))  # Output: ['A', 'B', 'D', 'E', 'C', 'F', 'G']