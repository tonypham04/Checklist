from tkinter import Menu
from tkinter import messagebox
from tkinter import ttk
from tkinter import PhotoImage

class Banner:
    
    def __init__(self, master):
        # MENU BAR SECTION
        # Remove dashes from the menubar drop down
        master.option_add('*tearOff', False)
        self.menubar = Menu(master)
        master.config(menu=self.menubar)
        
        file = Menu(self.menubar)
        # THEMES SECTION
        themes = Menu(self.menubar)
        gimp_themes = Menu(themes)
        gimp_themes.add_command(label='Maple Leaves (Default)', command=lambda: self.change_theme('images/gimp_themes/maple_leaves.png'))
        gimp_themes.add_command(label='Lightning', command=lambda: self.change_theme('images/gimp_themes/lightning.png'))
        gimp_themes.add_command(label='Chocolate Swirl', command=lambda: self.change_theme('images/gimp_themes/chocolate_swirl.png'))
        themes.add_cascade(menu=gimp_themes, label='GIMP Themes')

        # ADD COMMANDS SECTION
        file.add_command(label='Test', command=lambda: messagebox.showinfo(title='Test', message='This is a test.'))

        # ADD TO MENU BAR SECTION
        self.menubar.add_cascade(menu=file, label='File')
        self.menubar.add_cascade(menu=themes, label='Themes')

        # BANNER IMAGE SECTION
        # Create widgets
        self.banner_frame = ttk.Frame(master, height=180, width=480, relief='solid')
        self.banner_img = PhotoImage(file='images/gimp_themes/maple_leaves.png')
        self.banner_img_label = ttk.Label(self.banner_frame)
        self.banner_img_label.img = self.banner_img
        self.banner_img_label.config(image=self.banner_img_label.img)

        # Place widgets
        self.banner_img_label.pack()
        self.banner_frame.pack()

    # Remove the old theme and replace with new theme
    def change_theme(self, path=None):
        if path is not None:
            self.banner_img_label.forget()
            self.banner_img = PhotoImage(file=path)
            self.banner_img_label = ttk.Label(self.banner_frame)
            self.banner_img_label.img = self.banner_img
            self.banner_img_label.config(image=self.banner_img_label.img)
            self.banner_img_label.pack()