from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import subprocess

root=Tk()
root.geometry("1920x1080+0+0")
#@@@@@image================================================================================================================================================================================
img1=Image.open("C:/project/bg1.png")
r_img=img1.resize((1920,1080))
bg_img=ImageTk.PhotoImage(r_img)
img4=Image.open("C:/project/empu.png")
r4_img=img4.resize((170,170))
i_img4=ImageTk.PhotoImage(r4_img)

img9=Image.open("C:/project/report.png")
r9_img=img9.resize((170,170))
i_img9=ImageTk.PhotoImage(r9_img)
####@@@@@@@@@@@@@function================================================================================================================================================================
def sub2():
    subprocess.Popen(["python", "employee.py"])
def sub3():
    subprocess.Popen(["python", "report.py"])
def logout():
    root.destroy()

####@@@@@@@@@@@@@GUI================================================================================================================================================================

frame2=Frame(root).pack(pady=50)
bg1=Label(root,image=bg_img,border=0).place(x=0,y=0)
lab=Label(root,text="EMPLOYEE MANAGEMENT",font=("verdana",44,'bold'),bg="blue",fg="white",bd=5).pack()
btnimg1=Button(root,image=i_img4,command=sub2,borderwidth=0).place(x=500,y=340)

btnimg2=Button(root,image=i_img9,command=sub3,borderwidth=0).place(x=840,y=340)
    
btne1=Button(root,text="Logout",fg="white",bg="blue",width=9,font=("times",19),command=logout,relief=RIDGE).place(x=45,y=50)

if __name__ == '__main__':
    root.mainloop()
