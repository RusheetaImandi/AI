from collections import deque

class WaterJug:
    def __init__(self, jug1_capacity, jug2_capacity, goal):
        self.jug1_capacity = jug1_capacity
        self.jug2_capacity = jug2_capacity
        self.goal = goal

    def is_goal_state(self, state):
        return state[0] == self.goal or state[1] == self.goal

    def get_next_states(self, state):
        jug1, jug2 = state
        next_states = []

        # Fill jug 1
        if jug1 < self.jug1_capacity:
            next_states.append((self.jug1_capacity, jug2))

        # Fill jug 2
        if jug2 < self.jug2_capacity:
            next_states.append((jug1, self.jug2_capacity))

        # Empty jug 1
        if jug1 > 0:
            next_states.append((0, jug2))

        # Empty jug 2
        if jug2 > 0:
            next_states.append((jug1, 0))

        # Pour water from jug 1 to jug 2
        if jug1 > 0 and jug2 < self.jug2_capacity:
            transfer_amount = min(jug1, self.jug2_capacity - jug2)
            next_states.append((jug1 - transfer_amount, jug2 + transfer_amount))

        # Pour water from jug 2 to jug 1
        if jug2 > 0 and jug1 < self.jug1_capacity:
            transfer_amount = min(jug2, self.jug1_capacity - jug1)
            next_states.append((jug1 + transfer_amount, jug2 - transfer_amount))

        return next_states

    def bfs(self):
        initial_state = (0, 0)
        queue = deque([initial_state])
        visited = set()
        visited.add(initial_state)
        path = {initial_state: None}

        while queue:
            current_state = queue.popleft()

            if self.is_goal_state(current_state):
                return self.construct_path(path, current_state)

            for next_state in self.get_next_states(current_state):
                if next_state not in visited:
                    visited.add(next_state)
                    path[next_state] = current_state
                    queue.append(next_state)

        return None

    def construct_path(self, path, goal_state):
        current = goal_state
        result = []
        while current is not None:
            result.append(current)
            current = path[current]
        result.reverse()
        return result

if __name__ == "__main__":
    jug1_capacity = 3
    jug2_capacity = 5
    goal = 4

    water_jug_solver = WaterJug(jug1_capacity, jug2_capacity, goal)
    solution = water_jug_solver.bfs()

    if solution:
        print("Solution found:")
        for state in solution:
            print(f"Jug 1: {state[0]} liters, Jug 2: {state[1]} liters")
    else:
        print("No solution found.")
