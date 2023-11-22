from tkinter import *
from tkinter import ttk
import mysql.connector
import datetime
from tkinter import messagebox

open = None

class ret:
        def __init__(self, master):
                self.master = master
                master.title("Loan")
                master.iconbitmap(r"""C:\Users\chrik\Documents\Mini_project_yr_2\Book.ico""")
                master.geometry("400x400")
                master.configure(background="#6883bc")
                self.conn = mysql.connector.connect(host="localhost", user="root", passwd="Romero23?", database="library")
                self.cur = self.conn.cursor()
                self.bid = IntVar()
                self.uid = IntVar()
                self.sid = IntVar()
                self.condi = IntVar()
                frm = LabelFrame(master, text="Book return", relief=RIDGE, font=("arial", 14), bg="#d9a5b3")
                fr1 = Frame(frm, bg="#79a7d3")
                fr2 = Frame(frm, bg="#79a7d3")
                #Label(fr1, text="Return book", font=("verdana", 10), bg="gray").grid(row=0, column=1, sticky=N, padx=2, pady=3)

                Label(fr1, text="Book ID", font=('verdana', 10), bg="#8a307f", fg="white").grid(row=1, column=1, sticky=W, padx=5, pady=5)
                ent = Entry(fr1, font=("Arial", 12), textvariable=self.bid)
                ent.grid(row=2, column=1, sticky=W, padx=5, pady=5)
                ent.focus_set()
                Label(fr1, text="UID of Lendee", font=('verdana', 10), bg="#8a307f", fg="white").grid(row=3, column=1, sticky=W, padx=5, pady=5)
                Entry(fr1, font=("Arial", 12), textvariable=self.uid).grid(row=4, column=1, sticky=W, padx=5, pady=5)
                Label(fr1, text="Staff UID", font=('verdana', 10), bg="#8a307f", fg="white").grid(row=5, column=1, sticky=W, padx=5, pady=5)
                Entry(fr1, font=("Arial", 12), textvariable=self.sid).grid(row=6, column=1, sticky=W, padx=5, pady=5)
                Label(fr1, text="Condition", font=('verdana', 10), bg="#8a307f", fg="white").grid(row=7, column=1, sticky=W, padx=5, pady=5)
                Entry(fr1, font=("Arial", 12), textvariable=self.condi).grid(row=8, column=1, sticky=W, padx=5, pady=5)
                Label(fr2, text="(Scaling from 1 to 9 where 0 is unusable and 9 is new)", bg="#8a307f", fg="white").grid(row=9, column=1,
                                                                                               sticky=W, padx=2, pady=3)
                Button(fr1, text="Submit", font=('verdana', 10), bg="#8a307f", command=self.retbooks).grid(row=10, column=1, sticky=NSEW, padx=5, pady=5)
                fr1.pack(side=TOP, anchor=CENTER, padx=50, pady=10)
                fr2.pack(side=TOP, anchor=N)
                frm.pack(side=TOP, anchor=CENTER, padx=50, pady=10)

        def retbooks(self):
                open = 1
                self.cur.execute(f"Select u_type from usertb where uid={self.sid.get()};")
                lvl = self.cur.fetchone()
                if lvl[0] > 3:
                        self.cur.execute(f"select bookscon from books where b_id={self.bid.get()};")
                        condition = self.cur.fetchone()
                        #self.master.bind('<Destroy>', self.setrun)
                        if condition[0] >= self.condi.get():
                                curtime = datetime.datetime.today()
                                self.cur.execute(f"Update loan set returndate='{curtime}' where (b_id={self.bid.get()} and uid={self.uid.get()});")
                                self.cur.execute(f"select overdue from loan where b_id={self.bid.get()}")
                                fee = self.cur.fetchone()
                                if fee:
                                        messagebox.showinfo(title="Due", message=f"The Lendee has to pay {fee[0]}")
                                        self.conn.commit()
                                        self.cur.close()
                                        self.conn.close()
                                        self.master.destroy()
                                else:
                                        messagebox.showinfo(title="Due", message="There were no fees levied")
                        else:
                                messagebox.showinfo(title="Input Error", message=f"Book condition cannot be better than when loaned!                  "
                                                                                 f"The book condition was {condition[0]}.")
                else:
                        messagebox.showerror(title="Low authority", message="You are not allowed to change return values")
                        exit(0)

