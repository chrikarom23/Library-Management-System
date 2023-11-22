from tkinter import *
from tkinter import ttk
import mysql.connector
from tkinter import messagebox

class Libdataviewlow:
    def __init__(self, master):
        self.master = master
        master.title("Library Management System")
        master.iconbitmap(r"""C:\Users\chrik\Documents\Mini_project_yr_2\Book.ico""")
        master.geometry("500x350")
        master.configure(background="#6883bc")
        self.conn = mysql.connector.connect(host="localhost", user="root", passwd="Romero23?", database="library")
        self.cur = self.conn.cursor()
        self.run = False
        self.mfr = Frame(master, bg="#d9a5b3")
        self.rfr = Frame(master, bg="#d9a5b3")
        self.Fr1 = LabelFrame(self.mfr, text="Search", relief=RIDGE, font=("arial", 14), bg="#79a7d3")
        self.Fr2 = Frame(self.mfr, bg="#79a7d3")
        self.Searchval = StringVar()
        self.bname = ''
        self.con = ''
        self.Lstat = ''
        self.Lto = ''
        self.entry = Entry(self.Fr1, font=("Arial", 12), textvariable=self.Searchval)
        # search
        Label(self.Fr1, text="Enter title to search:", font=('verdana', 10), bg="#8a307f", fg="white").grid(row=0, column=0, padx=3, sticky=W)
        ent = Entry(self.Fr1, font=("Arial", 12), textvariable=self.Searchval)
        ent.grid(row=0, column=1, padx=5, pady=5, sticky=W)
        ent.focus_set()
        Button(self.Fr1, text="Search", command=self.searchvalue, bg="#8a307f", fg="white").grid(row=0, column=2, padx=5, sticky=W)
        self.entry.grid(row=0, column=1, padx=5, pady=5, sticky=W)
        self.entry.focus()
        # reset search values
        Button(self.Fr1, text="Reset", command=self.resetvalue, bg="#8a307f", fg="white").grid(row=0, column=3, padx=5, pady=5)
        self.Fr1.grid(row=0, column=0, padx=20, pady=20)

        scrollbarx = Scrollbar(self.Fr2, orient=HORIZONTAL)
        scrollbary = Scrollbar(self.Fr2, orient=VERTICAL)

        self.tree = ttk.Treeview(self.Fr2, columns=("Book id", "Book Title","Book Author", "Condition", "Loan Status", "Loaned to")
                            , yscrollcommand=scrollbary, xscrollcommand=scrollbarx, selectmode="extended", show='headings')
        self.tree.heading("Book id", text="Book id", anchor=NW)
        self.tree.heading("Book Title", text="Book Title", anchor=NW)
        self.tree.heading("Book Author", text="Book Author", anchor=NW)
        self.tree.heading("Condition", text="Book Condition", anchor=NW)
        self.tree.heading("Loan Status", text="Loan Status", anchor=NW)
        self.tree.heading("Loaned to", text="Loaned to", anchor=NW)

        self.tree.column('#1', stretch=NO, minwidth=0, width=50)
        self.tree.column('#2', stretch=NO, minwidth=0, width=80)
        self.tree.column('#3', stretch=NO, minwidth=0, width=80)
        self.tree.column('#4', stretch=NO, minwidth=0, width=100)
        self.tree.column('#5', stretch=NO, minwidth=0, width=75)
        self.tree.column('#6', stretch=NO, minwidth=0, width=75)

        self.tree.grid(row =1, column=0, padx=5, pady=5)
        self.Fr2.grid(row=1, column=0)
        self.mfr.grid(row=0, column=1,padx=2, pady=2)


    def searchvalue(self):
        try:
            self.cur.execute(f"Select * from books where b_title = '{self.Searchval.get()}'")
            searchres = self.cur.fetchall()
        except:
            messagebox.showerror(title="Database error", text="An error occured while fetching data from the database")
        else:
            if searchres:
                for i in searchres:
                    if not self.run:
                        self.cur.execute(f"select * from loan where b_id = {i[0]}")
                        userwb = self.cur.fetchone()
                        self.tree.insert(parent='', index=0, iid=0, text='', values=(f"{i[0]}", f"{i[1]}", f"{i[2]}", f"{i[4]}", f"{i[3].decode()}", userwb))
                        self.run = True
                    else:
                        x = self.tree.get_children()
                        for item in x:
                            self.tree.delete(item)
                        self.cur.execute(f"select * from loan where b_id = {i[0]}")
                        userwb = self.cur.fetchone()
                        self.tree.insert(parent='', index=0, iid=0, text='',
                                         values=(f"{i[0]}", f"{i[1]}", f"{i[2]}", f"{i[4]}", f"{i[3].decode()}", userwb))
            elif not self.Searchval:
                messagebox.showinfo(title="No Result",
                                    message="Insert value to search for")
            else:
                try:
                    x = self.tree.get_children()
                    for item in x:
                        self.tree.delete(item)
                    messagebox.showinfo(title="No Result", message="There is no book with that title in here. Try inserting the exact title.")
                except:
                    messagebox.showerror(title="Database Error", message="An error occured while trying to fetch data from the database")

    def resetvalue(self):
        self.entry.delete(0, END)