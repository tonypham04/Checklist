from banner import Banner
from item import ChecklistItem
from content import Content

class App:
    
    def __init__(self, master):
        self.banner = Banner(master)
        self.content = Content(master)