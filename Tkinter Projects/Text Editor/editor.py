from tkinter import *
from tkinter.filedialog import *
import tkinter.messagebox
import os

# New file title
newfile = 'New File'

# Saving a new file with desired name. Can edit an existing file with existing name.
def save():
    save_text = text.get("1.0",END)
    title = root.title()
    if title == (newfile +  ' - Text Editor'):
        currentPath = asksaveasfilename(filetypes=[('Text Document', '*.txt')])
    else:
        currentPath = title[:-14]
    with open(currentPath, 'w') as file:
        file.write(save_text)
    root.title(currentPath + ' - Text Editor')
    tkinter.messagebox.showinfo("", "File is saved!")

# open a txt file of choice from the directory for read and edit
def open_file():
    file = askopenfilename(filetypes=[('Text Document', '*.txt')])
    root.title(file + ' - Text Editor')
    with open(file, 'r') as f:
        text.delete(1.0,END)
        text.insert(INSERT,f.read())

# Erase and delete the current file from the directory 
def delete_file():
    currentPath = root.title()[:-14]
    response = tkinter.messagebox.askquestion("", "Are you sure you want to delete the file?")
    if response == "yes":
        if currentPath != newfile:
            os.remove(currentPath)
        text.delete("1.0", END)
        tkinter.messagebox.showinfo("", "File is deleted!")
        new_file()
        

# Opens a new blank file with new file title        
def new_file():
    text.delete("1.0", END)
    root.title(newfile +  ' - Text Editor')



# Creating the Tkinter window
root = Tk()
root.title(newfile +  ' - Text Editor')
root.geometry("500x400")

# Creating the file menu 
file_menu = Menu(root)
root.config(menu=file_menu)

# Creating the sub menu buttons
sub_menu = Menu(file_menu)
file_menu.add_cascade(label="File", menu=sub_menu)
sub_menu.add_command(label="New", command= new_file)
sub_menu.add_command(label="Open", command=open_file)
sub_menu.add_separator()
sub_menu.add_command(label="Save", command= lambda: save())
sub_menu.add_command(label="Delete", command=delete_file)

# Text field
text = Text(root)
text.pack(expand=True)
text.config(state='normal')

root.mainloop()
