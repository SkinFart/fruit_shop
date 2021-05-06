#from tkinter import *
import tkinter as tk
import random
from test import fruit

class Program(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def window(self):
        a=("x")

    def create_widgets(self):
        self.hi_there = tk.Button(self)
        self.hi_there["text"] = "Hello World\n(click me)"
        self.hi_there["command"] = self.say_hi
        self.hi_there.pack(side="top")


        self.quit = tk.Button(self, text="QUIT", fg="red",
                              command=self.master.destroy)
        self.quit.pack(side="bottom")

        clicked = tk.StringVar()
        clicked.set("Jan")
        Opt = ["Jan","Feb", "Mar"]
        self.drop_down = tk.OptionMenu(self,clicked,*Opt)

        self.drop_down.pack()
    
    def say_hi(self):
        print("hi there, everyone!")
        for i in fruit:
	        print(fruit[i][FRUIT_NAME],fruit[i][FRUIT_COST])

FRUIT_NAME = "Name"
FRUIT_COST = "Price"
root = tk.Tk()
app = Program(master=root)
app.mainloop()