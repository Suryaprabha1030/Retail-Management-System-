from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import mysql.connector
import re
#@@@@@@@@@@@@GUI============================================================================================================================================================================
root=Tk()
root.geometry("1920x1080+0+0")
root.config(bg="blue")
def logout():
    root.destroy()
emp=Frame(root,width=1499,height=754,bd=0,bg="white").pack(pady=15)
emp1=Label(root,text="EMPLOYEE MANAGEMENT",fg="black",font=("times",30,'bold'),bg="white").place(x=440,y=20)
emp2=Label(root,text="ADMIN",fg="black",font=("times",12),bg="white").place(x=70,y=20)
emp3=Button(root,text="Logout",fg="white",bg="blue",width=7,font=("times",16),command=logout,relief=RIDGE).place(x=45,y=50)
#@@@str=================================================================================================================================================================================
placeholderArray=['','','','','','','']
for i in range(0,6):
    placeholderArray[i]=StringVar()
#@@@@@@@@@@@@@read===================================================================================================================================================================   
def read1():
    conn=mysql.connector.connect(host="localhost",username="root",password="",port="3306",database="supermarket")
    cursor=conn.cursor()
    sql3=f"SELECT `employId`,`Name`,`password`, `designation`,`native`,`phone no`,`aadharno` FROM employ ORDER BY `employId` DESC";
    cursor.execute(sql3)
    results=cursor.fetchall()
    conn.commit()
    conn.close()
    return results
#add data in db and also added tree view-----------------------------------------------------------------------------------------------------------------------------------------------------
def refresh():
    for data in mytree1.get_children():
        mytree1.delete(data)
    for arr in read1():
        mytree1.insert(parent='',index='end',iid=arr,values=(arr),tag="orow")
def seth(word,num):
    for ph in range(0,7):
        if ph==num:
            placeholderArray[ph].set(word)
#set word in entry field-----------------------------------------------------------------------------------------------------------------------------------------------------------
def validate(phoneno):
    pat=r"^[6-9]\d{9}$s"
    if re.match(pat,phoneno):
        return True
    else:
        messagebox.showerror("error","")
    
    


def add():
    name=str(placeholderArray[0].get())
    password=str(placeholderArray[1].get())
    designation=str(placeholderArray[2].get())
    Native=str(placeholderArray[3].get())
    phoneno=str(placeholderArray[4].get())
   
    aadharno=str(placeholderArray[5].get())
    
   
    if not(name and name.strip()) or not(password and password.strip()) or not(designation and designation.strip()) or not(Native and Native.strip()) or not(phoneno and phoneno.strip()) or not(aadharno and aadharno.strip()):
        messagebox.showerror("error","enter value in tha field")
    if (len(phoneno)!=13):
        messagebox.showerror("error","valid digit of phonenumber")
        
    
    else:
        try:
            conn=mysql.connector.connect(host="localhost",username="root",password="",port="3306",database="supermarket")
            cursor=conn.cursor()
            sql3=f"INSERT INTO `employ`(`employId`, `Name`, `password`, `designation`, `native`, `phone no`, `aadharno`) VALUES ('','{name}','{password}','{designation}','{Native}','{ phoneno}','{aadharno}')"
            cursor.execute(sql3)
            conn.commit()
            conn.close()
            seth('',0)
            seth('',1)
            seth('',2)
            seth('',3)
            seth('+91',4)
            seth('',5)
        except:
            messagebox.showwarning("","error while saving")
    refresh()
#slect data in treeview------------------------------------------------------------------------------------------------------------------------------------------------------    
def selection():
    try:
        selectedItem1=mytree1.selection()[0]
        ename=str(mytree1.item(selectedItem1)['values'][1])
        epw=str(mytree1.item(selectedItem1)['values'][2])
        epw1=str(mytree1.item(selectedItem1)['values'][3])
        epw2=str(mytree1.item(selectedItem1)['values'][4])
        epw3=str(mytree1.item(selectedItem1)['values'][5])
        epw4=str(mytree1.item(selectedItem1)['values'][6])
        seth(ename,0)
        seth(epw,1)
        seth(epw1,2)
        seth(epw2,3)
        seth(epw3,4)
        seth(epw4,5)
       
    except:
        messagebox.showwarning("","Please select a data row")

#--------------update data in -------------------------------------------------------------------------------------------------------------------------------  
def update():
    ename=''
    try:
        selectedItem1=mytree1.selection()[0]
        ename=str(mytree1.item(selectedItem1)['values'][1])
       
    except:
         messagebox.showwarning('','select click button')
         
    name=str(placeholderArray[0].get())
    password=str(placeholderArray[1].get())
    designation=str(placeholderArray[2].get())
    Native=str(placeholderArray[3].get())
    phoneno=str(placeholderArray[4].get())
    aadharno=str(placeholderArray[5].get())
    if not(name and name.strip()) or not(password and password.strip()) or not(designation and designation.strip()) or not(Native and Native.strip()) or not(phoneno and phoneno.strip()) or not(aadharno and aadharno.strip()):
        messagebox.showinfo("","Then,enter value in tha field")
        return
    if(ename!=name):
        messagebox.showwarning("","you cannot change  name")
        return
    if (len(phoneno)!=12):
        messagebox.showerror("error","valid digit of phonenumber")
    else:
        try:
            conn=mysql.connector.connect(host="localhost",username="root",password="",port="3306",database="supermarket")
            cursor=conn.cursor()
            sql5=f"UPDATE `employ` SET  `Name`='{name}',`password`='{password}', `designation`='{designation}',`native`='{Native}',`phone no`='{ phoneno}',`aadharno`='{aadharno}' WHERE `Name`='{name}'"
            cursor.execute(sql5)
            conn.commit()
            conn.close()
            seth('',0)
            seth('',1)
            seth('',2)
            seth('',3)
            seth('+91',4)
            seth('',5)
            messagebox.showinfo("","update succesfully")
        except:
            messagebox.showinfo("","sorry,an error occured")
            return
            
    refresh()
def delete():
    try:
        if(mytree1.selection()[0]):
            decide=messagebox.askquestion("","do you want delete?")
            if(decide!='yes'):
                return
            else:
                selectedItem=mytree1.selection()[0]
                selectedProduct=str(mytree1.item(selectedItem)['values'][1])
                
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="",port=3306,database="supermarket")
                cursor=conn.cursor()
                sql4=f"DELETE FROM employ WHERE `Name`='{selectedProduct}'"
                cursor.execute(sql4)
                conn.commit()
                conn.close()
                messagebox.showinfo('',"data has been successfully deleted?")
            except:
               messagebox.showerror('',"error while delete")
    except:
        messagebox.showerror(''," please select row")
    refresh()
    
#@@@@@@@@@gui for entry field==========================================================================================================================================
emp4=LabelFrame(root,text="Menu",font=("times",13),width=510,height=560,bg="white",bd=3).place(x=60,y=150)

emp5=Label(root,text="Name",fg="black",font=("times",14),bg="white").place(x=80,y=200)
emp6=Entry(root,bd=2,font=("times",20),width=15,textvariable=placeholderArray[0]).place(x=80,y=230)
emp7=Label(root,text="password",fg="black",font=("times",14),bg="white").place(x=310,y=200)
emp8=Entry(root,bd=2,font=("times",20),width=15,textvariable=placeholderArray[1]).place(x=310,y=230)

emp9=Label(root,text="designation",fg="black",font=("times",14),bg="white").place(x=80,y=290)
emp10=Entry(root,bd=2,font=("times",20),width=15,textvariable=placeholderArray[2]).place(x=80,y=320)
emp11=Label(root,text="Native",fg="black",font=("times",14),bg="white").place(x=310,y=290)
emp12=Entry(root,bd=2,font=("times",20),width=15,textvariable=placeholderArray[3]).place(x=310,y=320)

emp13=Label(root,text="phone no",fg="black",font=("times",14),bg="white").place(x=80,y=380)
emp14=Entry(root,bd=2,font=("times",20),width=15,textvariable=placeholderArray[4])
emp14.place(x=80,y=410)
emp14.insert(END,"+91")

emp15=Label(root,text="aadhar no",fg="black",font=("times",14),bg="white").place(x=310,y=380)
emp16=Entry(root,bd=2,font=("times",20),width=15,textvariable=placeholderArray[5]).place(x=310,y=410)

#@@@@@@@@@@@@@@@@@@@@button===============================================================================
emp19=Button(root,text="ADD",fg="white",bg="blue",width=9,font=("times",14),command=add,relief=RIDGE,bd=0).place(x=80,y=580)
emp20=Button(root,text="SELECT",fg="white",bg="blue",width=9,font=("times",14),command=selection,bd=0).place(x=210,y=580)
emp21=Button(root,text="UPDATE ",fg="white",bg="blue",width=9,font=("times",14),command=update,relief=RIDGE,bd=0).place(x=330,y=580)
emp21=Button(root,text="DELETE",fg="white",bg="blue",width=9,font=("times",14),command=delete,relief=RIDGE,bd=0).place(x=450,y=580)
#@@@@@@@@@gui for tree viwe========================================================================================================================================   

af4=Frame(root,bd=2,relief=GROOVE)
af4.place(x=630,y=160)
mytree1=ttk.Treeview(af4,show='headings',height=26)
dummy=[['123','567','45656776','5676778','5566776','56676767']]


mytree1['columns']=('employeId', 'Name','password','native','designation', 'phone no', 'Aadhar no')
mytree1.column("#0",width=0,stretch=NO)
mytree1.column('employeId',anchor=W,width=70)
mytree1.column('Name',anchor=W,width=130)
mytree1.column('password',anchor=W,width=130)
mytree1.column('designation',anchor=W,width=130)
mytree1.column('native',anchor=W,width=130)
mytree1.column('phone no',anchor=W,width=130)
mytree1.column('Aadhar no',anchor=W,width=130)


mytree1.heading('employeId',text='employeId',anchor=W)
mytree1.heading('Name',text='Name',anchor=W)
mytree1.heading('password',text='password',anchor=W)
mytree1.heading('designation',text='designation',anchor=W)
mytree1.heading('native',text='native',anchor=W)


mytree1.heading('phone no',text='phone no',anchor=W)
mytree1.heading('Aadhar no',text='Aadhar no',anchor=W)

scroll=Scrollbar(root,orient=VERTICAL)
scroll.place(x=1464,y=160,width=22,height=549)
scroll.configure(command=mytree1.yview)
mytree1.configure(yscrollcommand=scroll.set)
mytree1.configure(selectmode="extended")


mytree1.tag_configure('orow',background="blue")
mytree1.pack(fill=X)
refresh()


if __name__ == '__main__':
    root.mainloop()

