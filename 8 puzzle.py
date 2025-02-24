from collections import deque
GOAL_STATE = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]

def array_to_matrix(arr):
    return [arr[i:i+3] for i in range(0, 9, 3)]
    
def find_zero(state):
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                return i, j

def get_neighbors(state):
    x, y = find_zero(state)
    moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # Up, Down, Left, Right
    neighbors = []
    
    for dx, dy in moves:
        nx, ny = x + dx, y + dy
        if 0 <= nx < 3 and 0 <= ny < 3:
            new_state = [row[:] for row in state]
            new_state[x][y], new_state[nx][ny] = new_state[nx][ny], new_state[x][y]
            neighbors.append(new_state)
    return neighbors

def bfs(initial):
    queue = deque([(initial, [])])  # (state, path)
    visited = set()
    while queue:
        state, path = queue.popleft()
        if state == GOAL_STATE:
            return path + [state]  # Return solution path
        visited.add(tuple(map(tuple, state)))
        for neighbor in get_neighbors(state):
            if tuple(map(tuple, neighbor)) not in visited:
                queue.append((neighbor, path + [state]))
    return None  
    
def solve_puzzle(arr):
    initial = array_to_matrix(arr)
    solution = bfs(initial)
    if solution:
        for step in solution:
            for row in step:
                print(row)
            print("↓")
    else:
        print("No solution found.")

initial_state = [1, 2, 3, 4, 0, 6, 7, 5, 8]  # Change this for different inputs
solve_puzzle(initial_state)