from tkinter import Tk
from tkinter import Menu
from tkinter import messagebox
from tkinter import ttk
from tkinter import StringVar
from tkinter import Button
from tkinter import Toplevel
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

class ChecklistItem:

    def __init__(self, master, task):
        self.task = task
        # Allows the Checkbutton value to be dynamic
        self.value = StringVar()
        self.value.set("Imcomplete")
        self.item = ttk.Checkbutton(master, text=self.task)
        self.item.config(variable=self.value, onvalue="Complete", offvalue="Imcomplete")

class Content:
    
    def __init__(self, master, checklist=None):
        # Constants
        frame_width = 480
        checklist_frame_height = 480
        button_frame_height = checklist_frame_height/8

        # Create widgets
        self.checklist_frame = ttk.Frame(master, height=checklist_frame_height, width=frame_width, relief='solid')
        self.button_frame = ttk.Frame(master, height=button_frame_height, width=frame_width, relief='solid')
        if checklist is None:
            self.checklist = []
        else:
            self.checklist = checklist

        for task in self.checklist:
            task.config(command=self.update_state)

        self.add_button = Button(self.button_frame, text="\u271a Add Task", command=self.add_task)

        # Configure widgets
        self.checklist_frame.pack_propagate(False)
        self.button_frame.pack_propagate(False)

        # Place widgets
        self.add_button.pack(pady=15)
        self.checklist_frame.pack()
        self.button_frame.pack()

    def display_tasks(self):
        for task in self.checklist:
            task.item.pack(anchor='w', pady=5, padx=5)

    def add_task(self):
        # Create widgets
        add_window = Toplevel(self.button_frame, height=120, width=480)
        # Prevent window resizing along x and y
        add_window.resizable(False, False)
        add_frame = ttk.Frame(add_window)
        add_label = ttk.Label(add_frame, text="Task Name: ")
        add_entry = ttk.Entry(add_frame, width=48)
        add_entry.bind('<Return>', lambda e: self.submit(add_entry.get(), add_window))
        submit_button = Button(add_frame, text="Submit", command=lambda: self.submit(add_entry.get(), add_window))
        cancel_button = Button(add_frame, text="Cancel", command=lambda: self.cancel(add_window))

        # Place widgets
        add_label.pack(side='left')
        add_entry.pack(side='left')
        submit_button.pack(side='left')
        cancel_button.pack(side='left')
        add_frame.pack()

    def cancel(self, master):
        master.destroy()

    def submit(self, task, master):
        if task != "":
            new_task = ChecklistItem(self.checklist_frame, task)
            new_task.item.config(command=self.update_state)
            self.checklist.append(new_task)
            self.cancel(master)
            self.display_tasks()
        else:
            messagebox.showerror(title="Invalid entry", message="A task cannot be blank.")

    def update_state(self):
        for task in self.checklist:
            if task.value.get() == "Complete":
                self.checklist.remove(task)
                task.item.destroy()
        self.display_tasks()

class App:
    
    def __init__(self, master):
        self.banner = Banner(master)
        self.content = Content(master)

def main():
    root = Tk()
    app = App(root)
    root.mainloop()

if __name__ == '__main__':
    main()