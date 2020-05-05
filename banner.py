from tkinter import Menu
from tkinter import messagebox
from tkinter import ttk
from tkinter import Label
from tkinter import colorchooser
import configparser

# REFERENCES SECTION
# Creating a right-click menu with tkinter: https://stackoverflow.com/questions/12014210/tkinter-app-adding-a-right-click-context-menu

class Banner:

    # Constants for the Banner class from the config file
    config = configparser.ConfigParser()
    config.read('configs/config.ini')

    def __init__(self, master):
        # Banner widget attributes
        banner_width = Banner.config['BANNER'].getint('banner_width')
        banner_height = Banner.config['BANNER'].getint('banner_height')
        banner_text = Banner.config['BANNER']['banner_text']
        banner_background_color = Banner.config['BANNER']['banner_background_color']
        banner_text_color = Banner.config['BANNER']['banner_text_color']
        banner_font = Banner.config['BANNER']['banner_font']
        banner_font_size = Banner.config['BANNER'].getint('banner_font_size')

        # Create widgets
        self.banner_frame = ttk.Frame(master, width=banner_width, height=banner_height, relief='solid')
        self.banner_frame.pack_propagate(False)
        self.banner_label = Label(self.banner_frame, text=banner_text, background=banner_background_color, foreground=banner_text_color, width=banner_width, height=banner_height)
        self.banner_label.config(font=(banner_font, banner_font_size))

        # Place widgets
        self.banner_frame.pack()
        self.banner_label.pack()

    def change_banner_color(self):
        initial_color = self.banner_label['background']
        # The askcolor function will return a tuple containing the RGB and hex code for the chosen color; otherwise None
        new_color = colorchooser.askcolor(initial_color)
        if new_color is not None:
            self.banner_label.config(background=new_color[1])