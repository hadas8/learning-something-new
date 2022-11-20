from tkinter import *

# create a window in root
root = Tk()
# create frame
newFrame = Frame(root)
newFrame.pack()

# determine place of the frame at the bottom of the window
otherFrame = Frame(root)
otherFrame.pack(side=BOTTOM)

# add buttons with text and color to the frames
button1 = Button(newFrame, text="Click Here", fg="Red")
button2 = Button(otherFrame, text="Click Here", fg="Blue")

button1.pack()
button2.pack()

root.mainloop()
