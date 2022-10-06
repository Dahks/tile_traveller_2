import random

# Constants
NORTH = "n"
EAST = "e"
SOUTH = "s"
WEST = "w"

YES = "y"
NO = "n"


def has_won(col, row):
    """Return true if player is in the victory cell."""

    return col == 3 and row == 1  # (3,1)


def find_directions(col, row):
    """Returns valid directions as a string given the supplied location."""

    if col == 1 and row == 1:  # (1,1)
        valid_directions = NORTH
    elif col == 1 and row == 2:  # (1,2) --> pull lever?
        valid_directions = NORTH + EAST + SOUTH
    elif col == 1 and row == 3:  # (1,3)
        valid_directions = EAST + SOUTH
    elif col == 2 and row == 1:  # (2,1)
        valid_directions = NORTH
    elif col == 2 and row == 2:  # (2,2) --> pull lever?
        valid_directions = SOUTH + WEST
    elif col == 2 and row == 3:  # (2,3) --> pull lever?
        valid_directions = EAST + WEST
    elif col == 3 and row == 2:  # (3,2) --> pull lever?
        valid_directions = NORTH + SOUTH
    elif col == 3 and row == 3:  # (3,3)
        valid_directions = SOUTH + WEST

    return valid_directions

def pull_lever_for_coin():
    # Ask if player want to pull lever
    PROMPT = "Pull a lever (y/n): "
    print(PROMPT, end="")
    answer = random.choice([YES, NO])
    print(answer)
    if answer.lower() == "y":
        return 1
    return 0

def is_on_lever_tile(col, row, wallet):
    coin = 0
    if col == 1 and row == 2:
        coin = pull_lever_for_coin()
    elif col == 2 and row == 2:  # (2,2) --> pull lever?
        coin = pull_lever_for_coin()
    elif col == 2 and row == 3:  # (2,3) --> pull lever?
        coin = pull_lever_for_coin()
    elif col == 3 and row == 2:  # (3,2) --> pull lever?
        coin = pull_lever_for_coin()

    if coin:
        print(f"You received 1 coin, your total is now {wallet + coin}.")
    return coin


def print_directions(directions_str):
    print("You can travel: ", end="")

    one_done_already = False
    for ch in directions_str:
        if one_done_already:
            print(" or ", end="")

        if ch == NORTH:
            print("(N)orth", end="")
        elif ch == EAST:
            print("(E)ast", end="")
        elif ch == SOUTH:
            print("(S)outh", end="")
        elif ch == WEST:
            print("(W)est", end="")

        one_done_already = True

    print(".")


def play_one_move(col, row, valid_directions, wallet):
    """Plays one move of the game.

    Return whether victory has been obtained, and updated col, row.
    """
    print("Direction: ", end="")
    direction = random.choice([NORTH, EAST, SOUTH, WEST])
    print(direction)
    direction = direction.lower()

    if direction in valid_directions:
        col, row = move(direction, col, row)
        wallet += is_on_lever_tile(col, row, wallet)
    else:
        print("Not a valid direction!")

    return col, row, wallet


def move(direction, col, row):
    """Returns updated col, row given the direction."""

    if direction == NORTH:
        row += 1
    elif direction == SOUTH:
        row -= 1
    elif direction == EAST:
        col += 1
    elif direction == WEST:
        col -= 1
    return (col, row)

def play_tile_traveller():
    # The main program starts here
    row = 1
    col = 1
    wallet = int()
    move_counter = 0

    while not has_won(col, row):
        valid_directions = find_directions(col, row)
        print_directions(valid_directions)
        col, row, wallet = play_one_move(col, row, valid_directions, wallet)
        move_counter += 1

    print(f"Victory! Total coins {wallet}. Moves {move_counter}.")

# Randomness implementation
def initialize() -> None:
    the_seed = int(input("Input seed: "))
    random.seed(the_seed)

def main():
    initialize() # set seed
    PROMPT = "Play again (y/n): "
    play = True
    while play:
        play_tile_traveller()
        if not input(PROMPT).lower() == "y":
            play = False


if __name__ == "__main__":
    main()

'''
You can travel: (N)orth.
Direction: s
Not a valid direction!
You can travel: (N)orth.
Direction: n
Pull a lever (y/n): y
You received 1 coin, your total is now 1.
You can travel: (N)orth or (E)ast or (S)outh.
Direction: N
You can travel: (E)ast or (S)outh.
Direction: w
Not a valid direction!
You can travel: (E)ast or (S)outh.
Direction: E
Pull a lever (y/n): n
You can travel: (E)ast or (W)est.
Direction: e
You can travel: (S)outh or (W)est.
Direction: s
Pull a lever (y/n): y
You received 1 coin, your total is now 2.
You can travel: (N)orth or (S)outh.
Direction: S
Victory! Total coins 2.


'''