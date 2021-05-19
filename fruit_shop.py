#from tkinter import *
import tkinter as tk
from tkinter import ttk
import random
from test import fruit
from tkinter import messagebox
from PIL import ImageTk, Image  

class Program(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.grid()
        self.a = self.c()
        self.create_widgets()


    def create_widgets(self):

        n = tk.StringVar()
        self.abc = ttk.Combobox(self, width = 27, textvariable = n)
        self.abc["values"] = (self.a)
        self.abc.grid(column=5, row=1)
        self.abc.current(0)

        
        # self.hi_there = tk.Button(self)
        # self.hi_there["text"] = "Hello World\n(click me)"
        # self.hi_there["command"] = self.say_hi
        # self.hi_there.grid(column=5, row=2) 

        xd = tk.Button(self,width="5", text="+1", command=self.mt)
        xd.grid(column=5, row=2)

        self.quit = tk.Button(self, text="QUIT", fg="red",
                              command=self.master.destroy)
        self.quit.grid(column=5, row=3)


        acb = tk.Label(self, text="", width="80", height="20")
        acb.grid(column=5, row=4)

        xyz = ttk.Button(self, text="Get Value",command=self.check)
        xyz.grid(column=5, row=4)

    
    def check(self):
        a = self.abc.get()
        print(a)

    def mt(self):
        print(amount)
    
    def say_hi(self):
        print("hi there, everyone!")
        for i in fruit:
	        print(fruit[i][FRUIT_NAME],fruit[i][FRUIT_COST])

    def c(self):
        a = []
        for i in fruit:
            x = fruit[i][FRUIT_NAME]
            a.append(x)
        return(a)

        

FRUIT_NAME = "Name"
FRUIT_COST = "Price"
image1 = Image.open("temp.png")
amount = 0
root = tk.Tk()
app = Program(master=root)
app.mainloop()