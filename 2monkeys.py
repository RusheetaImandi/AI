import random

class MonkeyBananaProblem:
    def __init__(self):
        self.monkey1_position = "entrance"
        self.monkey2_position = "entrance"
        self.box_position = "corner"
        self.banana_position = "center"
        self.has_banana = False
        self.box_pusher = None

    def move_monkey(self, monkey, position):
        if monkey == 1:
            print(f"Monkey 1 moves from {self.monkey1_position} to {position}.")
            self.monkey1_position = position
        elif monkey == 2:
            print(f"Monkey 2 moves from {self.monkey2_position} to {position}.")
            self.monkey2_position = position

    def push_box(self, monkey, position):
        if (monkey == 1 and self.monkey1_position == self.box_position) or (
            monkey == 2 and self.monkey2_position == self.box_position
        ):
            print(f"Monkey {monkey} pushes the box from {self.box_position} to {position}.")
            self.box_position = position
            if monkey == 1:
                self.monkey1_position = position
            else:
                self.monkey2_position = position

            # Record the first monkey to push the box
            if self.box_pusher is None:
                self.box_pusher = monkey
        else:
            print(f"Monkey {monkey} must be at the box's position to push it.")

    def climb_box_and_grab_banana(self):
        if (
            (self.box_pusher == 1 and self.monkey1_position == self.box_position)
            or (self.box_pusher == 2 and self.monkey2_position == self.box_position)
        ) and self.box_position == self.banana_position:
            print(f"Monkey {self.box_pusher} climbs the box and grabs the banana!")
            self.has_banana = True
        else:
            print("The box must be under the banana, and only the box pusher can grab the banana.")

    def return_to_entrance(self):
        if self.box_pusher == 1:
            print("Monkey 1 returns to the entrance with the banana.")
            self.monkey1_position = "entrance"
        elif self.box_pusher == 2:
            print("Monkey 2 returns to the entrance with the banana.")
            self.monkey2_position = "entrance"

    def solve(self):
        # Step 1: Both monkeys move to random positions to find the box
        positions = ["corner", "banana", "center"]
        random.shuffle(positions)

        self.move_monkey(1, positions[0])
        self.move_monkey(2, positions[1])

        # Step 2: Check which monkey reaches the box first
        if self.monkey1_position == self.box_position:
            self.push_box(1, self.banana_position)
        elif self.monkey2_position == self.box_position:
            self.push_box(2, self.banana_position)

        # Step 3: The box pusher climbs the box to grab the banana
        self.climb_box_and_grab_banana()

        # Step 4: The box pusher returns to the entrance with the banana
        self.return_to_entrance()


# Main execution
if __name__ == "__main__":
    problem = MonkeyBananaProblem()
    print("Starting the Monkey-Banana Problem with Two Monkeys...\n")
    problem.solve()
    print("\nResult:")
    if problem.has_banana:
        print(f"Monkey {problem.box_pusher} grabbed the banana and returned to the entrance first.")
    else:
        print("Failed to solve the problem: No monkey grabbed the banana.")