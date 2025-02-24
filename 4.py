class MonkeyBananaProblem:
    def __init__(self):
        self.monkey_position, self.box_position, self.banana_position = "entrance", "corner", "center"
        self.has_banana = False

    def move(self, position):
        print(f"Monkey moves from {self.monkey_position} to {position}.")
        self.monkey_position = position

    def push_box(self, position):
        if self.monkey_position == self.box_position:
            print(f"Monkey pushes the box from {self.box_position} to {position}.")
            self.box_position = position
            self.monkey_position = position
        else:
            print("Monkey must be at the box's position to push it.")

    def climb_and_grab(self):
        if self.monkey_position == self.box_position == self.banana_position:
            print("Monkey climbs the box and grabs the banana!")
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
        self.move(self.box_position)
        self.push_box(self.banana_position)
        self.climb_and_grab()
        self.return_to_entrance()

if __name__ == "__main__":
    problem = MonkeyBananaProblem()
    print("Starting the Monkey-Banana Problem...")
    problem.solve()
    print("Goal Achieved!" if problem.has_banana else "Failed to solve the problem.")
