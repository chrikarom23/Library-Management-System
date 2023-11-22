import tkinter
from tkinter import *
from tkinter import ttk
import mysql.connector
from tkinter import messagebox

from Windows import Addvalue
from Windows import Rembook
from Windows import Lout
from Windows.Returned import ret
from Windows import Loandets

#root = Tk()
# root.configure(background="black")
#root.title("Library Management System")
#root.iconbitmap(r"""C:\Users\chrik\Documents\Mini_project_yr_2\Book.ico""")
#root.geometry("700x350")

adder = None
remover = None
loan = None
bret = None


class Libdataview:
    def __init__(self, master):
        self.master = master
        master.title("Library Management System")
        master.iconbitmap(r"""C:\Users\chrik\Documents\Mini_project_yr_2\Book.ico""")
        master.geometry("693x345")
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
        Entry(self.Fr1, font=("Arial", 12), textvariable=self.Searchval).grid(row=0, column=1, padx=5, pady=5, sticky=W)
        Button(self.Fr1, text="Search", command=self.searchvalue, bg="#8a307f", fg="white").grid(row=0, column=2, padx=5, sticky=W)
        self.entry.grid(row=0, column=1, padx=5, pady=5, sticky=W)
        self.entry.focus()
        # reset search values
        Button(self.Fr1, text="Reset", command=self.resetvalue, bg="#8a307f", fg="white").grid(row=0, column=3, padx=5, pady=5)
        self.Fr1.grid(row=0, column=0, padx=10, pady=20)

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

        self.tree.grid(row =1, column=0, padx=4, pady=4)
        self.Fr2.grid(row=1, column=0)
        self.mfr.grid(row=0, column=1,padx=2, pady=2)


        self.options = LabelFrame(self.rfr, text="Functions", relief=RIDGE, cursor="dot", font=("arial", 14), bg="#79a7d3")
        Button(self.options, text="Add Book to Library", command=self.addbook, bg="#8a307f", fg="white").grid(row=0, column=1, ipadx=20, ipady=5, padx=3, pady=2,sticky=NSEW)
        Button(self.options, text="Remove Book from Library", command=self.rembook, bg="#8a307f", fg="white").grid(row=1, column=1, ipadx=20, ipady=5, padx=2, pady=3,sticky=NSEW)
        Button(self.options, text="Loan Out Book", command=self.loan_out, bg="#8a307f", fg="white").grid(row=2, column=1, ipadx=20, ipady=5, padx=3, pady=3,sticky=NSEW)
        Button(self.options, text="Loaned Book Return", command=self.returned, bg="#8a307f", fg="white").grid(row=3, column=1, ipadx=20, ipady=5, padx=2, pady=3,sticky=NSEW)
        Button(self.options, text="Get All Books", command=self.getall, bg="#8a307f", fg="white").grid(row=4, column=1, ipadx=20, ipady=5, padx=3, pady=2,sticky=NSEW)
        Button(self.options, text="Loan Search", command=self.loandet, bg="#8a307f", fg="white").grid(row=5, column=1, ipadx=20, ipady=5, padx=3, pady=2,sticky=NSEW)
        minifr = Frame(self.options, borderwidth=1, relief=SUNKEN)
        Label(minifr, text="Library Management System").grid(row=0, column=1, padx=3,  sticky=NSEW)
        Label(minifr, text="By Chris").grid(row=1, column=1,padx=3, sticky=NSEW)
        minifr.grid(row=6, column=1, padx=10, pady=4, sticky=NSEW)
        self.options.grid(row=0, column=5, padx=5, pady=7)
        self.rfr.grid(row=0, column=5, padx=3, pady=3)

    def setflag(self, event):
        global adder, remover, loan, returned, bret
        adder = None
        remover = None
        loan = None
        bret = None


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
                        self.cur.execute(f"select uid from loan where b_id = {i[0]};")
                        userwb = self.cur.fetchone()
                        self.cur.execute(f"select username from usertb where uid = {userwb[0]}")
                        uname = self.cur.fetchone()
                        self.tree.insert(parent='', index=0, iid=0, text='', values=(f"{i[0]}", f"{i[1]}", f"{i[2]}", f"{i[4]}", f"{i[3].decode()}", f"{uname[0]}"))
                        self.run = True
                    else:
                        x = self.tree.get_children()
                        for item in x:
                            self.tree.delete(item)
                        self.cur.execute(f"select uid from loan where b_id = {i[0]}")
                        userwb = self.cur.fetchone()
                        self.cur.execute(f"select username from usertb where uid = {userwb[0]}")
                        uname = self.cur.fetchone()
                        self.tree.insert(parent='', index=0, iid=0, text='',
                                         values=(f"{i[0]}", f"{i[1]}", f"{i[2]}", f"{i[4]}", f"{i[3].decode()}", f"{uname[0]}"))
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

    def addbook(self):
        global adder
        if not adder and not remover and not loan and not bret:
        #use top level here to reduce multiple windows
            adder = Toplevel()
            add = Addvalue.addval(adder)
            adder.bind('<Destroy>', self.setflag)
            adder.mainloop()
        #adder = False

    def rembook(self):
        global remover
        if not adder and not remover and not loan and not bret:
            remover = tkinter.Toplevel()
            rem = Rembook.remval(remover)
            remover.bind('<Destroy>', self.setflag)
            remover.mainloop()
        #remover = False

    def loan_out(self):
        global loan
        if not adder and not remover and not loan and not bret:
            loan = Toplevel()
            l = Lout.remval(loan)
            loan.bind('<Destroy>', self.setflag)
            loan.mainloop()

    def returned(self):
        global bret
        if not adder and not remover and not loan and not bret:
            bret = Toplevel()
            r = ret(bret)
            bret.bind('<Destroy>', self.setflag)
            bret.mainloop()

    def loandet(self):
        ldtable = Toplevel()
        l = Loandets.ldetails(ldtable)
        ldtable.mainloop()

    def getall(self):
        try:
            self.cur.execute("select * from Books;")
            sres = self.cur.fetchall()
        except:
            messagebox.showerror(title="Database", message="An error occured while trying to connect to the database")
        else:
            j = 0
            x = self.tree.get_children()
            for item in x:
                self.tree.delete(item)
            for i in sres:
                if not self.run:
                    self.cur.execute(f"select * from loan where b_id = {i[0]}")
                    userwb = self.cur.fetchone()
                    self.cur.execute(f"select username from usertb where uid = {userwb[0]}")
                    uname = self.cur.fetchone()
                    self.tree.insert(parent='', index=j, iid=j, text='',
                                     values=(f"{i[0]}", f"{i[1]}", f"{i[2]}", f"{i[4]}", f"{i[3].decode()}", uname[0]))
                    j += 1
                    self.run=True
                else:
                    self.cur.execute(f"select * from loan where b_id = {i[0]}")
                    userwb = self.cur.fetchone()
                    if userwb:
                        self.cur.execute(f"select username from usertb where uid = {userwb[0]}")
                        uname = self.cur.fetchone()
                    else:
                        uname=("None", )
                    self.tree.insert(parent='', index=j, iid=j, text='',
                                     values=(f"{i[0]}", f"{i[1]}", f"{i[2]}", f"{i[4]}", f"{i[3].decode()}", uname[0]))
                    j += 1

    #def resetvalues(self):
        #self.Ent1.delete(0, END)
        #pass


#r =Libdataview(root)
#root.mainloop()
