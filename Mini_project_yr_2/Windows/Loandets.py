from tkinter import *
from tkinter import ttk
import mysql.connector
from tkinter import messagebox

#root =Tk()
w1 = None
w2 = None
w3 = None
w4 = None
w5 = None

class ldetails:
    def __init__(self, master):
        master.title("Library Management System")
        master.iconbitmap(r"""C:\Users\chrik\Documents\Mini_project_yr_2\Book.ico""")
        master.geometry("930x280")
        self.conn = mysql.connector.connect(host="localhost", user="root", passwd="Romero23?", database="library")
        self.cur = self.conn.cursor()
        self.mfr = Frame(master)
        self.rfr = Frame(master)
        self.username = StringVar()
        self.bt = StringVar()
        self.lid = IntVar()
        self.uid = IntVar()
        self.bid = IntVar()
        self.run = False

        Label(self.mfr, text="Loan Details", font=('verdana', 10), bg="gray").grid(row=0, column=1, padx=3, sticky=NSEW)

        sbx = Scrollbar(self.mfr, orient=HORIZONTAL)
        sby = Scrollbar(self.mfr, orient=VERTICAL)

        self.tree = ttk.Treeview(self.mfr, columns=("Loan id", "Book id", "User id", "Loan out date", "Expected return",
            "overdue", "returned date"), yscrollcommand=sby, xscrollcommand=sbx, selectmode="extended", show="headings")

        self.tree.heading("Loan id", text="loan id", anchor=NW)
        self.tree.heading("Book id", text="Book id", anchor=NW)
        self.tree.heading("User id", text="User id", anchor=NW)
        self.tree.heading("Loan out date", text="Loan out date", anchor=NW)
        self.tree.heading("Expected return", text="Expected return", anchor=NW)
        self.tree.heading("overdue", text="Overdue", anchor=NW)
        self.tree.heading("returned date", text="Returned date", anchor=NW)

        self.tree.column('#1', stretch=NO, minwidth=0, width=100)
        self.tree.column('#2', stretch=NO, minwidth=0, width=100)
        self.tree.column('#3', stretch=NO, minwidth=0, width=100)
        self.tree.column('#4', stretch=NO, minwidth=0, width=100)
        self.tree.column('#5', stretch=NO, minwidth=0, width=100)
        self.tree.column('#6', stretch=NO, minwidth=0, width=100)
        self.tree.column('#7', stretch=NO, minwidth=0, width=100)

        self.tree.grid(row=1,column=1,padx=5,pady=5)
        self.mfr.grid(row=0, column=0,padx=10, pady=10)

        sep = ttk.Separator(master, orient=VERTICAL)
        sep.grid(sticky=NS, row=0, column=3)

        self.options = LabelFrame(self.rfr, text="Functions", relief=RIDGE, cursor="dot", font=("arial", 14))
        Button(self.options, text="Search by Username", command=self.sbu).grid(row=0, column=1, ipadx=20, ipady=5, padx=3, pady=4,sticky=NSEW)
        Button(self.options, text="Search by Book Title", command=self.sbbt).grid(row=1, column=1, ipadx=20, ipady=5, padx=3, pady=4,sticky=NSEW)
        Button(self.options, text="Search by UID", command=self.sbuid).grid(row=2, column=1, ipadx=20, ipady=5, padx=3, pady=4,sticky=NSEW)
        Button(self.options, text="Search by LID", command=self.sblid).grid(row=3, column=1, ipadx=20, ipady=5, padx=3, pady=4,sticky=NSEW)
        Button(self.options, text="Search by BID", command=self.sbbid).grid(row=4, column=1, ipadx=20, ipady=5, padx=3, pady=4,sticky=NSEW)
        self.options.grid(row=0, column=5, padx=5, pady=7)
        self.rfr.grid(row=0, column=4,padx=10, pady=10)

    def setflag(self, event):
        global w1, w2, w3, w4, w5
        w1 = None
        w2= None
        w3 = None
        w4 = None
        w5 = None

    def sbu(self):
        global w1
        if not w1 and not w2 and not w3 and not w4 and not w5:
            w1 = Toplevel()
            Label(w1, text="Enter the username:", font=('verdana', 10), bg="gray").grid(row=0, column=0, sticky=W, padx=5, pady=5)
            ent1 = Entry(w1, textvariable=self.username)
            ent1.grid(row=0, column=1, sticky=W, padx=5, pady=5)
            ent1.focus_set()
            w1.bind('<Destroy>', self.setflag)
            Button(w1, text="Submit", command=self.sbuwin).grid(row=0, column=2, sticky=W, padx=5, pady=5)
        
    def sbbt(self):
        global w2
        if not w1 and not w2 and not w3 and not w4 and not w5:
            w2 = Toplevel()
            Label(w2, text="Enter the Book title:", font=('verdana', 10), bg="gray").grid(row=0, column=0, sticky=W,
                                                                           padx=5, pady=5)
            ent1 = Entry(w2, textvariable=self.bt)
            ent1.grid(row=0, column=1, sticky=W, padx=5, pady=5)
            ent1.focus_set()
            w2.bind('<Destroy>', self.setflag)
            Button(w2, text="Submit", command=self.sbbtwin).grid(row=0, column=2, sticky=W, padx=5, pady=5)

    def sblid(self):
        global w3
        if not w1 and not w2 and not w3 and not w4 and not w5:
            w3 = Toplevel()
            Label(w3, text="Enter Loan ID:", font=('verdana', 10), bg="gray").grid(row=0, column=0, sticky=W,
                                                                                              padx=5, pady=5)
            ent1 = Entry(w3, textvariable=self.lid)
            ent1.grid(row=0, column=1, sticky=W, padx=5, pady=5)
            ent1.focus_set()
            w3.bind('<Destroy>', self.setflag)
            Button(w3, text="Submit", command=self.sblidwin).grid(row=0, column=2, sticky=W, padx=5, pady=5)

    def sbuid(self):
        global w4
        if not w1 and not w2 and not w3 and not w4 and not w5:
            w4 = Toplevel()
            Label(w4, text="Enter User ID:", font=('verdana', 10), bg="gray").grid(row=0, column=0, sticky=W,
                                                                                              padx=5, pady=5)
            ent1 = Entry(w4, textvariable=self.uid)
            ent1.grid(row=0, column=1, sticky=W, padx=5, pady=5)
            ent1.focus_set()
            w4.bind('<Destroy>', self.setflag)
            Button(w4, text="Submit", command=self.sbuidwin).grid(row=0, column=2, sticky=W, padx=5, pady=5)

    def sbbid(self):
        global w5
        if not w1 and not w2 and not w3 and not w4 and not w5:
            w5 = Toplevel()
            Label(w5, text="Enter Book ID:", font=('verdana', 10), bg="gray").grid(row=0, column=0, sticky=W,
                                                                                              padx=5, pady=5)
            ent1 = Entry(w5, textvariable=self.bid)
            ent1.grid(row=0, column=1, sticky=W, padx=5, pady=5)
            ent1.focus_set()
            w5.bind('<Destroy>', self.setflag)
            Button(w5, text="Submit", command=self.sbbidwin).grid(row=0, column=2, sticky=W, padx=5, pady=5)

    def sbuwin(self):
        j = 0
        if not self.run:
            self.cur.execute(f"select uid from usertb where username='{self.username.get()}'")
            uid = self.cur.fetchone()
            if not uid:
                messagebox.showerror(title="Input error", message="Enter a value!")
            else:
                self.cur.execute(f"select * from loan where uid='{uid[0]}';")
                searchres = self.cur.fetchall()
                if not searchres:
                    messagebox.showerror(title="Input Error", message="No records for the given value")
                else:
                    for i in searchres:
                        self.tree.insert(parent='', index=j, iid=j, text='', values=(i[0], i[1], i[2], f"{i[3]}", f"{i[4]}", f"{i[5]}", f"{i[6]}"))
                    self.run=True
                    j += 1
        else:
            x = self.tree.get_children()
            for item in x:
                self.tree.delete(item)
            self.cur.execute(f"select uid from usertb where username='{self.username.get()}'")
            uid = self.cur.fetchone()
            if not uid:
                messagebox.showerror(title="Input Error", message="Enter valid input")
            else:
                self.cur.execute(f"select * from loan where uid='{uid[0]}';")
                searchres = self.cur.fetchall()
                if not searchres:
                    messagebox.showerror(title="Input Error", message="No records for the given value")
                else:
                    for i in searchres:
                        self.tree.insert(parent='', index=j, iid=j, text='',
                                         values=(i[0], i[1], i[2], f"{i[3]}", f"{i[4]}", i[5], f"{i[6]}"))
                    j += 1

    def sbbtwin(self):
        j = 0
        if not self.run:
            self.cur.execute(f"select b_id from books where b_title='{self.bt.get()}'")
            bid = self.cur.fetchone()
            if not bid:
                messagebox.showerror(title="Input Error", message="Enter a value!")
            else:
                self.cur.execute(f"select * from loan where b_id='{bid[0]}';")
                searchres = self.cur.fetchall()
                if not searchres:
                    messagebox.showerror(title="Input Error", message="No records for the given value")
                else:
                    for i in searchres:
                        self.tree.insert(parent='', index=j, iid=j, text='',
                                         values=(i[0], i[1], i[2], f"{i[3]}", f"{i[4]}", f"{i[5]}", f"{i[6]}"))
                    self.run = True
                    j += 1
        else:
            x = self.tree.get_children()
            for item in x:
                self.tree.delete(item)
            self.cur.execute(f"select b_id from books where b_title='{self.bt.get()}'")
            bid = self.cur.fetchone()
            if not bid:
                messagebox.showerror(title="Input Error", message="Enter valid input")
            else:
                self.cur.execute(f"select * from loan where b_id='{bid[0]}';")
                searchres = self.cur.fetchall()
                if not searchres:
                    messagebox.showerror(title="Input Error", message="No records for the given value")
                else:
                    for i in searchres:
                        self.tree.insert(parent='', index=j, iid=j, text='',
                                         values=(i[0], i[1], i[2], f"{i[3]}", f"{i[4]}", i[5], f"{i[6]}"))
                    j += 1

    def sblidwin(self):
        j = 0
        if not self.run:
            self.cur.execute(f"select * from loan where lid={self.lid.get()};")
            searchres = self.cur.fetchall()
            if not searchres:
                messagebox.showerror(title="Input Error", message="No records for the given value")
            else:
                for i in searchres:
                    self.tree.insert(parent='', index=j, iid=j, text='',
                                     values=(i[0], i[1], i[2], f"{i[3]}", f"{i[4]}", f"{i[5]}", f"{i[6]}"))
                self.run = True
                j += 1
        else:
            x = self.tree.get_children()
            for item in x:
                self.tree.delete(item)
            self.cur.execute(f"select * from loan where lid={self.lid.get()};")
            searchres = self.cur.fetchall()
            if not searchres:
                messagebox.showerror(title="Input Error", message="No records for the given value")
            else:
                for i in searchres:
                    self.tree.insert(parent='', index=j, iid=j, text='',
                                     values=(i[0], i[1], i[2], f"{i[3]}", f"{i[4]}", i[5], f"{i[6]}"))
                j += 1

    def sbuidwin(self):
        j = 0
        if not self.run:
            self.cur.execute(f"select * from loan where uid={self.uid.get()};")
            searchres = self.cur.fetchall()
            if not searchres:
                messagebox.showerror(title="Input Error", message="No records for the given value")
            else:
                for i in searchres:
                    self.tree.insert(parent='', index=j, iid=j, text='',
                                     values=(i[0], i[1], i[2], f"{i[3]}", f"{i[4]}", f"{i[5]}", f"{i[6]}"))
                self.run = True
                j += 1
        else:
            x = self.tree.get_children()
            for item in x:
                self.tree.delete(item)
            self.cur.execute(f"select * from loan where uid={self.uid.get()};")
            searchres = self.cur.fetchall()
            if not searchres:
                messagebox.showerror(title="Input Error", message="No records for the given value")
            else:
                for i in searchres:
                    self.tree.insert(parent='', index=j, iid=j, text='',
                                     values=(i[0], i[1], i[2], f"{i[3]}", f"{i[4]}", i[5], f"{i[6]}"))
                j += 1

    def sbbidwin(self):
        j = 0
        if not self.run:
            self.cur.execute(f"select * from loan where b_id={self.bid.get()};")
            searchres = self.cur.fetchall()
            if not searchres:
                messagebox.showerror(title="Input Error", message="No records for the given value")
            else:
                for i in searchres:
                    self.tree.insert(parent='', index=j, iid=j, text='',
                                     values=(i[0], i[1], i[2], f"{i[3]}", f"{i[4]}", f"{i[5]}", f"{i[6]}"))
                self.run = True
                j += 1
        else:
            x = self.tree.get_children()
            for item in x:
                self.tree.delete(item)
            self.cur.execute(f"select * from loan where b_id={self.bid.get()};")
            searchres = self.cur.fetchall()
            if not searchres:
                messagebox.showerror(title="Input Error", message="No records for the given value")
            else:
                for i in searchres:
                    self.tree.insert(parent='', index=j, iid=j, text='',
                                     values=(i[0], i[1], i[2], f"{i[3]}", f"{i[4]}", i[5], f"{i[6]}"))
                j += 1

#runner = ldetails(root)
#root.mainloop()