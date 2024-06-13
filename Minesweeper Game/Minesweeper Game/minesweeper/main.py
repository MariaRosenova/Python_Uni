from tkinter import *
from cell import Cell
import settings
import utils

root = Tk()
# Override the settings of the window
root.configure(bg="black")
root.geometry(f'{settings.WIDTH}x{settings.HEIGHT}')
root.title('Minesweeper Game')
root.resizable(False, False)

top_frame = Frame(
    root,
    bg='black',
    width=settings.WIDTH,
    height=utils.height_prct(25)
)  # game information
top_frame.place(x=0, y=0)

game_title = Label(
    top_frame,
    bg='black',
    fg='white',
    text='Minesweeper Game',
    font=('arial', 48, 'bold')
)
game_title.place(
    x=utils.width_prct(25),
    y=utils.height_prct(5),
    )

# left sidebar
left_frame = Frame(
    bg="black",
    width=utils.width_prct(25),
    height=utils.height_prct(75)
)  # game settings or navigation
left_frame.place(x=0, y=utils.height_prct(25))

center_frame = Frame(
    root,
    bg='black',
    width=utils.width_prct(75),
    height=utils.height_prct(750)
)  # intended for the Minesweeper grid
center_frame.place(
    x=utils.width_prct(25),
    y=utils.height_prct(25),
)

for x in range(settings.GRID_SIZE):  # used to create a grid of 'Cell' instances within 'center_frame'
    for y in range(settings.GRID_SIZE):
        c = Cell(x, y)  # create an instance
        c.create_btn_object(center_frame)  # creates a 'Button' widget associated with tje cell
        c.cell_btn_object.grid(
            column=x,
            row=y
        )  # places the button in the grid layout of 'center_frame'

# Call the label from the Cell class
Cell.create_cell_count_label(left_frame)
Cell.cell_count_label_object.place(
    x=0, y=0
)

Cell.randomize_mines()

# Run the window
root.mainloop()  # starts the tkinter event loop, which waits for user interactions and handles events like button
# clicks
