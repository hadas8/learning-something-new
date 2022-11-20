from tkinter import *

def function1():
    print('Menu item clicked')

root = Tk()

my_menu = Menu(root)
root.config(menu=my_menu)

sub_menu = Menu(my_menu)
my_menu.add_cascade(label="File", menu=sub_menu)

sub_menu.add_command(label="Project", command=function1)
sub_menu.add_command(label="Save", command=function1)

sub_menu.add_separator()
sub_menu.add_command(label="Exit", command=function1)

new_menu = Menu(my_menu)
my_menu.add_cascade(label="Edit", menu=new_menu)
new_menu.add_command(label="Undo")


toolbar = Frame(root, bg="Pink")
insert_button = Button(toolbar, text="Insert Files", command=function1)
insert_button.pack(side=LEFT, padx=2, pady=3)

print_button = Button(toolbar, text="Print", command=function1)
print_button.pack(side=LEFT, padx=2, pady=3)

toolbar.pack(side=TOP, fill=X)

status = Label(root, text="This is the status", bd=1, relief=SUNKEN, anchor=W)
status.pack(side=BOTTOM, fill=X)

root.mainloop()