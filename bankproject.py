import tkinter
from tkinter import *
from tkinter import ttk, font, messagebox
import pymysql as mysql
import tk as tk

def updatec(amt,id,win):
    connection = mysql.connect(host="localhost",user="root",password="livewire",database="python1")
    cursor=connection.cursor()
    cursor.execute('select balance from customers where id=%s', (id))
    u=cursor.fetchone()
    a=0
    for x in u:
        a=int(x)

    balance=a+int(amt)
    cursor.execute('update customers set balance=%s where id=%s', (balance,id))
    connection.commit()
    messagebox.showinfo( "Success", "Credited Successfully")
    connection.close()
    customerpage(id,win)


def updated(amt,id,win):
    connection = mysql.connect(host="localhost",user="root",password="livewire",database="python1")
    cursor=connection.cursor()
    cursor.execute('select balance from customers where id=%s', (id))
    u=cursor.fetchone()
    a=0
    for x in u:
        a=int(x)
    if(int(amt)<a):
        balance=a-int(amt)
        cursor.execute('update customers set balance=%s where id=%s', (balance,id))
        connection.commit()
        messagebox.showinfo( "Success", "Debited Successfully")
        connection.close()
        customerpage(id,win)
    else:
        messagebox.showinfo( "Error", "Your Balance is Insufficient")

def balance(id):
    connection = mysql.connect(host="localhost",user="root",password="livewire",database="python1")
    cursor=connection.cursor()
    cursor.execute('select balance from customers where id=%s', (id))
    u=cursor.fetchone()
    a=0
    for x in u:
        a=int(x)
    return a
def customerpage(cid,win):
    win.destroy()
    win = Tk()
    win.geometry("1500x700")
    win.title("bank")
    frame = Frame(win, width=1500, height=50, bg="blue")
    frame.pack()
    win.attributes('-fullscreen', True)
    label_font = font.Font(weight="bold", family="Times New Roman", size=30)
    x = Label(frame, text="SRI BANK", font=label_font, bg="Red")
    x.config(bg="blue", fg="white")
    x.place(relx=0.43, rely=0.01)
    label_font = font.Font(weight="bold", family="Times New Roman", size=20)
    s = """A bank is a financial institution that accepts deposits from the public
    and creates a demand deposit while simultaneously making loans.
    Lending activities can be directly performed by the bank or indirectly through capital markets."""
    l = Label(win, text=s, font=label_font)
    l.place(relx=0.1, rely=0.1)
    frame = Frame(win)
    b=Label(win,text="Credit:",font=label_font)
    b.place(relx=0.3,rely=0.3)
    c=Label(win,text="Debit:",font=label_font)
    c.place(relx=0.3,rely=0.4)
    a1=Entry(win)
    a1.place(relx=0.45,rely=0.3,width=150,height=30)
    b1=Entry(win)
    b1.place(relx=0.45,rely=0.4,width=150,height=30)
    label_font=font.Font(weight="bold",family="Times New Roman",size=15)
    b=Button(win,text="Credit",font=label_font,command=lambda:updatec(a1.get(),cid,win))
    b.place(relx=0.6,rely=0.3)
    b=Button(win,text="Debit",font=label_font,command=lambda:updated(b1.get(),cid,win))
    b.place(relx=0.6,rely=0.4)
    label_font=font.Font(weight="bold",family="Times New Roman",size=25)
    blabel=Label(win,text="Your Balance : ",font=label_font)
    blabel.place(relx=0.3,rely=0.5)
    blabel=Label(win,text=balance(cid),font=label_font)
    blabel.place(relx=0.47,rely=0.5)
    win.mainloop()





def customer(win):
    win.destroy()
    win=Tk()
    win.geometry("300x300")
    win.title("bank")
    win.attributes('-fullscreen', True)
    frame=Frame(win,width=1500,height=50,bg="blue")
    frame.pack()
    label_font=font.Font(weight="bold",family="Times New Roman",size=30)
    x=Label(frame,text="SRI BANK",font=label_font)
    x.config(bg= "blue", fg= "white")
    x.place(relx=0.43,rely=0.01)
    frame=Frame(win,width=500,height=300,bg="pink")
    frame.pack()
    frame.place(relx=0.3,rely=0.3)
    label_font=font.Font(weight="bold",family="Times New Roman",size=20)
    x=Label(frame,text="CUSTOMER LOGIN",font=label_font)
    x.place(relx=0.35,rely=0.1)
    x.config(bg= "pink")
    label_font=font.Font(weight="bold",family="Times New Roman",size=17)
    a=Label(frame,text="Customer number:",font=label_font)
    a.place(relx=0.1,rely=0.4)
    a.config(bg= "pink")
    b=Label(frame,text="Password:",font=label_font)
    b.place(relx=0.1,rely=0.55)
    b.config(bg= "pink")
    a1=Entry(frame)
    a1.place(relx=0.5,rely=0.42, width=200, height=25)
    b1=Entry(frame,show="*")
    b1.place(relx=0.5,rely=0.57, width=200, height=25)
    b5=Button(frame,text="Login",font=label_font,command=lambda:customerLogin(a1.get(),b1.get(),win))
    b5.place(relx=0.3,rely=0.8)
    frame=Frame(win,width=1500,height=50,bg="blue")
    frame.pack()
    frame.place(relx=0.0,rely=0.94)
    label_font=font.Font(weight="bold",family="Times New Roman",size=20)
    x=Label(frame,text="Copyright © 2023 Sri ",font=label_font,bg="Red")
    x.config(bg= "blue", fg= "white")
    x.place(relx=0.35,rely=0.1)
    win.mainloop()
#Admin Login
def admin(win):
    win.destroy()
    win=Tk()
    win.geometry("300x300")
    win.title("bank")
    win.attributes('-fullscreen', True)
    frame=Frame(win,width=1500,height=50,bg="blue")
    frame.pack()
    label_font=font.Font(weight="bold",family="Times New Roman",size=30)
    x=Label(frame,text="SRI BANK",font=label_font)
    x.config(bg= "blue", fg= "white")
    x.place(relx=0.43,rely=0.01)
    frame=Frame(win,width=500,height=300,bg="pink")
    frame.pack()
    frame.place(relx=0.3,rely=0.3)
    label_font=font.Font(weight="bold",family="Times New Roman",size=20)
    x=Label(frame,text="ADMIN LOGIN",font=label_font)
    x.place(relx=0.35,rely=0.1)
    x.config(bg= "pink")
    label_font=font.Font(weight="bold",family="Times New Roman",size=17)
    a=Label(frame,text="Admin number:",font=label_font)
    a.place(relx=0.1,rely=0.4)
    a.config(bg= "pink")
    b=Label(frame,text="Password:",font=label_font)
    b.place(relx=0.1,rely=0.55)
    b.config(bg= "pink")
    a1=Entry(frame)
    a1.place(relx=0.5,rely=0.42, width=200, height=25)
    b1=Entry(frame,show="*")
    b1.place(relx=0.5,rely=0.57, width=200, height=25)
    b5=Button(frame,text="Login",font=label_font,command=lambda:adminLogin(a1.get(),b1.get(),win))
    b5.place(relx=0.3,rely=0.8)
    frame=Frame(win,width=1500,height=50,bg="blue")
    frame.pack()
    frame.place(relx=0.0,rely=0.94)
    label_font=font.Font(weight="bold",family="Times New Roman",size=20)
    x=Label(frame,text="Copyright © 2023 Sri ",font=label_font,bg="Red")
    x.config(bg= "blue", fg= "white")
    x.place(relx=0.35,rely=0.1)
    win.mainloop()



#Admin Login Check
def adminLogin(id,pin,win):
    connection = mysql.connect(host="localhost",user="root",password="livewire",database="python1")
    cursor=connection.cursor()
    cursor.execute('SELECT * FROM users WHERE username=%s AND password=%s', (id, pin))
    user = cursor.fetchone()
    connection.close()
    if user:
        admin1(win)
    else:
        messagebox.showerror( "Incorrect", "Invalid UserId and Password")

def customerLogin(id,pin,win):
    connection = mysql.connect(host="localhost",user="root",password="livewire",database="python1")
    cursor=connection.cursor()
    cursor.execute('SELECT * FROM customers WHERE Username=%s AND id=%s', (id, pin))
    user = cursor.fetchone()
    connection.close()
    if user:
        customerpage(pin,win)
    else:
        messagebox.showerror( "Incorrect", "Invalid UserId and Password")

def print1():
    print("Login Successfully")

def insert(name,age,deposite):
    import pymysql as mysql
    connection = mysql.connect(host="localhost",user="root",password="livewire",database="python1")
    cursor=connection.cursor()
    s="insert into customers(Username,age,balance) values(%s,%s,%s)"
    t=(name,age,deposite)
    cursor.execute(s,t)
    connection.commit()
    messagebox.showinfo( "Success", "User Insert Successfully")

def admin1(win):
    win.destroy()
    win = Tk()
    win.geometry("1500x700")
    win.title("bank")
    def show_data():
        import pymysql as mysql
        connection = mysql.connect(host="localhost", user="root", password="livewire", database="python1")
        cursor = connection.cursor()
        cursor.execute('SELECT * FROM customers')
        data = cursor.fetchall()
        connection.close()
        for item in tree.get_children():
                            tree.delete(item)
        for row in data:
            tree.insert("", "end", values=row)
    frame = Frame(win, width=1500, height=50, bg="blue")
    win.attributes('-fullscreen', True)
    frame.pack()
    label_font = font.Font(weight="bold", family="Times New Roman", size=30)
    x = Label(frame, text="SRI BANK", font=label_font, bg="Red")
    x.config(bg="blue", fg="white")
    x.place(relx=0.43, rely=0.01)
    label_font = font.Font(weight="bold", family="Times New Roman", size=20)
    s = """A bank is a financial institution that accepts deposits from the public
    and creates a demand deposit while simultaneously making loans.
    Lending activities can be directly performed by the bank or indirectly through capital markets."""
    l = Label(win, text=s, font=label_font)
    l.place(relx=0.1, rely=0.1)
    frame = Frame(win)
    frame.pack()
    frame.place(relx=0.4, rely=0.4)
    show = Button(frame, text="Show Data", command=show_data)
    show.pack()
    tree = ttk.Treeview(frame, columns=("Account Number", "Name", "Age", "Balance"), show="headings")
    tree.heading("Account Number", text="Account Number")
    tree.heading("Name", text="Name")
    tree.heading("Age", text="Age")
    tree.heading("Balance", text="Balance")
    tree.pack()
    frame1=Frame(win,width=250, height=270, bg="gray")
    frame1.pack()
    frame1.place(relx=0.1, rely=0.42)
    label_font=font.Font(weight="bold",family="Times New Roman",size=10)
    x=Label(frame1,text="REGISTRATION",font=label_font, bg="gray")
    x.place(relx=0.35,rely=0.01)
    a=Label(frame1,text="Customer Name:",font=label_font, bg="gray")
    a.place(relx=0.01,rely=0.2)
    b=Label(frame1,text="Customer age:",font=label_font, bg="gray")
    b.place(relx=0.01,rely=0.3)
    c=Label(frame1,text="Amount Deposit:",font=label_font, bg="gray")
    c.place(relx=0.01,rely=0.4)
    a1=Entry(frame1)
    a1.place(relx=0.5,rely=0.2)
    b1=Entry(frame1)
    b1.place(relx=0.5,rely=0.3)
    c1=Entry(frame1)
    c1.place(relx=0.5,rely=0.4)
    label_font=font.Font(weight="bold",family="Times New Roman",size=10)
    b=Button(frame1,text="Registration",font=label_font,command=lambda:insert(a1.get(),b1.get(),c1.get()))
    b.place(relx=0.35,rely=0.5)
    win.mainloop()






#HOME Page
"Home Page"
win=Tk()
win.geometry("1500x700")
win.title("bank")
frame=Frame(win,width=1500,height=50,bg="blue")
frame.pack()
label_font=font.Font(weight="bold",family="Times New Roman",size=30)
x=Label(frame,text="SRI BANK",font=label_font,bg="Red")
x.config(bg= "blue", fg= "white")
x.place(relx=0.43,rely=0.01)
label_font=font.Font(weight="bold",family="Times New Roman",size=20)
s="""A bank is a financial institution that accepts deposits from the public
and creates a demand deposit while simultaneously making loans.
Lending activities can be directly performed by the bank or indirectly through capital markets."""
l=Label(win,text=s,font=label_font)
l.place(relx=0.1,rely=0.1)
label_font=font.Font(weight="bold",family="Times New Roman",size=20)
b=Button(win,text="Admin Login",font=label_font,command=lambda:admin(win))
b.place(relx=0.42,rely=0.3)
label_font=font.Font(weight="bold",family="Times New Roman",size=20)
q="""A person or entity that maintains an account and/or has business relationships with the bank.
One on whose behalf the account is maintained.
The beneficiary of the transaction carried professional intermediaries."""
l=Label(win,text=q,font=label_font)
l.place(relx=0.1,rely=0.4)
b=Button(win,text="Customer Login",font=label_font,command=lambda:customer(win))
b.place(relx=0.4,rely=0.6)

win.attributes('-fullscreen', True)
label_font=font.Font(weight="bold",family="Times New Roman",size=20)
q="""A financial institution licensed to receive deposits and make loans.
 There are several types of banks including retail,
  commercial, and investment banks."""
l=Label(win,text=q,font=label_font)
l.place(relx=0.21,rely=0.7)
frame=Frame(win,width=1500,height=50,bg="blue")
frame.pack()
frame.place(relx=0.0,rely=0.94)
label_font=font.Font(weight="bold",family="Times New Roman",size=20)
x=Label(frame,text="Copyright © 2023 Sri ",font=label_font,bg="Red")
x.config(bg= "blue", fg= "white")
x.place(relx=0.35,rely=0.1)
win.mainloop()





