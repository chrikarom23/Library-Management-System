import datetime
from tkinter import *
from tkinter import ttk
import mysql.connector
from tkinter import messagebox

class remval:
    def __init__(self, master):
        self.master = master
        master.title("Loan")
        master.iconbitmap(r"""C:\Users\chrik\Documents\Mini_project_yr_2\Book.ico""")
        master.geometry("325x300")
        master.configure(background="#6883bc")
        self.conn = mysql.connector.connect(host="localhost", user="root", passwd="Romero23?", database="library")
        self.cur = self.conn.cursor()
        self.bid = IntVar()
        self.username = StringVar()
        self.Staff = StringVar()
        fr1 = LabelFrame(master, text="Loan-out Book", relief=RIDGE, font=("arial", 14), bg="#d9a5b3")

        #Label(fr1, text="Remove Book from Library", font=("verdana", 10), bg="gray").grid(row=0, column=1, sticky=N, padx=2, pady=3)

        Label(fr1, text="Book ID", font=('verdana', 10), bg="#8a307f", fg="white").grid(row=1, column=1, sticky=W, padx=5, pady=5)
        ent1 =Entry(fr1, font=("Arial", 12), textvariable=self.bid)
        ent1.grid(row=2, column=1, sticky=W, padx=5, pady=5)
        ent1.focus_set()
        Label(fr1, text="Username", font=('verdana', 10), bg="#8a307f", fg="white").grid(row=3, column=1, sticky=W, padx=5, pady=5)
        Entry(fr1, font=("Arial", 12), textvariable=self.username).grid(row=4, column=1, sticky=W, padx=5, pady=5)
        Label(fr1, text="Staff Username", font=('verdana', 10), bg="#8a307f", fg="white").grid(row=5, column=1, sticky=W, padx=5, pady=5)
        Entry(fr1, font=("Arial", 12), textvariable=self.Staff).grid(row=6, column=1, sticky=W, padx=5, pady=5)
        Button(fr1, text="Loan Out Book", font=('verdana', 10), command=self.rembooks, bg="#8a307f").grid(row=7, column=1, sticky=NSEW, padx=5, pady=5)
        fr1.pack(side=TOP, anchor=CENTER, padx=50, pady=10)

    def rembooks(self):
        try:
            self.cur.execute(f"select loaned from books where b_id = '{self.bid.get()}'")
            loaned = self.cur.fetchone()
            if not loaned[0].decode():
                self.cur.execute(f"select uid from usertb where username='{self.username.get()}'")
                stud = self.cur.fetchone()
                self.cur.execute(f"Select u_type from usertb where username='{self.Staff.get()}'")
                staff = self.cur.fetchone()
                curtime = datetime.datetime.today()
                #curtime = datetime.datetime.strptime(str(now), '%Y-%m-%d %H:%M:%S.%f')
                if staff[0] > 4:
                    self.cur.execute(f"insert into loan(b_id,uid,loanout,exreturn) values({self.bid.get()}, {stud[0]}, '{curtime}','{curtime + datetime.timedelta(days=14)}');")
                    self.cur.execute(f"update books set loaned = 1 where b_id = '{self.bid.get()}';")
                    messagebox.showinfo(title="Success", message="The loan out has been registered in the database")
                    self.conn.commit()
                    self.cur.close()
                    self.conn.close()
                    self.master.destroy()
                else:
                    messagebox.showwarning(title="Authorization Error", message="Staff level is too low to authorize loaning")
                    self.master.destroy()
            else:
                messagebox.showerror(title="Already out", message="This book is currently loaned out to someone else")
                self.master.destroy()
        except:
                messagebox.showerror(title="Database Error", message="An error occured while contacting the database")
