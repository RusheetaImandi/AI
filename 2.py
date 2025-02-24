from collections import deque

class WaterJug:
    def __init__(self, jug1_capacity, jug2_capacity, goal):
        self.jug1_capacity, self.jug2_capacity, self.goal = jug1_capacity, jug2_capacity, goal

    def get_next_states(self, state):
        jug1, jug2 = state
        return [
            (self.jug1_capacity, jug2) if jug1 < self.jug1_capacity else None,
            (jug1, self.jug2_capacity) if jug2 < self.jug2_capacity else None,
            (0, jug2) if jug1 > 0 else None,
            (jug1, 0) if jug2 > 0 else None,
            (jug1 - min(jug1, self.jug2_capacity - jug2), jug2 + min(jug1, self.jug2_capacity - jug2)) if jug1 > 0 and jug2 < self.jug2_capacity else None,
            (jug1 + min(jug2, self.jug1_capacity - jug1), jug2 - min(jug2, self.jug1_capacity - jug1)) if jug2 > 0 and jug1 < self.jug1_capacity else None
        ]
    
    def bfs(self):
        queue, visited, path = deque([(0, 0)]), {(0, 0)}, {(0, 0): None}
        while queue:
            current = queue.popleft()
            if current[0] == self.goal or current[1] == self.goal:
                return self.construct_path(path, current)
            for next_state in self.get_next_states(current):
                if next_state and next_state not in visited:
                    visited.add(next_state)
                    path[next_state] = current
                    queue.append(next_state)
        return None

    def construct_path(self, path, goal_state):
        result, current = [], goal_state
        while current: result.append(current); current = path[current]
        return result[::-1]

if __name__ == "__main__":
    solution = WaterJug(3, 5, 4).bfs()
    if solution:
        print("Solution found:")
        for state in solution:
            print("Jug 1: {} liters, Jug 2: {} liters".format(state[0], state[1]))
    else:
        print("No solution found.")
