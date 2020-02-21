from tkinter import *
import tkinter
import mysql.connector as mysql
import tkinter.messagebox as MessageBox
top = Tk()
top.geometry('500x500')
top.config(bg = 'blue')
def fun():
    id=num.get()
    print(id)
    con=mysql.connect(host="localhost",user="root",password="",database="sample")
    cursor=con.cursor()
    cursor.execute("insert into demo values('"+id+"')")
    cursor.execute("commit")
    MessageBox.showinfo("demo","done")
    con.close()
num=tkinter.StringVar()
e1= Entry(top,textvariable=num).place(x=80, y=40)
button = Button(top, text = ' button')
button.config(bg= 'yellow', font=('arial bold', 10 , 'underline'),command=fun)
button.place(x=20, y=40)
top.mainloop()
