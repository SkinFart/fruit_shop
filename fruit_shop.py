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
        master.geometry("800x800")

    def create_widgets(self):
        
        # Create combo box for deals on product
        n = tk.StringVar()
        self.abc = ttk.Combobox(self, width = 27, textvariable = n)
        self.abc["values"] = (self.a)
        self.abc.grid(column=5, row=1)
        self.abc.current(0)

        # Create Image for item
        self.img = Image.open("vvv.png")
        self.img = self.img.resize((50,50), Image.ANTIALIAS)


        self.photo = ImageTk.PhotoImage(self.img)
        #self.label1 = tk.Label(self,image=self.photo)
        #self.label1.grid(row=6)
        
        # Image Button
        self.img_but = tk.Button(self, image=self.photo, command=self.openNewWindow)
        self.img_but.grid(row=3)

        # self.hi_there = tk.Button(self)
        # self.hi_there["text"] = "Hello World\n(click me)"
        # self.hi_there["command"] = self.say_hi
        # self.hi_there.grid(column=5, row=2) 

        # Amount
        xd = tk.Button(self,width="5", text="+1", command=self.mt)
        xd.grid(column=5, row=2)


        # Button that closes the program
        self.quit = tk.Button(self, text="QUIT", fg="red",
                              command=self.master.destroy)
        self.quit.grid(column=5, row=3)

        # Label
        acb = tk.Label(self, text="", width="80", height="20")
        acb.grid(column=5, row=4)

        # Test that checks whats in combobox 
        xyz = ttk.Button(self, text="Get Value",command=self.check)
        xyz.grid(column=5, row=4)

    
    def check(self):
        a = self.abc.get()
        print(a)
        return(a)

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

    def openNewWindow(self):
        
        self.newWindow = tk.Toplevel(root)

        self.newWindow.title("New Window")

        self.newWindow.geometry("800x800")

        a = tk.Button(self.newWindow, text='test', command=self.test)
        a.grid(row=1)

        img = Image.open("vvv.png")
        img = img.resize((400,400), Image.ANTIALIAS)
        self.fgh = ImageTk.PhotoImage(img)
        b = tk.Label(self.newWindow,image=self.fgh)
        b.grid(column=2,row=1)

    def add_item(self):
        x = self.button['text']
        print(x)

    def test(self):
        for i in self.a:
            self.button = tk.Button(self.newWindow, text=i, command=self.add_item)    #command=lambda x=i: func(x)
            self.button.grid()
        

FRUIT_NAME = "Name"
FRUIT_COST = "Price"
amount = 0
root = tk.Tk()
app = Program(master=root)
app.mainloop()