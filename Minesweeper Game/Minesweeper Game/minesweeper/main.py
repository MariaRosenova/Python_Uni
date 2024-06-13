from tkinter import *

root = Tk()
#Override the settings of the window
root.configure(bg="black")
root.geometry('1440x720')
root.title('Minesweeper Game')
root.resizable(False, False)

top_frame = Frame(
    root,
    bg='red', #Change later to black
    width=1440,
    height=180
)
top_frame.place(x=0, y=0)

#left side bar
left_frame = Frame(
    bg="blue", #Change later to black
    width=360,
    height=540
)
left_frame.place(x=0, y=180)

#Run the window
root.mainloop()