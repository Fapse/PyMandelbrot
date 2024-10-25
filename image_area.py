import tkinter as tk


class ImageArea(tk.Frame):
    def __init__(self, parent):
        super().__init__(width=512, height=512)
        self._parent = parent
        self.pack(side=tk.LEFT, expand=False)
