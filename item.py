from tkinter import StringVar
from tkinter import ttk

class ChecklistItem:

    def __init__(self, master, task):
        self.task = task
        # Allows the Checkbutton value to be dynamic
        self.value = StringVar()
        self.value.set("Imcomplete")
        self.item = ttk.Checkbutton(master, text=self.task)
        self.item.config(variable=self.value, onvalue="Complete", offvalue="Imcomplete")