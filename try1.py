from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import random,os,tempfile,smtplib

import subprocess
def sub1():
    subprocess.Popen(["python", "market.py"])
def sub():
    subprocess.Popen(["python", "employ1.py"])

root=Tk()
root.geometry("1920x1080")
root.title("grocery management system")
#@@@@@============================================image=====================================================================================================================================

img4=Image.open("C:/project/emkw.png")
r4_img=img4.resize((170,170))
i_img4=ImageTk.PhotoImage(r4_img)



img7=Image.open("C:/project/emke.png")
r7_img=img7.resize((170,170))
i_img7=ImageTk.PhotoImage(r7_img)

img1=Image.open("C:/project/bg8.png")
r_img=img1.resize((1900,1000))
bg_img=ImageTk.PhotoImage(r_img)

img2=Image.open("C:/project/adminay.png")
r2_img=img2.resize((170,170))
i_img2=ImageTk.PhotoImage(r2_img)

img3=Image.open("C:/project/emplyae.png")
r3_img=img3.resize((165,164))
i_img3=ImageTk.PhotoImage(r3_img)
#@@@@@@@@@@@@@@@@========================================admin login========================================================================================================================
def admin():
    global uEntry,pEntry,window2
    window2=Tk()
    window2.geometry("500x500")
    window2.config(bg="black")
#@==================login page=================
    global a,b
    a=StringVar()
    b=StringVar()
    Lbl=Label(window2,text="ADMIN LOGIN",font=("times",20,"bold"),fg="#fff",bg="#000").pack()
    lbl1=Label(window2,text="Username",font=("times",20,"bold"),fg="#fff",bg="#000").place(x=30,y=40)
    user=Entry(window2,font=("times",20,"bold"),bd=0,width=27,textvariable=a)
    user.place(x=30,y=80)
    lbl1=Label(window2,text="Password",font=("times",20,"bold"),fg="#fff",bg="#000").place(x=30,y=140)
    pword=Entry(window2,font=("times",20,"bold"),textvariable=b,bd=0,width=27)
    pword.place(x=30,y=180)
    def signin():
        try:
            conn=mysql.connector.connect(host="localhost",user="root",password="",port="3306",database="supermarket")
            cursor=conn.cursor()
        except:
            messagebox.showerror("Error","unable to connect")

        username=user.get()
        password=pword.get()
        insert_query="select * from login where username=%s and password=%s;"
        vals=(username,password)
        cursor.execute(insert_query,vals)
        a=cursor.fetchone()
        if a:
            window2.destroy()
            screen=Toplevel(root)
            screen.title("App")
            screen.geometry('1920x1080+0+0')
            #screen.config(bg="black")
            frame2=Frame(screen).pack(pady=50)
            bg1=Label(screen,image=bg_img,border=0).place(x=0,y=0)
            lab=Label(screen,text="TOVINO SUPER MARKET",font=("verdana",45,'bold'),bg="blue",fg="white",bd=5).pack(pady=10)
            btnimg1=Button(screen,image=i_img4,command=sub,borderwidth=0).place(x=490,y=320)
            
            btnimg2=Button(screen,image=i_img7,command=sub1,borderwidth=0).place(x=830,y=320)
            def logout():
                screen.destroy()
            btne=Button(screen,text="Logout",fg="white",bg="blue",width=10,font=("times",16),command=logout,relief=RIDGE).place(x=45,y=50)

            
            screen.mainloop()
            

        else:
            messagebox.showerror("info","not match")
    btn3=Button(window2,text="login",font=("times",20,"bold"),bg="red",fg="white",bd=0,relief=GROOVE,width=10,command=signin).place(x=150,y=250)
#@@@@@@@=========================userlogin===================================================================================================================================================
def userlogin():
    subprocess.Popen(["python","try.py"])
    
frame1=Frame(root).pack(pady=50)
bg=Label(root,image=bg_img,border=0).place(x=0,y=0)
name=Label(frame1,text="TOVINO SUPER MARKET",font=("verdana",45,'bold'),fg="white",bg="blue",bd=5)
name.pack()

btnimg=Button(frame1,image=i_img2,command=admin,borderwidth=0).place(x=500,y=320)
btnimg2=Button(frame1,image=i_img3,command=userlogin).place(x=840,y=320)
root.mainloop() 
