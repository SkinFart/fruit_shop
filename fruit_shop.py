import tkinter as tk  # tkinter gui import
from tkinter import ttk  # Import specific part of tkinter as its not in the main import
from fruit import fruit  # Imports the first dictionary 
from fruit2 import fruit2  # Imports the second menu dictionary (dictionary is split like this as its easier to use and better for longevity)
from PIL import Image, ImageTk  # Import for use of images in tkinter
from functools import partial  # Import for validation


class Program(tk.Frame):
    def __init__(self, master=None):  # Initialize class attributes
        super().__init__(master)
        self.master = master  
        self.grid()
        self.a = self.c()
        self.create_widgets()
        self.order_names={}
        self.amount=0  # Amount value that can be uses in all windows
        master.resizable(0,0)  # Stops resize of window with mouse
        self.configure(background="azure")  #Background colour
        

    def create_widgets(self):  # Creates all the widgits

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
        

        # Opens order window
        self.order_button = tk.Button(self, text="Order",command=self.openNewWindow,width=10)
        self.order_button.config(font=("Arial", 22),background="lavender")
        self.order_button.grid(row=4,column=4, columnspan=1)
        

        # View order button
        self.view_order = tk.Button(self,text="View Order",width=10,command=self.order_view)
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
        self.check_value = tk.Button(self, text="Get Value",command=self.check)
        self.check_value.config(font=("Arial", 16),background="lavender")
        self.check_value.grid(column=4, row=9)

    def order_view(self):  # Order view window
        self.view = tk.Toplevel(root)
        self.view.title("Order View")
        self.view.resizable(0,0)
        self.view.configure(background="azure")


        # Title label
        self.title_label = tk.Label(self.view,text="Order",bg="PaleVioletRed2",borderwidth=2,relief="groove")
        self.title_label.config(font=("Arial", 26))
        self.title_label.grid(ipadx=5,ipady=5,padx=5,pady=5,column=0,columnspan=8,sticky="NSEW")


        # Button that goes back to main window
        self.quit = tk.Button(self.view, text="Back", fg="red",
                              command=self.view.destroy)
        self.quit.config(font=("Arial", 14),background="lavender")
        self.quit.grid(column=6, row=9,padx=5,pady=5,ipadx=5,ipady=5, columnspan=2)


        # Button that cancels order
        self.quit = tk.Button(self.view, text="Cancel Order", fg="red",
                              command=self.master.destroy,width=15)
        self.quit.config(font=("Arial", 14),background="lavender")
        self.quit.grid(column=4, row=9,padx=5,pady=5,ipadx=5,ipady=5, columnspan=2)

        # Order Displayed
        c=0
        r=2
        for i in self.order_names:  # Makes labels of current order and displays them
            a=self.order_names[i]
            self.order_display = tk.Label(self.view,text="Item: "+i+" Quantity: "+str(a), anchor='w')
            self.order_display.config(font=("Arial", 18),background="azure")
            self.order_display.grid(column=c, row=r,columnspan=2)
            r+=1

        # Shows total cost
        self.total = tk.Label(self.view, text="Total Cost: "+str(self.amount))
        self.total.config(font=("Arial", 18),background="azure")
        self.total.grid(row=3, column=4)


        # Confirm button, closes everything
        self.order_conf = tk.Button(self.view, text="Confirm", fg='red', command=self.confirm_order,width=15)
        self.order_conf.configure(background="lavender",font=("Arial",14))
        self.order_conf.grid(column=4,row=8,columnspan=2,padx=5,pady=5,ipadx=5,ipady=5)
        
    def confirm_order(self):  # Confirm order window
        self.conf = tk.Toplevel(root)
        self.conf.title("Order Confirm")
        self.conf.resizable(0,0)
        self.conf.configure(background="azure")

        # Sting variable set for each entry
        n = tk.StringVar()
        p = tk.StringVar()
        a = tk.StringVar()
        e = tk.StringVar()
        pay = tk.StringVar()


        # Title label
        self.order_label = tk.Label(self.conf, text="Order Confirmed",borderwidth=2,relief="groove",bg="PaleVioletRed2")
        self.order_label.configure(font=("Arial",24))
        self.order_label.grid(row=0,column=0,columnspan=5,padx=5,pady=5,ipadx=5,ipady=5,sticky="NSEW")


        #  Name Entry
        self.name_input = tk.Entry(self.conf, text=n,width=27)
        self.name = tk.Label(self.conf, text="Name: ")
        self.name.configure(background="azure",font=("Arial",16))
        self.name.grid(row=1,column=2)
        self.name_input.grid(row=1,column=3)


        #  Phone Entry
        self.phone_input = tk.Entry(self.conf, text=p,width=27)
        self.phone = tk.Label(self.conf, text="Phone: ")
        self.phone.configure(background="azure",font=("Arial",16))
        self.phone.grid(row=2,column=2)
        self.phone_input.grid(row=2,column=3)


        #  Email Entry
        self.email_input = tk.Entry(self.conf, text=e,width=27)
        self.email = tk.Label(self.conf, text="Email: ")
        self.email.configure(background="azure",font=("Arial",16))
        self.email.grid(row=3,column=2)
        self.email_input.grid(row=3,column=3)


        #  Address Entry
        self.add_input = tk.Entry(self.conf, text=a,width=27)
        self.add = tk.Label(self.conf, text="Address: ")
        self.add.configure(background="azure",font=("Arial",16))
        self.add.grid(row=4,column=2)
        self.add_input.grid(row=4,column=3)

        #  Payment Entry
        self.pay_input = tk.Entry(self.conf, text=pay,width=27)
        self.pay = tk.Label(self.conf, text="Card Number: ")
        self.pay.configure(background="azure",font=("Arial",16))
        self.pay.grid(row=5,column=2)
        self.pay_input.grid(row=5,column=3)
        

        #  Location Info
        self.pickup = tk.Label(self.conf, text = "Pickup from 16 Joemongus Place from between 8am - 8pm")
        self.pickup.configure(background="azure",font=("Arial",18))
        self.pickup.grid(row=9,column=3)

        self.close = tk.Button(self.conf,text="Confirm",fg="red",
                              command=self.master.destroy)
        self.close.configure(background="lavender",font=("Arial",18))
        self.close.grid(row=8,column=4,padx=5)


    def check(self):  # Checks whats in the entry box
        a = self.abc.get()
        if a == '':
            return
        else:
            self.exa=fruit2[a]
            self.exact_price = tk.Label(self,text=self.exa, width=15)  # Added a width to cover up old price rather than re grid 
            self.exact_price.config(font=("Arial", 16),background="azure")
            self.exact_price.grid(column=6,row=9)


    def buy(self,i):  # Buys item, adds to list and calulates cost
        if i in self.order_names:  # Addes item to order list
            self.order_names[i] += 1
        else:
            self.order_names[i] = 1
        cost=fruit2[i]
        cost=cost.split(" ")
        cost=cost[0].strip("$")
        self.amount=self.amount+float(cost)
        self.total['text']=f"Total: ${self.amount:.2f}"

    def c(self):  # Item list creation
        a = []
        for i in fruit:
            x = fruit[i][FRUIT_NAME]
            a.append(x)
        return(a)

    def openNewWindow(self):  # Order screen
        self.newWindow = tk.Toplevel(root)
        self.newWindow.title("Order")
        self.newWindow.resizable(0,0)
        self.newWindow.configure(background="azure")
        self.image_ref = []


        # Button that closes the window
        self.quit = tk.Button(self.newWindow, text="Back", fg="red",
                              command=self.newWindow.destroy)
        self.quit.config(font=("Arial", 16),background="lavender")
        self.quit.grid(column=3, row=9,padx=5,pady=5,ipadx=5,ipady=5)


        # Position variables for layout 
        r = 1
        image_column=0
        image_row=0
        n=0
        x=0
        images=['01.png', '02.png', '03.png', '04.png', '05.png', '06.png', '07.png', ]  #List of images
        images = iter(images)


        # Creates the images and the button labels for them    
        for i in images:  #For loop that creates the menu images
            menu_image = Image.open(i)  #Opens the image, resizes it, sets it to a format for tkinter
            menu_image = menu_image.resize((150,150), Image.ANTIALIAS)
            display_image = ImageTk.PhotoImage(menu_image)
            self.image_ref.append(display_image)  #Saves image refrence
            self.b = tk.Label(self.newWindow,image=display_image,borderwidth=2,relief="groove")  #Creats the image label
            self.b.grid(column=image_column,row=image_row,padx=10,pady=10,ipadx=10,ipady=10)
            image_column+=1
            if image_column == 3:  #This decides how many images on each row
                image_column = 0
                image_row += 2

        self.button_dict = {}  #  Store the buttons so that they have uniquie identify
        for i in self.a:
            a=(fruit2[i])
            self.button_dict[i] = tk.Button(self.newWindow, text=i+" "+a, width=25, command=lambda i=i: self.buy(i))
            self.button_dict[i].config(font=("Arial", 14),background="lavender") 
            self.b.grid(column=n,row=x,padx=10,pady=10,ipadx=10,ipady=10)
            self.button_dict[i].grid(column=n, row=r,padx=5,pady=5,ipadx=5,ipady=5)
            a=(fruit2[i])
            n+=1
            if n == 3:  # Layout for images, 3 accross then continue that pattern down
                n = 0
                r += 2
                x += 2
        
        # Shows total cost
        self.total = tk.Label(self.newWindow, text="Total Cost: "+str(self.amount))
        self.total.config(font=("Arial", 16),background="azure") 
        self.total.grid(row=9, column=2)
        
    def admin_login(self):  # Admin login window
        self.admin = tk.Toplevel(root)
        self.admin.title("New Window")
        self.admin.resizable(0,0)
        self.admin.configure(background="azure")

        # Title Label
        self.title_label = tk.Label(self.admin,text="Admin Login",width=25,bg="teal")
        self.title_label.config(font=("Arial", 26))
        self.title_label.grid(ipadx=5,ipady=5,column=0,columnspan=5,padx=5,pady=5)


        # Variable Set
        password = tk.StringVar()
        username = tk.StringVar()


        # User name
        self.user_label = tk.Label(self.admin,text="User Name: ")
        self.user_label.config(font=("Arial", 16),background="azure")
        self.user_label.grid(padx=15,pady=10,column=1,columnspan=3)

        self.user_entry = tk.Entry(self.admin,text=username)
        self.user_entry.grid(padx=15,pady=10,column=1,columnspan=3)


        # Password
        self.pass_label = tk.Label(self.admin,text="Password: ")
        self.pass_label.config(font=("Arial", 16),background="azure")
        self.pass_label.grid(padx=15,pady=10,column=1,columnspan=3)

        self.user_pass = tk.Entry(self.admin,text=password)
        self.user_pass.grid(padx=15,pady=10,column=1,columnspan=3)


        #validate call
        validateLogin = partial(self.validateLogin, username, password)
        

        # Button that uses the validate
        login_button=tk.Button(self.admin,text='login',command=validateLogin)
        login_button.config(font=("Arial", 16),background="lavender")
        login_button.grid(padx=15,pady=15,column=1,columnspan=3)
        

        # Go back 
        self.quit = tk.Button(self.admin, text="Back", fg="red",
                              command=self.admin.destroy)
        self.quit.config(font=("Arial", 16),background="lavender")
        self.quit.grid(column=4,padx=5,pady=5,ipadx=5,ipady=5,columnspan=2)


    # Validate for admin login
    def validateLogin(self,username, password):
        print("username entered :", username.get())
        print("password entered :", password.get())
        return   

# Some constants for dictionary use
FRUIT_NAME = "Name"
FRUIT_COST = "Price"
amount = 0  # Global amount
root = tk.Tk()
app = Program(master=root)
app.mainloop()  # Starts program 