from tkinter import *
from tkinter import ttk
import mysql.connector
from tkinter import messagebox

class remval:
        def __init__(self, master):
                self.master = master
                master.title("Remove Books")
                master.iconbitmap(r"""C:\Users\chrik\Documents\Mini_project_yr_2\Book.ico""")
                master.geometry("375x310")
                master.configure(background="#6883bc")
                self.conn = mysql.connector.connect(host="localhost", user="root", passwd="Romero23?", database="library")
                self.cur = self.conn.cursor()
                self.bid = StringVar()
                self.username = StringVar()
                self.password = StringVar()
                fr1 = LabelFrame(master, text="Remove Books", relief=RIDGE, font=("arial", 14), bg="#79a7d3")

                #Label(fr1, text="Remove Book from Library", font=("verdana", 10), bg="gray").grid(row=0, column=1, sticky=N, padx=2, pady=3)

                Label(fr1, text="Book ID", font=('verdana', 10), bg="#8a307f", fg="white").grid(row=1, column=1, sticky=W, padx=5, pady=5)
                ent1 = Entry(fr1, font=("Arial", 12), textvariable=self.bid)
                ent1.grid(row=2, column=1, sticky=W, padx=5, pady=5)
                ent1.focus_set()
                Label(fr1, text="Username", font=('verdana', 10), bg="#8a307f", fg="white").grid(row=3, column=1, sticky=W, padx=5, pady=5)
                Entry(fr1, font=("Arial", 12), textvariable=self.username).grid(row=4, column=1, sticky=W, padx=5, pady=5)
                Label(fr1, text="Password", font=('verdana', 10), bg="#8a307f", fg="white").grid(row=5, column=1, sticky=W, padx=5, pady=5)
                Entry(fr1, font=("Arial", 12), textvariable=self.password, show="*",).grid(row=6, column=1, sticky=W, padx=5, pady=5)
                Label(fr1, text="*For security purposes we require ",
                      font=('verdana', 7), bg="#8a307f", fg="white").grid(row=7, column=1, sticky=NSEW, padx=5, pady=0)
                Label(fr1, text="the book id,your username and password.",
                      font=('verdana', 7), bg="#8a307f", fg="white").grid(row=8, column=1, sticky=NSEW, padx=5, pady=0)
                Button(fr1, text="Delete book records", command=self.rembooks, bg="#8a307f").grid(row=9, column=1, sticky=NSEW, padx=5, pady=5)
                fr1.pack(side=TOP, anchor=CENTER, padx=50, pady=10)

        def rembooks(self):
                self.cur.execute(f"select passw,u_type from usertb where username ='{self.username.get()}'")
                remsearch = self.cur.fetchone()
                if self.password.get() == remsearch[0]:
                        if remsearch[1] < 5:
                                messagebox.showwarning(title="Low Authority", message="You are not allowed to remove values from this database")
                                print("Quiting for safety...")
                                exit(0)
                        else:
                                if self.bid:
                                        try:
                                                self.cur.execute(f"delete from topicmid where bid = '{self.bid.get()}';")
                                                self.cur.execute(f"delete from loan where b_id ='{self.bid.get()}';")
                                                self.cur.execute(f"delete from books where b_id = '{self.bid.get()}'")
                                        except:
                                                messagebox.showerror(title="Database Error", message="An error occured while trying to delete item from the database")
                                        else:
                                                messagebox.showinfo(title="Success", message="The entered item was deleted from the database!")
                                                self.master.destroy()
                                                self.conn.commit()
                                                self.cur.close()
                                                self.conn.close()
                else:
                        messagebox.showwarning(title="Input error", message="Enter a valid username and password.")