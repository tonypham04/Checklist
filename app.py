from tkinter import Menu
from tkinter import messagebox
from banner import Banner
from item import ChecklistItem
from content import Content

class App:
    
    def __init__(self, master):
        # Prevent the app window from being resized
        master.resizable(False, False)
        default_image_path = 'images/gimp_themes/maple_leaves.png'
        self.banner = Banner(master, default_image_path)
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

        # THEMES MENU
        themes = Menu(self.menubar)
        gimp_themes = Menu(themes)
        gimp_themes.add_command(label='Maple Leaves (Default)', command=lambda: self.change_theme('images/gimp_themes/maple_leaves.png'))
        gimp_themes.add_cascade(label='Lightning', command=lambda: self.change_theme('images/gimp_themes/lightning.png'))
        gimp_themes.add_cascade(label='Chocolate Swirl', command=lambda: self.change_theme('images/gimp_themes/chocolate_swirl.png'))
        themes.add_cascade(menu=gimp_themes, label = 'GIMP Themes')
        self.menubar.add_cascade(menu=themes, label='Themes')

    def change_theme(self, image_path=None, foreground=None, background=None):
        if image_path is not None:
            self.banner.change_image(image_path)