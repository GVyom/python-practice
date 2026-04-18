# Concepts Implemented in this Project:
# 1. print() function for displaying game story and outputs
# 2. input() function for taking user decisions
# 3. .lower() method for handling uppercase/lowercase inputs
# 4. Variables for storing user choices
# 5. if / elif / else conditional statements
# 6. Nested conditionals for multiple decision paths
# 7. Basic game logic and branching storyline
# 8. User interaction through terminal-based gameplay

print("Welcome to Treasure Island. Your mission is to find the treasure.")

# First decision point
direction = input("Which direction do you want to go? Left or Right: ").lower()

if direction == "left":

    # Second decision point
    action = input(
        "You have reached a lake. What would you like to do? "
        "(Wait for the boat / Swim over): "
    ).lower()

    if action == "wait":

        # Final decision point
        chest = input(
            "You came across three chests. One has treasure.\n"
            "Pick your poison - Red, Yellow, Blue: "
        ).lower()

        if chest == "yellow":
            print("Congratulations! You found the treasure.")

        elif chest == "red":
            print("You entered the realm of fire. Engulfed by lava. Game Over.")

        elif chest == "blue":
            print("You entered a vast wasteland. No treasure here. Game Over.")

        else:
            print("Invalid chest chosen. Game Over.")

    elif action == "swim over":
        print("You tried to swim across and became dinner for crocodiles. Game Over.")

    else:
        print("Invalid action chosen. Game Over.")

else:
    print("You made the wrong choice. Game Over.")