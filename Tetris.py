from tkinter import *
import random

GAME_HEIGHT = 640  # Default 640
GAME_WIDTH = int(GAME_HEIGHT / 2)
SIDE_BAR_SIZE = int(GAME_HEIGHT / 4)
SPACE_SIZE = int(GAME_HEIGHT / 20)
BACKGROUND_COLOR = "#25042F"
STARTING_SPEED = 600  # Default 600
REFRESH_SPEED = 1  # Default 5
STARTING_COORDINATES = [((GAME_WIDTH / SPACE_SIZE) / 2 - 1) * SPACE_SIZE, SPACE_SIZE * 1]


# Functions for creating different block types.
def block_type1(x, y, orientation):  # L-block 1
    if orientation == 0:
        coordinates = [[x, y], [x + SPACE_SIZE, y], [x + SPACE_SIZE, y - SPACE_SIZE], [x - SPACE_SIZE, y]]
    elif orientation == 1:
        coordinates = [[x, y], [x, y + SPACE_SIZE], [x + SPACE_SIZE, y + SPACE_SIZE], [x, y - SPACE_SIZE]]
    elif orientation == 2:
        coordinates = [[x, y], [x - SPACE_SIZE, y], [x - SPACE_SIZE, y + SPACE_SIZE], [x + SPACE_SIZE, y]]
    else:
        coordinates = [[x, y], [x, y - SPACE_SIZE], [x - SPACE_SIZE, y - SPACE_SIZE], [x, y + SPACE_SIZE]]
    return coordinates


def block_type2(x, y, orientation):  # L-block 2
    if orientation == 0:
        coordinates = [[x, y], [x + SPACE_SIZE, y], [x - SPACE_SIZE, y - SPACE_SIZE], [x - SPACE_SIZE, y]]
    elif orientation == 1:
        coordinates = [[x, y], [x, y + SPACE_SIZE], [x, y - SPACE_SIZE], [x + SPACE_SIZE, y - SPACE_SIZE]]
    elif orientation == 2:
        coordinates = [[x, y], [x + SPACE_SIZE, y], [x - SPACE_SIZE, y], [x + SPACE_SIZE, y + SPACE_SIZE]]
    else:
        coordinates = [[x, y], [x, y - SPACE_SIZE], [x, y + SPACE_SIZE], [x - SPACE_SIZE, y + SPACE_SIZE]]
    return coordinates


def block_type3(x, y, orientation):  # Square block
    coordinates = [[x, y], [x + SPACE_SIZE, y], [x, y - SPACE_SIZE], [x + SPACE_SIZE, y - SPACE_SIZE]]
    return coordinates


def block_type4(x, y, orientation):  # I-block
    if orientation == 0:
        coordinates = [[x, y], [x + SPACE_SIZE, y], [x + 2*SPACE_SIZE, y], [x - SPACE_SIZE, y]]
    elif orientation == 1:
        coordinates = [[x, y], [x, y + SPACE_SIZE], [x, y - SPACE_SIZE], [x, y + 2*SPACE_SIZE]]
    elif orientation == 2:
        coordinates = [[x, y], [x + SPACE_SIZE, y], [x - 2*SPACE_SIZE, y], [x - SPACE_SIZE, y]]
    else:
        coordinates = [[x, y], [x, y + SPACE_SIZE], [x, y - SPACE_SIZE], [x, y - 2*SPACE_SIZE]]
    return coordinates


def block_type5(x, y, orientation):  # Z-block 1
    if orientation == 0:
        coordinates = [[x, y], [x - SPACE_SIZE, y], [x, y - SPACE_SIZE], [x + SPACE_SIZE, y - SPACE_SIZE]]
    elif orientation == 1:
        coordinates = [[x, y], [x, y - SPACE_SIZE], [x + SPACE_SIZE, y], [x + SPACE_SIZE, y + SPACE_SIZE]]
    elif orientation == 2:
        coordinates = [[x, y], [x + SPACE_SIZE, y], [x, y + SPACE_SIZE], [x - SPACE_SIZE, y + SPACE_SIZE]]
    else:
        coordinates = [[x, y], [x, y + SPACE_SIZE], [x - SPACE_SIZE, y], [x - SPACE_SIZE, y - SPACE_SIZE]]
    return coordinates


def block_type6(x, y, orientation):  # Z-block 2
    if orientation == 0:
        coordinates = [[x, y], [x + SPACE_SIZE, y], [x, y - SPACE_SIZE], [x - SPACE_SIZE, y - SPACE_SIZE]]
    elif orientation == 1:
        coordinates = [[x, y], [x, y + SPACE_SIZE], [x + SPACE_SIZE, y], [x + SPACE_SIZE, y - SPACE_SIZE]]
    elif orientation == 2:
        coordinates = [[x, y], [x - SPACE_SIZE, y], [x, y + SPACE_SIZE], [x + SPACE_SIZE, y + SPACE_SIZE]]
    else:
        coordinates = [[x, y], [x, y - SPACE_SIZE], [x - SPACE_SIZE, y], [x - SPACE_SIZE, y + SPACE_SIZE]]
    return coordinates


def block_type7(x, y, orientation):
    if orientation == 0:
        coordinates = [[x, y], [x + SPACE_SIZE, y], [x - SPACE_SIZE, y], [x, y - SPACE_SIZE]]
    elif orientation == 1:
        coordinates = [[x, y], [x, y + SPACE_SIZE], [x, y - SPACE_SIZE], [x + SPACE_SIZE, y]]
    elif orientation == 2:
        coordinates = [[x, y], [x - SPACE_SIZE, y], [x + SPACE_SIZE, y], [x, y + SPACE_SIZE]]
    else:
        coordinates = [[x, y], [x, y - SPACE_SIZE], [x, y + SPACE_SIZE], [x - SPACE_SIZE, y]]
    return coordinates


class Block:
    """
    Class for the blocks in the game. Each block has coordinates, squares and shadow squares.
    """
    def __init__(self):

        x, y = STARTING_COORDINATES

        self.coordinates = [x, y]
        self.squares = []
        self.shadow_squares = []
        self.shadow_coordinates = []

    def create(self, coordinates, type):
        for pos in coordinates:
            x = pos[0]
            y = pos[1]
            square = canvas.create_rectangle(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=block_dictionary[type][1])
            self.squares.append(square)

    def erase(self):
        for i in range(0, 4):
            canvas.delete(self.squares[0])
            del self.squares[0]

    def create_shadow(self, coordinates):

        at_bottom = False
        step = 0

        while not at_bottom:
            for pos in coordinates:
                x = int(pos[0]/SPACE_SIZE)
                y = int((pos[1] + step)/SPACE_SIZE)

                if y == 19 or bin_matrix[y + 1][x] == 1:
                    at_bottom = True
                    self.shadow_coordinates = [coordinates[0][0], coordinates[0][1] + step]
            step += SPACE_SIZE

        for i in range(0, 4):
            xshadow = coordinates[i][0]
            yshadow = coordinates[i][1] + step - SPACE_SIZE
            square = canvas.create_rectangle(xshadow, yshadow, xshadow + SPACE_SIZE, yshadow + SPACE_SIZE,
                                             fill=BACKGROUND_COLOR, outline=block_dictionary[block_type][1])
            self.shadow_squares.append(square)

    def erase_shadow(self):
        for _ in range(0, 4):
            canvas.delete(self.shadow_squares[0])
            del self.shadow_squares[0]
        self.shadow_coordinates = []


def next_turn():
    global block_falling, block_dictionary, block1, block_type, direction, orientation, bin_matrix, upcoming_blocks, upcoming_positions, turncount, fastforward_enabled, game_speed, speed_multiplier
    """
    Moves falling block one step down. If the block has reached the bottom, the block is placed in the game board. Updates the game speed.
    Checks if any rows are full and deletes them. Creates a new falling block. Checks if the game is over. Creates the three upcoming blocks.
    """

    if block_falling:
        xold, yold = block1.coordinates
        oldcoordinates = block_dictionary[block_type][0](xold, yold, orientation)

        if check_collisions():
            block_falling = False
            fastforward_enabled = False
            window.after(500, enable_fastforward)

            for i in range(0, 4):
                x = oldcoordinates[i][0]
                y = oldcoordinates[i][1]
                square = canvas.create_rectangle(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=block_dictionary[block_type][1])

                row = int(oldcoordinates[i][1]/SPACE_SIZE)
                col = int(oldcoordinates[i][0]/SPACE_SIZE)
                bin_matrix[row][col] = 1
                square_matrix[row][col] = square

            block1.erase()
            block1.erase_shadow()
            check_matrix()
            orientation = 0

        else:
            newcoordinates = block_dictionary[block_type][0](xold, yold + SPACE_SIZE, orientation)

            block1.erase()
            block1.coordinates = newcoordinates[0]
            block1.create(newcoordinates, block_type)

    else:
        turncount += 1
        # Updating the game speed
        if turncount % 10 == 0:
            speed_multiplier += 1
            game_speed = int(STARTING_SPEED * 0.95**speed_multiplier)

        if len(upcoming_blocks) <= 4:
            new_blocks = [1, 2, 3, 4, 5, 6, 7]
            random.shuffle(new_blocks)
            upcoming_blocks.extend(new_blocks)

        # Creating the falling block (block1)
        block_type = upcoming_blocks[0]
        del upcoming_blocks[0]
        x1, y1 = STARTING_COORDINATES
        block1.coordinates = [x1, y1]
        coordinates = block_dictionary[block_type][0](x1, y1, orientation)

        block1.create_shadow(coordinates)
        block1.create(coordinates, block_type)

        block_falling = True

        # Creating the three upcoming blocks (block2, block3 and block4).
        side_blocks = [block2, block3, block4]
        if turncount != 1:
            for blockn in side_blocks:
                blockn.erase()

        for i in range(0, 3):
            x = upcoming_positions[i][0]
            y = upcoming_positions[i][1]
            coords = block_dictionary[upcoming_blocks[i]][0](x, y, 0)
            side_blocks[i].create(coords, upcoming_blocks[i])


def next_turn_callback():
    """
    The main loop of the game. Calls next_turn when the game is not over.
    """
    if bin_matrix[0] == [0]*10:  # First row is empty
        next_turn()
        window.after(game_speed, next_turn_callback)
    else:
        game_over()


def fastforward():
    global fastforward_enabled, is_over
    """
    Fastforwards the game by calling next_turn when the down key is pressed.
    """

    if fastforward_enabled and not is_over:
        next_turn()


def enable_fastforward():
    global fastforward_enabled
    """
    Enables the fastforward function after a block has been placed in the game board.
    """
    fastforward_enabled = True


def skip_turn():
    global block_falling, fastforward_enabled, block_dictionary, block_type, orientation
    """
    Immediately places the block in the game board.
    """

    if block_falling:
        block_falling = False
        fastforward_enabled = False
        window.after(500, enable_fastforward)

        xshadow, yshadow = block1.shadow_coordinates
        coordinates = block_dictionary[block_type][0](xshadow, yshadow, orientation)
        for i in range(0, 4):
            x = coordinates[i][0]
            y = coordinates[i][1]
            square = canvas.create_rectangle(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=block_dictionary[block_type][1])

            row = int(coordinates[i][1] / SPACE_SIZE)
            col = int(coordinates[i][0] / SPACE_SIZE)
            bin_matrix[row][col] = 1
            square_matrix[row][col] = square

        block1.erase()
        block1.erase_shadow()
        check_matrix()
        orientation = 0


def update_status():
    global block_falling, block_type, direction, orientation, block1
    """
    Updates the status of the game bases on the speed defined by the variable REFRESH_SPEED.
    """

    if block_falling:
        xold, yold = block1.coordinates
        newcoordinates = []

        if direction == 0:
            newcoordinates = block_dictionary[block_type][0](xold, yold, orientation)
        elif direction == 1:
            newcoordinates = block_dictionary[block_type][0](xold - SPACE_SIZE, yold, orientation)
            direction = 0
        else:
            newcoordinates = block_dictionary[block_type][0](xold + SPACE_SIZE, yold, orientation)
            direction = 0

        block1.erase()
        block1.erase_shadow()
        block1.coordinates = newcoordinates[0]
        block1.create_shadow(newcoordinates)
        block1.create(newcoordinates, block_type)

    window.after(REFRESH_SPEED, update_status)


def check_collisions():
    global block_type, block_dictionary, block_falling, bin_matrix
    """
    Cheks if the block has collided with the bottom or another block.
    """

    x, y = block1.coordinates
    coordinates = block_dictionary[block_type][0](x, y, orientation)

    for square in coordinates:
        row = int(square[1]/SPACE_SIZE)
        col = int(square[0]/SPACE_SIZE)
        if square[1] == GAME_HEIGHT - SPACE_SIZE or bin_matrix[row + 1][col] == 1:
            return True


def change_orientation():
    global orientation, block1, block_type, bin_matrix
    """
    Checks if the block can be rotated. If it can, the block is rotated.
    """

    new_orientation = 0

    if orientation != 3:
        new_orientation = orientation + 1
    else:
        new_orientation = 0

    def is_inside(coordinates):
        block_inside = []
        inside = False

        for square in coordinates:
            new_row = int(square[1] / SPACE_SIZE)
            new_col = int(square[0] / SPACE_SIZE)

            if new_col < 0 or new_col > 9 or bin_matrix[new_row][new_col] == 1:
                block_inside = square
                inside = True

        return [inside, block_inside]

    x, y = block1.coordinates
    new_coordinates = block_dictionary[block_type][0](x, y, new_orientation)
    iteration = 0

    while is_inside(new_coordinates)[0] and iteration <= 2:

        if is_inside(new_coordinates)[1][0] < x:
            xnew = new_coordinates[0][0] + SPACE_SIZE
            new_coordinates = block_dictionary[block_type][0](xnew, y, new_orientation)

        elif is_inside(new_coordinates)[1][0] > x:
            xnew = new_coordinates[0][0] - SPACE_SIZE
            new_coordinates = block_dictionary[block_type][0](xnew, y, new_orientation)

        iteration += 1

    if iteration != 3:
        block1.coordinates = new_coordinates[0]
        orientation = new_orientation


def move_to(new_direction):
    global direction, block1, block_type, bin_matrix, bin_matrix
    """
    Checks if the block can be moved to the new direction. If it can, the block is moved.
    """

    x, y = block1.coordinates
    coordinates = block_dictionary[block_type][0](x, y, orientation)
    next_to = False

    for square in coordinates:
        row = int(square[1] / SPACE_SIZE)
        col = int(square[0] / SPACE_SIZE)

        if square[0] == 0 and new_direction == 1:
            next_to = True
        elif int(square[0]/SPACE_SIZE) == 9 and new_direction == 2:
            next_to = True
        elif new_direction == 1 and bin_matrix[row][col - 1] == 1:
            next_to = True
        elif new_direction == 2 and bin_matrix[row][col + 1] == 1:
            next_to = True
        else:
            pass

    if not next_to:
        direction = new_direction


def check_matrix():
    global bin_matrix, square_matrix, score
    """
    Checks if any rows are full and deletes them. Updates the score.
    """

    rows_to_delete = []

    # Find rows to delete
    for row in reversed(range(len(bin_matrix))):
        if all(bin_matrix[row]):
            rows_to_delete.append(row)

    # Delete and update rows
    for row in reversed(rows_to_delete):
        for j in range(len(bin_matrix[0])):
            if bin_matrix[row][j] == 1:
                canvas.delete(square_matrix[row][j])

        # Update bin_matrix and square_matrix
        old_bin_matrix = bin_matrix.copy()
        old_square_matrix = square_matrix.copy()
        for i in range(row, 0, -1):
            bin_matrix[i] = old_bin_matrix[i - 1]
            square_matrix[i] = old_square_matrix[i - 1]

        bin_matrix[0] = [0] * 10
        square_matrix[0] = [0] * 10

        for i in range(1, row + 1):
            for j in range(len(bin_matrix[0])):
                if bin_matrix[i][j] == 1:
                    canvas.move(square_matrix[i][j], 0, SPACE_SIZE)

    # Update score
    if len(rows_to_delete) == 1:
        score += 40
    elif len(rows_to_delete) == 2:
        score += 100
    elif len(rows_to_delete) == 3:
        score += 300
    elif len(rows_to_delete) == 4:
        score += 1200
    score_label.config(text="Score: {}".format(score))


def initialize_game():
    global score_label, next_label, is_over, bin_matrix, square_matrix, score, direction, score_file, turncount, fastforward_enabled, block_falling, block_dictionary, block_type, upcoming_blocks, upcoming_positions, orientation, block1, block2, block3, block4, speed_multiplier, game_speed
    """
    Initializes game variables and creates the game board for a new game.
    """

    orientation = 0  # Block orientation gets values from 0 to 3. 0 = starting orientation.
    block_falling = False

    # Dictionary for block types and their colors.
    block_dictionary = {1: [block_type1, "#F2F911"], 2: [block_type2, "#F93F11"], 3: [block_type3, "#89F911"],
                        4: [block_type4, "#BD11F9"], 5: [block_type5, "#1DE5F1"], 6: [block_type6, "#F1A11D"], 7: [block_type7, "#F246F2"]}
    block_type = None

    upcoming_blocks = [1, 2, 3, 4, 5, 6, 7]
    random.shuffle(upcoming_blocks)
    upcoming_positions = [[SPACE_SIZE*11.5, SPACE_SIZE*7], [SPACE_SIZE*11.5, SPACE_SIZE*10], [SPACE_SIZE*11.5, SPACE_SIZE*13]]

    is_over = False
    score = 0
    direction = 0  # 0 = do nothing, 1 = Left, 2 = Right.

    score_file = "tetris_score.txt"
    turncount = 0
    fastforward_enabled = True
    game_speed = STARTING_SPEED
    speed_multiplier = 0


    #  Stores placements of each square.
    rows, cols = 20, 10
    bin_matrix = [([0] * cols) for _ in range(rows)]

    #  Stores drawn pictures of the squares.
    square_matrix = [([0] * cols) for _ in range(rows)]

    canvas.delete(ALL)
    # Creating the game-board.
    for i in range(len(bin_matrix)):
        for j in range(len(bin_matrix[0])):
            x = j * SPACE_SIZE
            y = i * SPACE_SIZE
            canvas.create_rectangle(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=BACKGROUND_COLOR)

    canvas.create_rectangle(GAME_WIDTH, 0, GAME_WIDTH + SPACE_SIZE/4, GAME_HEIGHT, fill="white")
    score_label = Label(window, text="Score: {}".format(score), font=('Comic Sans MS', 15), bg=BACKGROUND_COLOR, fg="white")

    score_label.place(x=GAME_WIDTH + SPACE_SIZE/3, y=2)
    next_label = Label(window, text="Next", font=('Comic Sans MS', 15), bg=BACKGROUND_COLOR, fg="white")

    next_label.place(x=GAME_WIDTH + SPACE_SIZE/3, y=SPACE_SIZE*4)

    # Game block and three visible blocks in the side bar. 
    block1 = Block()
    block2 = Block()
    block3 = Block()
    block4 = Block()


def create_starting_screen():
    global is_over, block_falling
    """
    Creates the starting screen.
    """

    is_over = True
    block_falling = False

    # Tetrsis text with each letter in a different color.
    colors = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet']
    text = "TETRIS"
    for i, letter in enumerate(text):
        canvas.create_text(
            canvas.winfo_width()/2 - 75 + (i * 30),  # Position each letter next to each other
            canvas.winfo_height()*2/14,
            font=('consolas', 40),
            text=letter,
            fill=colors[i]
        )
    canvas.create_text(canvas.winfo_width()/2, canvas.winfo_height()*3/14,
                       font=('Comic Sans MS', 14), text="By Markus Junttila", fill="white")    
    # Instructions
    canvas.create_text(canvas.winfo_width()/2, canvas.winfo_height()*9/14,
                          font=('Comic Sans MS', 16), text="Use arrow keys to move and rotate blocks", fill="white")
    canvas.create_text(canvas.winfo_width()/2, canvas.winfo_height()*10/14,
                            font=('Comic Sans MS', 16), text="Press space to skip a turn", fill="white")
    canvas.create_text(canvas.winfo_width()/2, canvas.winfo_height()*12/14,
                       font=('Comic Sans MS', 20), text="Press Enter to start", fill="white")


def start_game():
    global is_over
    """
    Starts new game.
    """

    if is_over:
        initialize_game()  # Initialize game variables and create game board.
        next_turn_callback()  # Start the game loop.


def game_over():
    global is_over, score_label, next_label, is_over
    """
    Ends the game and shows the game over screen.
    """

    is_over = True
    # Save score to a file
    with open(score_file, "a") as file:
        file.write(str(score) + "\n")
    
    # Get high score
    high_score = 0
    with open(score_file, "r") as file:
        scores = file.readlines()
        for s in scores:
            if int(s) > high_score:
                high_score = int(s)

    canvas.delete(ALL)
    canvas.create_text(canvas.winfo_width()/2, canvas.winfo_height()/2,
                       font=('consolas', 40), text="GAME OVER", fill="red")
    canvas.create_text(canvas.winfo_width()/2, canvas.winfo_height()*8/14,
                       font=('Comic Sans MS', 20), text="Score: "+str(score), fill="white")
    canvas.create_text(canvas.winfo_width()/2, canvas.winfo_height()*9/14,
                    font=('Comic Sans MS', 20), text="High score: "+str(high_score), fill="white")
    canvas.create_text(canvas.winfo_width()/2, canvas.winfo_height()*12/14,
                    font=('Comic Sans MS', 16), text="Press Enter to start a new game", fill="white")
    score_label.destroy()
    next_label.destroy()


# Create Tkinter window and canvas.
window = Tk()
window.title("Tetris")
window.resizable(False, False)
canvas = Canvas(window, bg=BACKGROUND_COLOR, height=GAME_HEIGHT, width=GAME_WIDTH + SIDE_BAR_SIZE)
canvas.pack()
window.update()

window_width = window.winfo_width()
window_height = window.winfo_height()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

x = int((screen_width / 2) - (window_width / 2))
y = int((screen_height / 2) - (window_height / 2) - window_height / 15)

window.geometry(f"{window_width}x{window_height}+{x}+{y}")

# Bind keys to functions.
window.bind('<Up>', lambda _: change_orientation())
window.bind('<Left>', lambda _: move_to(1))
window.bind('<Right>', lambda _: move_to(2))
window.bind('<Down>', lambda _: fastforward())
window.bind('<space>', lambda _: skip_turn())
window.bind('<Return>', lambda _: start_game())

create_starting_screen()  # Create the starting screen.
update_status()  # Update the status of the game.

window.mainloop()