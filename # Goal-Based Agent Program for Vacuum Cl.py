# Goal-Based Agent Program for Vacuum Cleaner

# Define the states for each room
room_states = {
    "A": False,  # False means not cleaned, True means cleaned
    "B": False,
    "C": False,
    "D": False
}

# Define the transition table
transition_table = {
    "A": "B",
    "B": "C",
    "C": "D",
    "D": None  # No next room after D
}

def display_room_states():
    """Display the cleaning status of all rooms."""
    print("Current Room States:")
    for room, state in room_states.items():
        status = "cleaned" if state else "dirty"
        print(f"Room {room} is {status}.")
    print()

def clean_room(room):
    """Clean the room and return the updated state."""
    print(f"Cleaning Room {room}...")
    room_states[room] = True
    print(f"Room {room} is cleaned.")

def vacuum_cleaner():
    """Simulate the vacuum cleaner's operation."""
    current_room = "A"  # Default start room

    while current_room is not None:
        # Display the current state of all rooms
        display_room_states()

        # Clean the current room
        clean_room(current_room)

        # Move to the next room based on the transition table
        current_room = transition_table[current_room]

    # Final display after all rooms are cleaned
    display_room_states()
    if all(room_states.values()):
        print("All rooms are cleaned!")

# Run the vacuum cleaner program
vacuum_cleaner()
