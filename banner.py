from tkinter import Menu
from tkinter import messagebox
from tkinter import ttk
from tkinter import Label
from tkinter import colorchooser

# REFERENCES SECTION
# Creating a right-click menu with tkinter: https://stackoverflow.com/questions/12014210/tkinter-app-adding-a-right-click-context-menu

class Banner:
    
    def __init__(self, master):
        
        # Create widgets
        self.banner_frame = ttk.Frame(master, height=180, width=480, relief='solid')
        self.banner_frame.pack_propagate(False)
        self.banner_label = Label(self.banner_frame, text="Be Yourself", background="#000000", foreground="#ffffff", height=180, width=480)
        self.banner_label.config(font=('Impact', 64))

        # Place widgets
        self.banner_frame.pack()
        self.banner_label.pack()

    def change_banner_color(self):
        initial_color = self.banner_label['background']
        # The askcolor function will return a tuple containing the RGB and hex code for the chosen color; otherwise None
        new_color = colorchooser.askcolor(initial_color)
        if new_color is not None:
            self.banner_label.config(background=new_color[1])