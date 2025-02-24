class VacuumCleaner:
    def __init__(self):
        self.rooms = {'A': 'dirty', 'B': 'dirty'}  # Initial state
        self.position = 'A'
    
    def suck(self):
        print(f"Vacuum cleaner in Room {self.position}: Dirt detected! Sucking dirt...")
        self.rooms[self.position] = 'clean'
    
    def move(self):
        if self.position == 'A' and self.rooms['A'] == 'clean':
            self.position = 'B'
            print("Vacuum cleaner moving right to Room B")
        elif self.position == 'B' and self.rooms['B'] == 'clean':
            self.position = 'A'
            print("Vacuum cleaner moving left to Room A")
    
    def clean_rooms(self):
        while any(state == 'dirty' for state in self.rooms.values()):
            if self.rooms[self.position] == 'dirty':
                self.suck()
            self.move()
        print("All rooms are clean!")

# Create and run the vacuum cleaner
vacuum = VacuumCleaner()
vacuum.clean_rooms()
