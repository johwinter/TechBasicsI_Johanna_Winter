
import turtle
import random

BACKGROUND_COLOR = "#1a1a2e"
COLOR_PALETTE = ["#264653", "#2a9d8f", "#e9c46a", "#f4a261", "#e76f51"]

GRID_SIZE = 7
CELL_SIZE = 60
PEN_SIZE = 2

MIN_SHAPE_SIZE = 10     # smallest possible random shape size
MAX_SHAPE_SIZE = 25     # largest possible random shape size

# SETUP FUNCTION

def setup_screen():
    """Creates and configures the turtle screen and pen. Returns both."""
    screen = turtle.Screen()
    screen.bgcolor(BACKGROUND_COLOR)
    screen.title("Generative Art")
    screen.tracer(0)

    pen = turtle.Turtle()
    pen.hideturtle()
    pen.speed(0)
    pen.pensize(PEN_SIZE)

    return screen, pen

# HELPER FUNCTION WITH RETURN VALUE

def calculate_grid_start(grid_size, cell_size):
    """
    Calculates the top-left starting coordinates so the grid
    is centered on the screen. Takes arguments and returns a value.
    """
    start_x = -(grid_size * cell_size) // 2
    start_y = (grid_size * cell_size) // 2
    return start_x, start_y

# DRAWING FUNCTIONS

def draw_circle(pen, x, y, size, color):
    """Draws a filled circle at position (x, y)."""
    pen.penup()
    pen.goto(x, y - size)  # turtle draws circles from the bottom
    pen.pendown()
    pen.fillcolor(color)
    pen.begin_fill()
    pen.circle(size)
    pen.end_fill()


def draw_square(pen, x, y, size, color):
    """Draws a filled square at position (x, y)."""
    pen.penup()
    pen.goto(x, y)
    pen.pendown()
    pen.fillcolor(color)
    pen.begin_fill()
    for _ in range(4):  # a square has 4 sides
        pen.forward(size)
        pen.right(90)
    pen.end_fill()


def draw_random_shape(pen, x, y):
    """
    Picks a random color, size and shape, then draws it at (x, y).
    Keeps the random-choice logic out of the main loop.
    """
    color = random.choice(COLOR_PALETTE)
    size = random.randint(MIN_SHAPE_SIZE, MAX_SHAPE_SIZE)
    shape = random.choice(["circle", "square"])

    if shape == "circle":
        draw_circle(pen, x + CELL_SIZE // 2, y - CELL_SIZE // 2, size, color)
    elif shape == "square":
        draw_square(pen, x + CELL_SIZE // 2 - size // 2,
                     y - CELL_SIZE // 2 + size // 2, size, color)


def draw_grid(pen, start_x, start_y):
    """Loops through every cell of the grid and draws a random shape in it."""
    for row in range(GRID_SIZE):
        for col in range(GRID_SIZE):
            x = start_x + col * CELL_SIZE
            y = start_y - row * CELL_SIZE
            draw_random_shape(pen, x, y)


# MAIN FUNCTION - controls the overall program flow

def main():
    screen, pen = setup_screen()
    start_x, start_y = calculate_grid_start(GRID_SIZE, CELL_SIZE)

    draw_grid(pen, start_x, start_y)

    screen.update()        # draw everything at once (tracer was off)
    screen.exitonclick()   # click the window to close it


if __name__ == "__main__":
    main()


# I wanted to build a code that extended what we had done in class and add another
# layer with the colors.
# I had to edit it a couple of times as the first code was bugging and the color codes were incomplete.
#
# Refactoring notes:
# - Grouped all constants at the top in UPPER_CASE
# - Added calculate_grid_start() as a function that takes arguments and returns a value
# - Split the random-shape logic into its own function (draw_random_shape) to keep
#   the nested loop in draw_grid() short and readable
# - Added a main() function that controls the program flow, called via
#   the standard "if __name__ == '__main__':" pattern
