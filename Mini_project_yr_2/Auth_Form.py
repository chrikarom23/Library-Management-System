from tkinter import *
from tkinter import messagebox
import logging
from PIL import ImageTk

from Info_page import Libdataview
from Lowlvl import Libdataviewlow
import mysql.connector

#root = Tk()
#root.configure(background="black")
#root.title("Library Management System")
#root.iconbitmap(r"""C:\Users\chrik\Documents\Mini_project_yr_2\Book.ico""")
#root.geometry("350x250")


class Auth:
    def __init__(self, root):
        try:
            self.conn = mysql.connector.connect(host="localhost", user="root", passwd="Romero23?", database="library")
            self.cur = self.conn.cursor()
            print("Trying to connect to database...")
        except:
            print("Not connected to db")
        print("Connected to database library")
        root.configure(background="#6883bc")
        root.title("Library Management System")
        root.iconbitmap(r"""C:\Users\chrik\Documents\Mini_project_yr_2\Book.ico""")
        root.geometry("320x200")
        self.root = root
        self.username = StringVar()
        self.password = StringVar()
        Label(root, text="Login Form", bg="#79a7d3", font=("arial", 12), relief=RIDGE).pack(side=TOP,padx=10, pady=10)
        self.Fr1 = Frame(self.root, bg='#79a7d3',borderwidth=1, relief=RAISED)
        self.en1 = Entry(self.Fr1, font=("Arial", 12), textvariable=self.username)

    def get_info(self):
        Label(self.Fr1, text="Enter username", bg="#8a307f", fg="white").grid(row=0, column=1, padx=3, pady=3)#pack(padx=2, pady=2)
        self.en1.grid(row=1, column=1, padx=3, pady=3)#.pack(padx=2, pady=2)
        self.en1.focus()
        Label(self.Fr1, text="Enter Password", bg="#8a307f", fg="white").grid(row=2, column=1, padx=3, pady=3)#.pack(padx=2, pady=2)
        Entry(self.Fr1, show="*", textvariable=self.password).grid(row=3, column=1, padx=3, pady=3, sticky=NSEW)#.pack(padx=2, pady=2)
        Button(self.Fr1, text="Submit", command=self.authorize, bg="#8a307f", fg="white").grid(row=4, column=1, padx=3, pady=3)#.pack(padx=2, pady=2)
        self.Fr1.pack(padx=20, pady=5, side=TOP)

    def authorize(self):
        try:
            self.cur.execute(f"select * from usertb where username = '{self.username.get()}'")
            pwd = self.cur.fetchone()
        except:
            messagebox.showerror(title="Input Error", message="The user doesn't exists")
        else:
            if self.username.get() and self.password.get():
                try:
                    if pwd[3] == self.password.get():
                        messagebox.showinfo(title="Login Info",  message=f"Welcome, {self.username.get()}.")
                        self.root.destroy()
                        self.cur.close()
                        self.conn.close()
                        print("closing connection in authentication form...")
                        if (pwd[1] >=0 and pwd[1] <5):
                            new = Tk()
                            N = Libdataviewlow(new)
                            new.mainloop()
                        else:
                            new = Tk()
                            N = Libdataview(new)
                            new.mainloop()
                    else:
                        messagebox.showerror(title="Invalid Entry", message="The username and password do not match")
                except:
                    messagebox.showerror(title="Invalid Entry", message="Please enter a valid username and password")
            else:
                messagebox.showwarning(title="Invalid Entry", message="Please enter username and password")
        #finally:
        #    self.cur.close()
        #    self.conn.close()

    #def __del__(self):
    #    self.cur.close()
    #    self.conn.close()
    #    print("closing connection in authentication form...")


#M = Auth(root)
#M.get_info()
#root.mainloop()
