import tkinter as tk
from tkinter import ttk
import random
from test import fruit
from fruit2 import fruit2
from tkinter import messagebox
from PIL import Image, ImageTk 
from functools import partial


class Program(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.grid()
        self.a = self.c()
        self.create_widgets()
        self.n=0
        self.amount=0
        master.resizable(0,0)
        self.configure(background="azure")
        

    def create_widgets(self):

        # Create combo box for deals on product
        n = tk.StringVar()
        self.abc = ttk.Combobox(self, width = 27, textvariable = n)
        self.abc["values"] = (self.a)
        self.abc.grid(column=5, row=9)
        self.abc.current(0)


        # Image on main window
        self.main_image_ref=[]  # Image Ref list so it shows up
        shop_image = Image.open("joefruit2.jpg")  #Opens the image, resizes it, sets it to a format for tkinter
        shop_image = shop_image.resize((550,450), Image.ANTIALIAS)
        display_image = ImageTk.PhotoImage(shop_image)
        self.main_image_ref.append(display_image)  #Saves image refrence
        self.shop_bg = tk.Label(self,image=display_image,borderwidth=0)
        self.shop_bg.grid(column=1,row=8,columnspan=7)
        
        
        # Store title label
        self.shop = tk.Label(self,text="The Uce's Fruit Shop", borderwidth=2,relief="groove",bg="PaleVioletRed2", width=35)
        self.shop.config(font=("Arial", 30))
        self.shop.grid(row=0,column=2,rowspan=2,columnspan=7,padx=15,pady=15,ipady=15,ipadx=15)

        self.fff=tk.Label(self,text='',height=30)
        self.fff.grid(row=10)
        

        # Opens order window
        self.order_button = tk.Button(self, text="Order",command=self.openNewWindow,width=10)
        self.order_button.config(font=("Arial", 22),background="lavender")
        self.order_button.grid(row=4,column=4, columnspan=1)
        

        # View order button
        self.view_order = tk.Button(self,text="View Order",width=10)
        self.view_order.config(font=("Arial", 22),background="lavender")
        self.view_order.grid(row=4,column=5,columnspan=1)


        # Admin login button
        self.admin_user = tk.Button(self,text="Admin",command=self.admin_login,width=10)
        self.admin_user.config(font=("Arial", 22),background="lavender")
        self.admin_user.grid(row=4,column=6,columnspan=1)


        # Button that closes the program
        self.quit = tk.Button(self, text="QUIT", fg="red",
                              command=self.master.destroy)
        self.quit.config(font=("Arial", 18),background="lavender")
        self.quit.grid(column=7, row=9,padx=5,pady=5,ipadx=5,ipady=5, columnspan=2)

        # Test that checks whats in combobox 
        self.check_value = ttk.Button(self, text="Get Value",command=self.check)
        self.check_value.grid(column=4, row=9)

    
    def check(self):
        a = self.abc.get()
        if a == '':
            return
        else:
            self.exa=fruit2[a]
            self.exact_price = tk.Label(self,text=self.exa, width=15)  # Added a width to cover up old price rather than re grid 
            self.exact_price.config(font=("Arial", 16),background="azure")
            self.exact_price.grid(column=6,row=9)

    def mt(self):
        print(amount)
    
    def buy(self,i):
        x = self.button_dict[i]['text']
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

    def openNewWindow(self):  # Order screen
        self.newWindow = tk.Toplevel(root)
        self.newWindow.title("New Window")
        self.newWindow.geometry("850x700")
        self.newWindow.resizable(0,0)

        self.newWindow.grid_columnconfigure(1, weight=1)

        self.newWindow.grid_rowconfigure(1, weight=0)

        self.image_ref = []

        self.title_label = tk.Label(self.newWindow, text="Fruit For Sale",bg="OrangeRed2")
        self.title_label.config(font=("Arial", 22))
        self.title_label.grid(row=0, column=0, columnspan=3,rowspan=3)

        self.quit = tk.Button(self.newWindow, text="Back", fg="red",
                              command=self.newWindow.destroy)
        self.quit.config(font=("Arial", 16))
        self.quit.grid(column=4, row=9,padx=5,pady=5,ipadx=5,ipady=5)

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
            self.b.grid(column=image_column,row=image_row,padx=10,pady=10,ipadx=10,ipady=10)
            image_column+=1
            if image_column == 3:  #This decides how many images on each row
                image_column = 0
                image_row += 2

        self.button_dict = {}
        for i in self.a:
            a=(fruit2[i])
            self.button_dict[i] = tk.Button(self.newWindow, text=i+" "+a, width=25, command=lambda i=i: self.buy(i)) 
            self.b.grid(column=n,row=x,padx=10,pady=10,ipadx=10,ipady=10)
            self.button_dict[i].grid(column=n, row=r,padx=5,pady=5,ipadx=5,ipady=5)
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
        
    def admin_login(self):  # Admin login window
        self.admin = tk.Toplevel(root)
        self.admin.title("New Window")
        self.admin.resizable(0,0)

        self.title_label = tk.Label(self.admin,text="Admin Login",width=25,bg="teal")
        self.title_label.config(font=("Arial", 26))
        self.title_label.grid(ipadx=5,ipady=5,column=0,columnspan=5)

        password = tk.StringVar()
        username = tk.StringVar()

        self.user_label = tk.Label(self.admin,text="User Name: ")
        self.user_label.config(font=("Arial", 16))
        self.user_label.grid(padx=15,pady=10,column=1,columnspan=3)

        self.user_entry = tk.Entry(self.admin,text=username)
        self.user_entry.grid(padx=15,pady=10,column=1,columnspan=3)

        self.pass_label = tk.Label(self.admin,text="Password: ")
        self.pass_label.config(font=("Arial", 16))
        self.pass_label.grid(padx=15,pady=10,column=1,columnspan=3)

        self.user_pass = tk.Entry(self.admin,text=password)
        self.user_pass.grid(padx=15,pady=10,column=1,columnspan=3)

        validateLogin = partial(self.validateLogin, username, password)
        
        login_button=tk.Button(self.admin,text='login',command=validateLogin)
        login_button.grid(padx=15,pady=15,column=1,columnspan=3)
        
        self.quit = tk.Button(self.admin, text="Back", fg="red",
                              command=self.admin.destroy)
        self.quit.config(font=("Arial", 16))
        self.quit.grid(column=4,padx=5,pady=5,ipadx=5,ipady=5,columnspan=2)

    def validateLogin(self,username, password):
        print("username entered :", username.get())
        print("password entered :", password.get())
        return   

FRUIT_NAME = "Name"
FRUIT_COST = "Price"
amount = 0
root = tk.Tk()
app = Program(master=root)
app.mainloop()