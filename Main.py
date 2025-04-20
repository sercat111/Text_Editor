n = "Notepad"
edit = "Edit"
newtab = "New Tab" + "   Ctrl+N"
import tkinter as tk
from tkinter import filedialog, colorchooser, messagebox, Button
import whitespace


def open_file():
    def callback():
        file_path = filedialog.askopenfilename(parent=root)
        messagebox.showinfo("No Command", file_path)
        print(file_path)
    return callback
def language():
    global n
    global edit
    global newtab
    n = "Блокнот"
    edit += "Изменить"
    newtab += "Новая вкладка" + "   Ctrl+N"
    root.title(n)
    def callback():
        print("Language")
    return callback
root = tk.Tk()
root.geometry("1650x700")
root.title(n)
head_tabs = tk.Menu(root)
def new_tab():
    tab = Button(root)
    def callback():
        print("New Tab")
    return callback
head_menu = tk.Menu(root)
root.config(menu=head_menu)

file_menu = tk.Menu(head_menu)
Edit = tk.Menu(head_menu)
View = tk.Menu(head_menu)
head_menu.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label=newtab, command=new_tab())
file_menu.add_command(label="New window    Ctrl+Shift+N", command=open_file())
file_menu.add_command(label="Open    Ctrl+O", command=open_file())
file_menu.add_command(label="Save    Ctrl+S", command=open_file())
file_menu.add_command(label="Save as    Ctrl+Shift+S", command=open_file())
file_menu.add_command(label="Print    Ctrl+P", command=open_file())
head_menu.add_cascade(label=edit, menu=Edit)
Edit.add_command(label="Cancel       Ctrl+Z", command=open_file())
head_menu.add_cascade(label="View", menu=View)
View.add_command(label="Language       Ctrl+l", command=language())

root.mainloop()