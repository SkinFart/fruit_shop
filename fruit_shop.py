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
        self.amount=0
        #master.geometry("800x500")


    def create_widgets(self):
        
        # Create combo box for deals on product
        n = tk.StringVar()
        self.abc = ttk.Combobox(self, width = 27, textvariable = n)
        self.abc["values"] = (self.a)
        self.abc.grid(column=4, row=6)
        self.abc.current(0)

        

        self.shop = tk.Label(self,text="The Uce's Fruit Shop", borderwidth=2,relief="groove",bg="red")
        self.shop.config(font=("Arial", 30))
        self.shop.grid(row=0,column=2,rowspan=2,columnspan=3,padx=15,pady=15,ipady=15,ipadx=15)

        # Opens order window
        self.order_button = tk.Button(self, text="Order",command=self.openNewWindow )
        self.order_button.config(font=("Arial", 22))
        self.order_button.grid(row=4,column=3, columnspan=2)

        self.temp = tk.Button(self,text="temp")
        self.temp.config(font=("Arial", 22))
        self.temp.grid(row=4,column=3,columnspan=1)

        self.temp2 = tk.Button(self,text="temp2")
        self.temp2.config(font=("Arial", 22))
        #self.temp2.grid(row=4,column=5,columnspan=2)


        # Button that closes the program
        self.quit = tk.Button(self, text="QUIT", fg="red",
                              command=self.master.destroy)
        self.quit.grid(column=5, row=6,padx=5,pady=5,ipadx=5,ipady=5)

        # Test that checks whats in combobox 
        self.xyz = ttk.Button(self, text="Get Value",command=self.check)
        self.xyz.grid(column=3, row=8)

    
    def check(self):
        a = self.abc.get()
        print(a)
        return(a)

    def mt(self):
        print(amount)
    
    def buy(self,i):
        x = self.button_dict[i]['text']
        #print(x)
        cost=fruit2[i]
        cost=cost.split(" ")
        cost=cost[0].strip("$")
        self.amount=self.amount+float(cost)
        self.total['text']=f"Total: ${self.amount:.2f}"
        print(self.amount)

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
        images=['01.png', '02.png', '03.png', '04.png', '05.png', '06.png', '07.png', ]  #List of images
        images = iter(images)
            
        for i in images:  #For loop that creates the menu images
            menu_image = Image.open(i)  #Opens the image, resizes it, sets it to a format for tkinter
            menu_image = menu_image.resize((125,125), Image.ANTIALIAS)
            display_image = ImageTk.PhotoImage(menu_image)
            self.image_ref.append(display_image)  #Saves image refrence
            self.b = tk.Label(self.newWindow,image=display_image,borderwidth=2,relief="groove")  #Creats the image label
            self.b.grid(column=image_column,row=image_row)
            image_column+=1
            if image_column == 3:  #This decides how many images on each row
                image_column = 0
                image_row += 2

        self.button_dict = {}
        for i in self.a:
            a=(fruit2[i])
            self.button_dict[i] = tk.Button(self.newWindow, text=i+" "+a, width=25, command=lambda i=i: self.buy(i)) 
            self.b.grid(column=n,row=x)
            self.button_dict[i].grid(column=n, row=r)
            a=(fruit2[i])
            rrr+=1
            n+=1
            if n == 3:
                n = 0
                r += 2
                x += 2
        
        self.total = tk.Label(self.newWindow, text="Total Cost: "+str(self.amount))
        self.total.grid(row=9, column=3)

    def add_item(self,i):
        x = self.button_dict[i]['text']
        print(x)
        

FRUIT_NAME = "Name"
FRUIT_COST = "Price"
amount = 0
root = tk.Tk()
app = Program(master=root)
app.mainloop()