# Constants
NORTH = "n"
EAST = "e"
SOUTH = "s"
WEST = "w"


def has_won(col, row):
    """Return true if player is in the victory cell."""

    return col == 3 and row == 1  # (3,1)


def find_directions(col, row):
    """Returns valid directions as a string given the supplied location."""

    if col == 1 and row == 1:  # (1,1)
        valid_directions = NORTH
    elif col == 1 and row == 2:  # (1,2)
        valid_directions = NORTH + EAST + SOUTH
    elif col == 1 and row == 3:  # (1,3)
        valid_directions = EAST + SOUTH
    elif col == 2 and row == 1:  # (2,1)
        valid_directions = NORTH
    elif col == 2 and row == 2:  # (2,2)
        valid_directions = SOUTH + WEST
    elif col == 2 and row == 3:  # (2,3)
        valid_directions = EAST + WEST
    elif col == 3 and row == 2:  # (3,2)
        valid_directions = NORTH + SOUTH
    elif col == 3 and row == 3:  # (3,3)
        valid_directions = SOUTH + WEST

    return valid_directions


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


def play_one_move(col, row, valid_directions):
    """Plays one move of the game.

    Return whether victory has been obtained, and updated col, row.
    """

    direction = input("Direction: ")
    direction = direction.lower()

    if direction in valid_directions:
        col, row = move(direction, col, row)
    else:
        print("Not a valid direction!")

    return col, row


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


# The main program starts here
row = 1
col = 1

while not has_won(col, row):
    valid_directions = find_directions(col, row)
    print_directions(valid_directions)
    col, row = play_one_move(col, row, valid_directions)

print("Victory!")
