import os
import sqlite3
from tkinter import *
from tkinter import messagebox


class Login_System:
    def __init__(self, root):
        self.root = root
        self.root.geometry('800x600+0+0')
        self.root.title('Login Page')
        self.root.config(bg='white')

        # =============Log in Frame
        login_frame = Frame(self.root, bd=4, relief=RIDGE, bg='lightgrey')
        login_frame.place(x=50, y=50, width=700, height=500)
        Label(login_frame, text='Login Page', font=('times new roman', 20, 'bold'), bg='#262626',
              fg='white').pack(side=TOP, fill=X)

        Label(login_frame, text='Username: ', font=('times new roman', 20), bg='lightgrey').place(x=150, y=100)
        self.username = StringVar()
        self.password = StringVar()
        Entry(login_frame, textvariable=self.username, font=('times new roman', 15)).place(x=300,
                                                                                           y=102,
                                                                                           width=170,
                                                                                           height=32)
        Label(login_frame, text='Password: ', font=('times new roman', 20), bg='lightgrey').place(x=150, y=150)
        Entry(login_frame, textvariable=self.password, show='*', font=('times new roman', 15)).place(x=300,
                                                                                                     y=152,
                                                                                                     width=170,
                                                                                                     height=32)
        Button(login_frame, text='Login', command=self.login, font=('times new roman', 15)).place(x=150, y=210,
                                                                                                  width=90, height=35)
        Button(login_frame, text='Reset', command=self.reset, font=('times new roman', 15)).place(x=250, y=210,
                                                                                                  width=90, height=35)
        Button(login_frame, text='Exit Window', command=self.exit, font=('times new roman', 15)).place(x=350, y=210,
                                                                                                       width=130,
                                                                                                       height=35)

        self.button_stock = Button(login_frame, text='Stock', state=DISABLED, command=self.stock,
                                   font=('times new roman', 15))
        self.button_stock.pack()
        self.button_stock.place(x=180,
                                y=310,
                                width=130,
                                height=35)
        self.button_sale = Button(login_frame, text='Sale', state=DISABLED, command=self.sale,
                                  font=('times new roman', 15))
        self.button_sale.pack()
        self.button_sale.place(x=330,
                               y=310,
                               width=130,
                               height=35)

    def login(self):
        con = sqlite3.connect(database=r'drugstore.db')
        cur = con.cursor()
        try:
            if self.username.get() == "":
                messagebox.showerror("Error", "Enter Username", parent=self.root)
                return
            elif self.password.get() == "":
                messagebox.showerror("Error", "Enter Password", parent=self.root)
                return
            else:
                cur.execute('select id, name from users where username = ? AND password = ?',
                            (self.username.get(), self.password.get()))
                user = cur.fetchone()
                if user is None:
                    messagebox.showerror("Error", "Invalid USERNAME/PASSWORD", parent=self.root)
                else:
                    messagebox.showinfo("Information", "Login Successfully", parent=self.root)
                    # self.root.destroy()
                    self.button_stock["state"] = "normal"
                    self.button_sale["state"] = "normal"


        except Exception as ex:
            messagebox.showerror("Error", f"Error due to : str{ex}", parent=self.root)

    def reset(self):
        print('reset')
        self.username.set('')
        self.password.set('')

    def exit(self):
        print('exit')
        self.root.destroy()

    def stock(self):
        print('stock')

    def sale(self):
        print('sale')


root = Tk()
obj = Login_System(root)
root.mainloop()
