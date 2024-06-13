from tkinter import Button
import random
import settings

class Cell:
    all = []
    def __init__(self, x,y, is_mine=False): # every time when we want to create an instance
        self.is_mine = is_mine
        self.cell_btn_object = None #will eventually hold a reference to the Button object associated with this cell.
        self.x = x
        self.y = y

        # Append the object to the Cell.all list
        Cell.all.append(self)

    def create_btn_object(self, location): #locaion is presumably the parent widget
        btn = Button(
            location,
            width=12,
            height=4,

        )
        btn.bind('<Button-1>', self.left_click_action) #Left Click
        btn.bind('<Button-3>', self.right_click_action) #Right Click
        self.cell_btn_object = btn

    def left_click_action(self, event):
      if self.is_mine:
          self.show_mine()
      else:
          self.show_cell()
            #the number which represents the amount of minds that
            #are surrounded the click cell

    def get_cell_by_axis(self, x, y):
         # Return a cell object based on the value of x, y
        for cell in Cell.all:
            if cell.x == x and cell.y == y:
                return cell
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
        self.cell_btn_object.configure(text=self.surrounded_cells_mines_length)
        #to eliminate the nuns
    def show_mine(self):
            #A logic to interupt the game and display a message that player lost
            self.cell_btn_object.configure(bg='red')
    def right_click_action(self, event):
        print(event)
        print("I am right clicked!")

    @staticmethod
    def randomize_mines():
        picked_cells = random.sample(
            Cell.all,
            settings.MINES_COUNT
        )
        for picked_cell in picked_cells:
            picked_cell.is_mine = True

    #magic method
    def __repr__(self):
        return f"Cell: {self.x}, {self.y}"