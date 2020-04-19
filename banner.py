from tkinter import Menu
from tkinter import messagebox
from tkinter import ttk
from tkinter import PhotoImage

class Banner:
    
    def __init__(self, master, image_path):
        # Create widgets
        self.banner_frame = ttk.Frame(master, height=180, width=480, relief='solid')
        self.banner_img = PhotoImage(file=image_path)
        self.banner_img_label = ttk.Label(self.banner_frame)
        self.banner_img_label.img = self.banner_img
        self.banner_img_label.config(image=self.banner_img_label.img)

        # Place widgets
        self.banner_img_label.pack()
        self.banner_frame.pack()

    # Remove current banner image and replace with another one
    def change_image(self, path=None):
        if path is not None:
            self.banner_img_label.forget()
            self.banner_img = PhotoImage(file=path)
            self.banner_img_label = ttk.Label(self.banner_frame)
            self.banner_img_label.img = self.banner_img
            self.banner_img_label.config(image=self.banner_img_label.img)
            self.banner_img_label.pack()