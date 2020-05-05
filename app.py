from tkinter import Menu
from tkinter import messagebox
from banner import Banner
from item import ChecklistItem
from content import Content

class App:
    
    def __init__(self, master):
        # Prevent the app window from being resized
        master.resizable(False, False)
        self.banner = Banner(master)
        self.content = Content(master)

        # KEYBOARD SHORTCUTS SECTION
        master.bind('<Control-n>', lambda e: self.content.add_task())

        # MENU BAR SECTION
        master.option_add('*tearOff', False)
        self.menubar = Menu(master)
        master.config(menu=self.menubar)

        # FILE MENU
        file = Menu(self.menubar)
        file.add_command(label='Test', command=lambda: messagebox.showinfo(title='Test', message='This is a test.'))
        file.add_command(label='Add Task', command=lambda: self.content.add_task())
        file.entryconfig('Add Task', accelerator='CTRL+N')
        self.menubar.add_cascade(menu=file, label='File')