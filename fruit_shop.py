#from tkinter import *
import tkinter as tk
from tkinter import ttk
import random
from test import fruit
from fruit2 import fruit2
from tkinter import messagebox
from PIL import Image, ImageTk 

class Program(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.grid()
        self.a = self.c()
        self.create_widgets()
        self.n=0
        master.geometry("800x500")

    def create_widgets(self):
        
        # Create combo box for deals on product
        n = tk.StringVar()
        self.abc = ttk.Combobox(self, width = 27, textvariable = n)
        self.abc["values"] = (self.a)
        self.abc.grid(column=5, row=1)
        self.abc.current(0)

        # Create Image for item
        #self.img = Image.open("vvv.png")
        #self.img = self.img.resize((50,50), Image.ANTIALIAS)


        #self.photo = ImageTk.PhotoImage(self.img)
        
        # Image Button
        self.neww = tk.Button(self, text='newWin', command=self.openNewWindow)
        self.neww.grid(row=3)

        # Amount
        xd = tk.Button(self,width="5", text="+1", command=self.mt)
        xd.grid(column=5, row=2)


        # Button that closes the program
        self.quit = tk.Button(self, text="QUIT", fg="red",
                              command=self.master.destroy)
        self.quit.grid(column=5, row=3)

        # Test that checks whats in combobox 
        xyz = ttk.Button(self, text="Get Value",command=self.check)
        xyz.grid(column=5, row=4)

    
    def check(self):
        a = self.abc.get()
        print(a)
        return(a)

    def mt(self):
        print(amount)
    
    def c(self):
        a = []
        for i in fruit:
            x = fruit[i][FRUIT_NAME]
            a.append(x)
        print(a)
        return(a)

    def openNewWindow(self):
        self.newWindow = tk.Toplevel(root)
        self.newWindow.title("New Window")
        self.newWindow.geometry("800x500")
        self.newWindow.resizable(0,0)

        self.newWindow.grid_columnconfigure(1, weight=1)

        self.newWindow.grid_rowconfigure(1, weight=0)

        self.image_ref = []

        r = 1
        image_column=0
        image_row=0
        n=0
        rrr=0
        x=0
        v=0  #for price in loop
        images=['01.png', '02.png', '03.png', '04.png', '05.png', '06.png', '07.png', ]
        images = iter(images)
            
        for i in images:  #For loop that creates the menu images
            menu_image = Image.open(i)  #Opens the image, resizes it, sets it to a format for tkinter
            menu_image = menu_image.resize((100,100), Image.ANTIALIAS)
            display_image = ImageTk.PhotoImage(menu_image)
            self.image_ref.append(display_image)  #Saves image refrence
            self.b = tk.Label(self.newWindow,image=display_image)  #Creats the image label
            self.b.grid(column=image_column,row=image_row)
            image_column+=1
            if image_column == 3:  #This decides how many images on each row
                image_column = 0
                image_row += 2

        self.button_dict = {}
        for i in self.a:
            a=(fruit2["fruit"+str(rrr)][i])
            self.button_dict[i] = tk.Button(self.newWindow, text=i+" "+a, width=25, command=lambda i=i: self.add_item(i))    #command=lambda x=i: func(x)
            self.b.grid(column=n,row=x)
            self.button_dict[i].grid(column=n, row=r)
            a=(fruit2["fruit"+str(rrr)][i])
            rrr+=1
            n+=1
            if n == 3:
                n = 0
                r += 2
                x += 2
        

    def add_item(self,i):
        x = self.button_dict[i]['text']
        print(x)
        

FRUIT_NAME = "Name"
FRUIT_COST = "Price"
amount = 0
root = tk.Tk()
app = Program(master=root)
app.mainloop()