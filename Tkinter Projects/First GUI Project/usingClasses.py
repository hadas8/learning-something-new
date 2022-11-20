from tkinter import *

class Mybuttons:
    def __init__(self, root1):
        frame = Frame(root1)
        frame.pack()

        self.printButton = Button(frame, text="Click Here", command=self.printMessage)
        self.printButton.pack()

        self.quitButton = Button(frame, text="Exit", command=frame.quit)
        self.quitButton.pack(side=RIGHT)

    def printMessage(self):
        print("Button Clicked")

root = Tk()
b = Mybuttons(root)

root.mainloop()