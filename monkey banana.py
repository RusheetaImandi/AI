class MonkeyBananaProblem:
    def __init__(self):
        self.monkey_position = "entrance"
        self.box_position = "corner"  # The box starts at the corner of the room
        self.banana_position = "center"
        self.has_banana = False

    def move_monkey(self, position):
        print(f"Monkey moves from {self.monkey_position} to {position}.")
        self.monkey_position = position

    def push_box(self, position):
        if self.monkey_position == self.box_position:
            print(f"Monkey pushes the box from {self.box_position} to {position}.")
            self.box_position = position
            self.monkey_position = position
        else:
            print("Monkey must be at the box's position to push it.")

    def climb_box(self):
        if self.monkey_position == self.box_position == self.banana_position:
            print("Monkey climbs the box.")
            self.grab_banana()
        else:
            print("The box must be under the banana for the monkey to climb it.")

    def grab_banana(self):
        if self.monkey_position == self.box_position == self.banana_position:
            print("Monkey grabs the banana!")
            self.has_banana = True
        else:
            print("Monkey cannot grab the banana.")

    def return_to_entrance(self):
        if self.has_banana:
            print("Monkey returns to the entrance with the banana.")
            self.monkey_position = "entrance"
        else:
            print("Monkey cannot leave without the banana.")

    def solve(self):
        # Step 1: Move to the box
        self.move_monkey(self.box_position)

        # Step 2: Push the box under the banana
        self.push_box(self.banana_position)

        # Step 3: Climb the box
        self.climb_box()

        # Step 4: Return to the entrance with the banana
        self.return_to_entrance()


# Main execution
if __name__ == "__main__":
    problem = MonkeyBananaProblem()
    print("Starting the Monkey-Banana Problem...")
    problem.solve()
    if problem.has_banana:
        print("Goal Achieved: Monkey has the banana and is back at the entrance!")
    else:
        print("Failed to solve the problem.")