from tkinter import Menu
from tkinter import messagebox
from tkinter import ttk
from tkinter import PhotoImage

# REFERENCES SECTION
# Creating a right-click menu with tkinter: https://stackoverflow.com/questions/12014210/tkinter-app-adding-a-right-click-context-menu

class Banner:
    
    def __init__(self, master, image_path=None):
        default_image_path = 'images/gimp_themes/maple_leaves.png'
        if image_path is not None:
            default_image_path = image_path
        
        # Create widgets
        self.banner_frame = ttk.Frame(master, height=180, width=480, relief='solid')
        self.banner_img = PhotoImage(file=default_image_path)
        self.banner_img_label = ttk.Label(self.banner_frame)
        self.banner_img_label.img = self.banner_img
        self.banner_img_label.config(image=self.banner_img_label.img)

        # Bind functions to widgets
        self.banner_img_label.bind('<Button-3>', lambda e: self.rc_change_image(self.banner_frame, e))

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
            self.banner_img_label.bind('<Button-3>', lambda e: self.rc_change_image(self.banner_frame, e))
            self.banner_img_label.pack()

    # Change the banner image from a menu on right-click
    # NOTE: .jpg not working, convert to .png
    def rc_change_image(self, master, event):
        right_click_menu = Menu(master)
        picsum_images = Menu(right_click_menu)
        picsum_images.add_command(label='Pineapple', command=lambda: self.change_image('images/picsum/pineapple_824.png'))
        picsum_images.add_command(label='Jellyfish', command=lambda: self.change_image('images/picsum/jellyfish_881.png'))
        picsum_images.add_command(label='Rasberries', command=lambda: self.change_image('images/picsum/rasberries_102.png'))
        right_click_menu.add_cascade(menu=picsum_images, label='Picsum')
        right_click_menu.tk_popup(event.x_root, event.y_root, 0)