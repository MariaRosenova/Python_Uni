import sys
from tkinter import Button, Label
import random
import settings
import ctypes


class Cell:
    all = []
    cell_count = settings.CELL_COUNT
    cell_count_label_object = None

    def __init__(self, x, y, is_mine=False):  # every time when we want to create an instance
        self.is_mine = is_mine
        self.is_opened = False
        self.is_mine_candidate = False
        self.cell_btn_object = None  # will eventually hold a reference to the Button object associated with this cell.
        self.x = x
        self.y = y

        # Append the object to the Cell.all list
        Cell.all.append(self)

    def create_btn_object(self, location):  # location is presumably the parent widget
        btn = Button(
            location,
            width=6,
            height=2,
            bg='#4CAF50',
            fg='black',
            font=('Helvetica', 14, 'bold'),
            relief='raised',
            borderwidth=2,

        )
        btn.bind('<Button-1>', self.left_click_action)  # Left Click
        btn.bind('<Button-3>', self.right_click_action)  # Right Click
        self.cell_btn_object = btn

    @staticmethod
    def create_cell_count_label(location):
        lbl = Label(
            location,
            bg='black',
            fg='white',
            text=f"Cells Left: {settings.CELL_COUNT}",
            width=12,
            height=4,
            font=("Helvetica", 17, 'bold')
        )
        Cell.cell_count_label_object = lbl

    def left_click_action(self, event):
        if self.is_mine:
            self.show_mine()
        else:
            if self.surrounded_cells_mines_length == 0:
                for cell_obj in self.surrounded_cells:
                    cell_obj.show_cell()
            self.show_cell()
            # If Mines count is equal to the cells left count, player won
            if Cell.cell_count == settings.MINES_COUNT:
                ctypes.windll.user32.MessageBoxW(0, 'Congratulations! You won the game!', 'Game Over', 0)
        # Cancel left and Right click events if cell is already opened:
        self.cell_btn_object.unbind('<Button-1>')
        self.cell_btn_object.unbind('<Button-3>')
        # the number which represents the amount of minds that
        # are surrounded the click cell

    def get_cell_by_axis(self, x, y):
        # Return a cell object based on the value of x, y
        for cell in Cell.all:
            if cell.x == x and cell.y == y:
                return cell
            else:
                self.cell_btn_object.configure(
                    bg="SystemButtonFace"
                )

    @property
    def surrounded_cells(self):
        cells = [
            self.get_cell_by_axis(self.x - 1, self.y - 1),
            self.get_cell_by_axis(self.x - 1, self.y),
            self.get_cell_by_axis(self.x - 1, self.y + 1),
            self.get_cell_by_axis(self.x, self.y - 1),
            self.get_cell_by_axis(self.x + 1, self.y - 1),
            self.get_cell_by_axis(self.x + 1, self.y),
            self.get_cell_by_axis(self.x + 1, self.y + 1),
            self.get_cell_by_axis(self.x, self.y + 1)
        ]
        cells = [cell for cell in cells if cell is not None]
        return cells

    @property
    def surrounded_cells_mines_length(self):
        counter = 0
        for cell in self.surrounded_cells:
            if cell.is_mine:
                counter += 1
        return counter

    def show_cell(self):
        if not self.is_opened:
            Cell.cell_count -= 1
            self.cell_btn_object.configure(text=self.surrounded_cells_mines_length)
            # to eliminate the nuns
            # Replace the text of cell count label with the newer count
            if Cell.cell_count_label_object:
                Cell.cell_count_label_object.configure(
                    text=f"Cells Left: {Cell.cell_count}"
                )
                self.cell_btn_object.configure(
                    bg="SystemButtonFace"
                )
        # Mark the cell as opened (Use is as the last line on this method)
        self.is_opened = True

    def show_mine(self):
        # A logic to interrupt the game and display a message that player lost
        self.cell_btn_object.configure(bg="red")
        ctypes.windll.user32.MessageBoxW(0, 'You clicked on a mine', 'Game Over', 0)
        sys.exit()

    def right_click_action(self, event):
        if not self.is_mine_candidate:
            self.cell_btn_object.configure(
                bg="orange"
            )
        else:
            self.cell_btn_object.configure(
                bg='#4CAF50'
            )
            self.is_mine_candidate = True

    @staticmethod
    def randomize_mines():
        picked_cells = random.sample(
            Cell.all,
            settings.MINES_COUNT
        )
        for picked_cell in picked_cells:
            picked_cell.is_mine = True

    @staticmethod
    def get_color_by_mine_count(mine_count):
        colors = {
            0: 'black',
            1: 'blue',
            2: 'green',
            3: 'red',
            4: 'purple',
            5: 'maroon',
            6: 'turquoise',
            7: 'black',
            8: 'grey'
        }
        return colors.get(mine_count, 'black')

    # magic method
    def __repr__(self):
        return f"Cell: {self.x}, {self.y}"
