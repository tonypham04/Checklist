from tkinter import ttk
from tkinter import Button
from tkinter import Toplevel
from tkinter import messagebox
from item import ChecklistItem

# REFERENCES
# Control the placement of a TopLevel Window: 'Creating additional top-level windows' from 'Python GUI Development with Tkinter' course on LinkedIn Learning with Barron Stone [5:27]
# Fix issue where winfo_width() and winfo_height() always return 1: https://stackoverflow.com/questions/34373533/winfo-width-returns-1-even-after-using-pack
# Remove the newline character from a string https://stackoverflow.com/questions/9347419/python-strip-with-n

class Content:
    
    def __init__(self, master, checklist=None):
        # Constants
        frame_width = 480
        checklist_frame_height = 480
        button_frame_height = checklist_frame_height/8
        task_list_file_path = 'to_do_list.txt'

        # Create widgets
        self.checklist_frame = ttk.Frame(master, height=checklist_frame_height, width=frame_width, relief='solid')
        self.button_frame = ttk.Frame(master, height=button_frame_height, width=frame_width, relief='solid')
        if checklist is None:
            self.checklist = []
            # Try to open the text file containing the list of to do items
            # If no such file exist, make one
            try:
                list_file_handler = open(task_list_file_path, 'r')
                if list_file_handler.readable():
                    to_do_list = list_file_handler.readlines()
                    for item in to_do_list:
                        item = item.strip('\n')
                        self.checklist.append(ChecklistItem(self.checklist_frame, item))
            except FileNotFoundError:
                list_file_handler = open(task_list_file_path, 'w')
            list_file_handler.close()
        else:
            self.checklist = checklist

        for task in self.checklist:
            task.item.config(command=self.update_state)

        self.add_button = Button(self.button_frame, text="\u271a Add Task", command=self.add_task)

        # Configure widgets
        self.checklist_frame.pack_propagate(False)
        self.button_frame.pack_propagate(False)

        # Place widgets
        self.add_button.pack(pady=15)
        self.checklist_frame.pack()
        self.button_frame.pack()
        self.display_tasks()

    def display_tasks(self):
        for task in self.checklist:
            task.item.pack(anchor='w', pady=5, padx=5)

    def add_task(self):
        # Create and configure the window for adding tasks
        add_window = Toplevel(self.checklist_frame, width=480, height=40)
        add_window.title('Add Task')
        # Prevent window resizing along x and y
        add_window.resizable(False, False)
        # Offset is by default relative to the screen; need offset relative to the parent widget
        offset_x = self.checklist_frame.winfo_rootx() - 8
        offset_y = self.checklist_frame.winfo_rooty() + int(self.checklist_frame.winfo_height()/3)
        # Call to update_idletasks() required to fix issue where winfo_width() and winfo_height() always return 1
        add_window.update_idletasks()
        # Make the window to add tasks appear on top and around the middle of the checklist frame
        add_window.geometry("{}x{}+{}+{}".format(add_window.winfo_width(), add_window.winfo_height(), offset_x, offset_y))

        # Create widgets for window to add tasks
        add_frame = ttk.Frame(add_window)
        add_label = ttk.Label(add_frame, text="Task Name: ")
        add_entry = ttk.Entry(add_frame, width=48)
        add_entry.bind('<Return>', lambda e: self.submit(add_entry.get(), add_window))
        submit_button = Button(add_frame, text="Submit", command=lambda: self.submit(add_entry.get(), add_window))
        cancel_button = Button(add_frame, text="Cancel", command=lambda: self.cancel(add_window))

        # Place widgets
        add_label.pack(side='left', pady=10)
        add_entry.pack(side='left', pady=10)
        submit_button.pack(side='left', padx=5)
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