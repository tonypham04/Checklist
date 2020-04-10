from tkinter import Tk
from tkinter import Menu
from tkinter import messagebox

class Banner:
    
    def __init__(self, master):
        # Remove dashes from the menubar drop down
        master.option_add('*tearOff', False)
        self.menubar = Menu(master)
        master.config(menu=self.menubar)
        
        file = Menu(self.menubar)

        file.add_command(label='Test', command=lambda: messagebox.showinfo(title='Test', message='This is a test.'))

        self.menubar.add_cascade(menu=file, label='File')

class Content:
    pass

class App:
    
    def __init__(self, master):
        self.banner = Banner(master)

def main():
    root = Tk()
    app = App(root)
    root.mainloop()

if __name__ == '__main__':
    main()