from tkinter import *

from Auth_Form import Auth
import Database


if __name__ == "__main__":
    root = Tk()
    Database.create_db()
    mainobject = Auth(root)
    mainobject.get_info()
    root.mainloop()