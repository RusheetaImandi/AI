from collections import deque

# BFS function
def bfs(graph, start):
    visited, queue, result = set(), deque([start]), []
    while queue:
        node = queue.popleft()
        if node not in visited:
            visited.add(node)
            result.append(node)
            queue.extend(graph.get(node, []))
    return result

# DFS function
def dfs(graph, start):
    visited, stack, result = set(), [start], []
    while stack:
        node = stack.pop()
        if node not in visited:
            visited.add(node)
            result.append(node)
            stack.extend(reversed(graph.get(node, [])))  # Reverse for correct order
    return result

# Tree structure builder
def build_tree_structure(graph, traversal_order):
    return {node: graph.get(node, []) for node in traversal_order}

# Graph as per the image
graph = {1: [2, 3], 2: [4, 5], 3: [6], 4: [], 5: [], 6: []}

# BFS and DFS Traversals and Tree Structures
bfs_result, dfs_result = bfs(graph, 1), dfs(graph, 1)
bfs_tree, dfs_tree = build_tree_structure(graph, bfs_result), build_tree_structure(graph, dfs_result)

# Output Results
print("BFS Traversal:", bfs_result)
print("BFS Tree Structure:", *[f"{node} -> {children}" for node, children in bfs_tree.items()], sep="\n")
print("\nDFS Traversal:", dfs_result)
print("DFS Tree Structure:", *[f"{node} -> {children}" for node, children in dfs_tree.items()], sep="\n")
