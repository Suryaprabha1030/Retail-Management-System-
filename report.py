from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import random,os,tempfile,smtplib
root=Tk()
root.geometry("1920x1080+0+0")
root.config(bg="blue")
#@image-------------------------------------------------------------------
img8=Image.open("C:/project/re.png")
r8_img=img8.resize((300,400))
i_img8=ImageTk.PhotoImage(r8_img)
#@@@function------------------------------------------------------------------------------------------------------------
def logout():
    root.destroy()


def fetch():
    emp6=a.get()
    if not emp6:
        return
    try:
        conn=mysql.connector.connect(host="localhost",user="root",password="",port="3306",database="supermarket")
        cursor=conn.cursor()
    except:
        messagebox.showerror("Error","unable to connect")

    query = "SELECT COUNT(`billno`) as count FROM `report` WHERE `employ id` = %s"

    emp6=str(a.get())
    vals=emp6
    cursor.execute(query,(emp6,))
    result = cursor.fetchone()[0]
   
    if result:
        h.set(result)
       
    else:
        messagebox.showerror("Error", "Product not found!")
    
def add():
    empx= a.get()
    empy= h.get()
    
    if not empy  or not  empx:
        messagebox.showerror("","please fill in entry field")
    textarea.insert(END, f"\n\t{empx}\t\t{empy}\n")
    
    # Clear the entry fields
    a.set("")
    h.set("")
def printt():
    textarea.delete(6.0,END)
    file=tempfile.mktemp('.txt')
    open(file,'w').write(textarea.get(1.0,END))
    os.startfile(file,'print') 
#@@@@report get area  ===============================================================================================================      
emp=Frame(root,width=1499,height=754,bd=0,bg="white").pack(pady=15)
emp1=Label(root,text="REPORT MANAGEMENT",fg="black",font=("times",20,'bold'),bg="white").place(x=430,y=20)
emp2=Label(root,text="ADMIN",fg="black",font=("times",12),bg="white").place(x=70,y=20)
emp3=Button(root,text="Logout",fg="white",bg="blue",width=7,font=("times",16),command=logout,relief=RIDGE).place(x=45,y=50)

emp4=LabelFrame(root,text="Menu",font=("times",13),width=410,height=560,bg="white",bd=3).place(x=100,y=140)
a=StringVar()
h=StringVar()
emp5=Label(root,text="employ id",fg="black",font=("times",14),bg="white").place(x=200,y=170)
emp6=Entry(root,bd=2,font=("times",20),width=15,textvariable=a).place(x=200,y=200)

emp5=Label(root,text="count",fg="black",font=("times",14),bg="white").place(x=220,y=270)
emp7=Entry(root,bd=2,font=("times",20),width=15,textvariable=h).place(x=200,y=300)
emp19=Button(root,text="SEARCH",fg="white",bg="blue",width=9,font=("times",14),command=fetch,relief=RIDGE,bd=0).place(x=130,y=580)
emp21=Button(root,text="ADD",fg="white",bg="blue",width=9,font=("times",14),command=add,relief=RIDGE,bd=0).place(x=250,y=580)
emp22=Button(root,text="print",fg="white",bg="blue",width=9,font=("times",14),command=printt,relief=RIDGE,bd=0).place(x=380,y=580)


###print area==============================================================

bill=Frame(root,bd=2,relief=GROOVE)
bill.place(x=540,y=148)

lblm=Label(bill,bd=3,relief=GROOVE,font=("times",18,"bold"),text="REPORT", fg="black",bg="#fff",padx=20)
lblm.pack(fill=X)



spin=Scrollbar(bill,orient=VERTICAL)
spin.pack(side=RIGHT,fill=Y)
textarea=Text(bill,width=41,height=22,bd=1,font=("times",15,"bold"),yscrollcommand=spin.set)
textarea.insert(END, f"\t         MONTHLY REPORT\n\n")
textarea.insert(END, f"=====================================\n")

textarea.insert(END, f"\tEMPLOYID\t\tCOUNT\n")
textarea.insert(END, f"=====================================\n")

textarea.pack(padx=3)
spin.config(command=textarea.yview)

frame2=Frame(root).place(x=1140,y=258)
bg1=Label(root,image=i_img8,border=0).place(x=1140,y=258)


if __name__ == '__main__':
    root.mainloop()
