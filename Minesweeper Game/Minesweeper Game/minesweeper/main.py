from tkinter import *
import settings
import utils

root = Tk()
#Override the settings of the window
root.configure(bg="black")
root.geometry(f'{settings.WIDTH}x{settings.HEIGHT}')
root.title('Minesweeper Game')
root.resizable(False, False)

top_frame = Frame(
    root,
    bg='red', #Change later to black
    width=settings.WIDTH,
    height=utils.height_prct(25)
)
top_frame.place(x=0, y=0)

#left side bar
left_frame = Frame(
    bg="blue", #Change later to black
    width=utils.width_prct(25),
    height=utils.height_prct(75)
)
left_frame.place(x=0, y=utils.height_prct(25))

#Run the window
root.mainloop()