from tkinter import *

root = Tk()

# label with background and foreground color
label1 = Label(root, text="First", bg="Red", fg="White")
# adjust the label to fill the width of the window
label1.pack(fill=X)

label2 = Label(root, text="Second", bg="Blue", fg="Green")
label2.pack(side=LEFT, fill=Y)
root.mainloop()
