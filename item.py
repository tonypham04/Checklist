from tkinter import StringVar
from tkinter import Checkbutton

class ChecklistItem:

    def __init__(self, master, task):
        self.task = task
        # Allows the Checkbutton value to be dynamic
        self.value = StringVar()
        self.value.set("Imcomplete")
        self.item = Checkbutton(master, text=self.task, fg="#ffffff", bg="#006994")
        self.item.config(variable=self.value, onvalue="Complete", offvalue="Imcomplete")