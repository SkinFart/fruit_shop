#from tkinter import *
import tkinter as tk
from tkinter import ttk
import random
from test import fruit
from tkinter import messagebox
from PIL import ImageTk, Image  

images=[]

class Program(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.grid()
        self.a = self.c()
        self.create_widgets()
        self.n=0
        master.geometry("600x400")

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
        #self.img_but = tk.Button(self, image=self.photo, command=self.openNewWindow)
        #self.img_but.grid(row=3)
        self.neww = tk.Button(self, text="newWin", command=self.openNewWindow)
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
        return(a)

    def openNewWindow(self):
        self.newWindow = tk.Toplevel(root)
        self.newWindow.title("New Window")
        self.newWindow.geometry("800x500")
        self.newWindow.resizable(0,0)

        images=['01.png', '02.png', '03.png', '04.png', '05.png', '06.png', '07.png', ]
        images = iter(images) #images = itertools.cycle(images)

        self.panel = tk.Label(self.newWindow)
        self.panel.grid()

        def next_img():
            try:
                img = next(images)  # get the next image from the iterator
            except StopIteration:
                return  # if there are no more images, do nothing

            # load the image and display it
            img = Image.open(img)
            img = img.resize((150,150),Image.ANTIALIAS)
            img = ImageTk.PhotoImage(img)
            self.panel.img = img  # keep a reference so it's not garbage collected
            self.panel['image'] = img
            self.alk = tk.Button(self.newWindow, image=img)
            self.alk.grid(column=0,row=0)

        self.btn = tk.Button(self.newWindow,text='Next image', command=next_img)
        self.btn.grid()
        #a = tk.Button(self.newWindow, text='test', command=self.test)
        #a.grid(row=1)

        r = 0
        h=0
        #img = Image.open("vvv.png")
        #img = img.resize((50,50), Image.ANTIALIAS)
        #self.fgh = ImageTk.PhotoImage(img)
        #b = tk.Label(self.newWindow,image=self.fgh)
        #b.grid(column=2,row=1,columnspan=3)
        self.button_dict = {}
        for i in self.a:
            #self.button_dict[i] = tk.Button(self.newWindow, text=i, command=lambda i=i: self.add_item(i))    #command=lambda x=i: func(x)
            #self.button_dict[i].grid(column=h, row=r)
            #h+=1
            if h == 3:
                h = 0
                r += 1
        

    def add_item(self,i):
        x = self.button_dict[i]['text']
        print(x)
        

FRUIT_NAME = "Name"
FRUIT_COST = "Price"
amount = 0
root = tk.Tk()
app = Program(master=root)
app.mainloop()