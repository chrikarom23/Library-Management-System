from tkinter import *
from tkinter import ttk
import mysql.connector
from tkinter import messagebox


class addval:
        def __init__(self,master):
                self.master = master
                master.title("Add Books")
                master.iconbitmap(r"""C:\Users\chrik\Documents\Mini_project_yr_2\Book.ico""")
                master.geometry("400x375")
                master.configure(background="#6883bc")
                self.conn = mysql.connector.connect(host="localhost", user="root", passwd="Romero23?",
                                                    database="library")
                self.cur = self.conn.cursor()
                self.bname = StringVar()
                self.con = IntVar()
                self.author = StringVar()
                self.genre = StringVar()
                frm = LabelFrame(master, text="Add Books", relief=RIDGE, font=("arial", 14), bg="#d9a5b3")
                fr1 = Frame(frm, bg="#79a7d3", relief=RIDGE)
                fr2 = Frame(frm, bg="#79a7d3", relief=RIDGE)

                #Label(fr1, text="Add Book to Library", font=("verdana", 10)).grid(row=0, column=1, sticky=N, padx=2, pady=3)

                Label(fr1, text="Book Title",  font=('verdana', 10), bg="#8a307f", fg="white").grid(row=1, column=1, sticky=W, padx=2, pady=3)
                ent1=self.ent1 = Entry(fr1, font=("Arial", 12), textvariable=self.bname)
                ent1.grid(row=2, column=1, sticky=W, padx=2, pady=3)
                ent1.focus_set()
                Label(fr1, text="Book Author", font=('verdana', 10), bg="#8a307f", fg="white").grid(row=3, column=1, sticky=W, padx=2, pady=3)
                self.ent2 = Entry(fr1, font=("Arial", 12), textvariable=self.author).grid(row=4, column=1, sticky=W, padx=2, pady=3)
                Label(fr1, text="Book Topics", font=('verdana', 10), bg="#8a307f", fg="white").grid(row=5, column=1, sticky=W, padx=2, pady=3)
                self.ent3 = Entry(fr1, font=("Arial", 12), textvariable=self.genre).grid(row=6, column=1, sticky=W, padx=2, pady=3)
                Label(fr1, text="Condition", font=('verdana', 10), bg="#8a307f", fg="white").grid(row=7, column=1, sticky=W, padx=2, pady=3)
                self.ent4 = Entry(fr1, font=("Arial", 12), textvariable=self.con).grid(row=8, column=1, sticky=W, padx=2, pady=3)
                Label(fr2, text="(Scaling from 1 to 9 where 0 is unusable and 9 is new)", bg="#6883bc",  relief=RIDGE).grid(row=9, column=1,
                                                                                               sticky=W, padx=2, pady=3)
                Button(fr2, text="Insert Book", command=self.addbooks, bg="#8a307f").grid(row=10, column=1, sticky=NSEW, padx=2, pady=3, ipadx=10, ipady=10)
                fr1.pack(side=TOP, anchor=CENTER, padx=50, pady=10)
                fr2.pack(side=TOP, anchor=N)
                frm.pack(side=TOP, anchor=CENTER, padx=50, pady=10)

        def addbooks(self):
                print(self.bname.get(),self.author.get(),self.genre.get(),self.con.get())
                if self.bname and self.author and self.genre:
                        try:
                                self.cur.execute(f"Insert into books(b_title, b_author, bookscon) values('{self.bname.get()}','{self.author.get()}',{self.con.get()});",)
                                self.cur.execute("select * from btops;")
                                topics = self.cur.fetchall()
                                self.cur.execute(f"Select b_id from books where b_title = '{self.bname.get()}';")
                                bid = self.cur.fetchone()
                                for i in topics:
                                        print(i)
                                        print(self.genre.get())
                                        if i[1] == self.genre.get().lower():
                                                self.cur.execute(f"insert into topicmid values({bid[0]}, {i[0]})")


                        except:
                                messagebox.showerror(title="Database error", message="There seems to be an error in the values you have entered")
                        else:
                                messagebox.showinfo(title="Success", message="The book has been inserted")
                                self.master.destroy()
                                self.conn.commit()
                                self.cur.close()
                                self.conn.close()
                else:
                        messagebox.showwarning(title="Input Error", message="Please enter the values")


        
#root = tkinter.Tk()



#object = addval(root)

#root.mainloop()