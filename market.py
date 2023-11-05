from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import mysql.connector


#@@@@@@@@@@@@GUI========================================================================================================================================
root=Tk()
root.geometry("1920x1080+0+0")
root.config(bg="blue")
def logout():
    root.destroy()
framew1=Frame(root,width=1499,height=754,bd=0,bg="white").pack(pady=15)
al3=Label(root,text="INVENTORY MANAGEMENT",fg="black",font=("times",30,'bold'),bg="white").place(x=430,y=20)
al=Label(root,text="ADMIN",fg="black",font=("times",12),bg="white").place(x=70,y=20)
btna=Button(root,text="Logout",fg="white",bg="blue",width=7,font=("times",16),command=logout,relief=RIDGE).place(x=45,y=50)
#@@@str===============================================
placeholderArray=['','','','','','','']
for i in range(0,7):
    placeholderArray[i]=StringVar()
#@@@@@@@@@@@@@read=====================================================    
def read():
    conn=mysql.connector.connect(host="localhost",username="root",password="",port="3306",database="supermarket")
    cursor=conn.cursor()
    sql=f"SELECT `ProductId`,`ProductName`,`company`, `Catagory`,`In-stock`,`MRP`,`Cost price`,`Vendor no` FROM inventory1 ORDER BY `ProductId` DESC";
    cursor.execute(sql)
    results=cursor.fetchall()
    conn.commit()
    conn.close()
    return results
#add data in db and also added tree view------------------------------------------------------------------------
def refresh():
    for data in mytree.get_children():
        mytree.delete(data)
    for arr in read():
        mytree.insert(parent='',index='end',iid=arr,values=(arr),tag="orow")
#set word in entry field-------------------------------------------------------------------------------------------------------------------        
def setp(word,num):
    for ph in range(0,7):
        if ph==num:
            placeholderArray[ph].set(word)



#------------------------------------------------------------adding------------------------------------------------
def adding():
    name=str(placeholderArray[0].get())
    company=str(placeholderArray[1].get())
    catagory=str(placeholderArray[2].get())
    inStock=str(placeholderArray[3].get())
    costprice=str(placeholderArray[5].get())
    mrp=str(placeholderArray[4].get())
    vendorNo=str(placeholderArray[6].get())
    if not(name and name.strip()) or not(company and company.strip()) or not(catagory and catagory.strip()) or not(inStock and inStock .strip()) or not(costprice and costprice.strip()) or not(mrp and mrp.strip()) or not(vendorNo and vendorNo.strip()):
         messagebox.showerror("error","enter value in tha field")
    if (len(vendorNo)!=13):
        messagebox.showerror("error","valid digit of phonenumber")
    else:
       try:
           conn=mysql.connector.connect(host="localhost",username="root",password="",port="3306",database="supermarket")
           cursor=conn.cursor()
           sql2=f"INSERT INTO inventory1(`ProductId`,`ProductName`,`company`, `Catagory`,`In-stock`,`MRP`,`Cost price`,`Vendor no`) VALUES('','{name}','{company}','{catagory}','{inStock}','{mrp}','{costprice}','{vendorNo}')"
           cursor.execute(sql2)
           conn.commit()
           conn.close()
           setp('',0)
           setp('',1)
           setp('',2)
           setp('',3)
           setp('',4)
           setp('',5)
           setp('+91',6)
       except:
           messagebox.showwarning("","error while saving")
    refresh()
    
    

#------------------update-------------------------------------------
def update():
    selectedProduct=''
    try:
        selectedItem=mytree.selection()[0]
        selectedProduct=str(mytree.item(selectedItem)['values'][1])
    except:
        messagebox.showwarning('','first click select button  ')
        
    name=str(placeholderArray[0].get())
    company=str(placeholderArray[1].get())
    catagory=str(placeholderArray[2].get())
    inStock=str(placeholderArray[3].get())
    costprice=str(placeholderArray[5].get())
    mrp=str(placeholderArray[4].get())
    vendorNo=str(placeholderArray[6].get())
    if not(name and name.strip()) or not(company and company.strip()) or not(catagory and catagory.strip()) or not(inStock and inStock .strip()) or not(costprice and costprice.strip()) or not(mrp and mrp.strip()) or not(vendorNo and vendorNo.strip()):
        messagebox.showerror("error","enter value in tha field")
        return
    if(selectedProduct!=name):
        messagebox.showwarning("","you cannot change product name")
        return
    if (len(vendorNo)!=12):
        messagebox.showerror("error","valid digit of phonenumber")
    else:
        try:
            conn=mysql.connector.connect(host="localhost",username="root",password="",port="3306",database="supermarket")
            cursor=conn.cursor()
            sql3=f"UPDATE `inventory1` SET `ProductName`='{name}',`company`='{company}',`Catagory`='{catagory}',`In-stock`='{inStock}',`MRP`='{mrp}',`Cost price`='{costprice}',`Vendor no`='{vendorNo}' WHERE `ProductName`='{name}'"
            cursor.execute(sql3)
            conn.commit()
            conn.close()
            setp('',0)
            setp('',1)
            setp('',2)
            setp('',3)
            setp('',4)
            setp('',5)
            setp('+91',6)
            setp('',7)
            messagebox.showinfo("","update succesfully")
        except:
            messagebox.showinfo("","sorry,an error occured")
            return
    refresh()
#------------------------------------select-------------------------------------------------
def select():
    try:
        selectedItem=mytree.selection()[0]
        cname=str(mytree.item(selectedItem)['values'][2])
        ccname=str(mytree.item(selectedItem)['values'][3])
        cstock=str(mytree.item(selectedItem)['values'][4])
        cmrp=str(mytree.item(selectedItem)['values'][5])
        ccostprice=str(mytree.item(selectedItem)['values'][6])
        vno=str(mytree.item(selectedItem)['values'][7])
        selectedProduct=str(mytree.item(selectedItem)['values'][1])
        setp(selectedProduct,0)
        setp(cname,1)
        setp(ccname,2)
        setp(cstock,3)
        setp(cmrp,4)
        setp(ccostprice,5)
        setp(vno,6)
    except:
        messagebox.showwarning("","Please select a data row")
def delete():
    try:
        if(mytree.selection()[0]):
            decide=messagebox.askquestion("","do you want delete?")
            if(decide!='yes'):
                return
            else:
                selectedItem=mytree.selection()[0]
                selectedProduct=str(mytree.item(selectedItem)['values'][1])
                print( selectedProduct)
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="",port=3306,database="supermarket")
                cursor=conn.cursor()
                sql4=f"DELETE FROM inventory1 WHERE `ProductName`='{selectedProduct}'"
                cursor.execute(sql4)
                conn.commit()
                conn.close()
                messagebox.showinfo('',"data has been successfully deleted?")
            except:
               messagebox.showerror('',"error while delete")
    except:
        messagebox.showerror(''," please select row")
    refresh()
#@@@@@@@@@gui for entry field=================================================        
af1=LabelFrame(root,text="Menu",font=("times",13),width=510,height=560,bg="white",bd=3).place(x=60,y=150)

a3=Label(root,text="productName",fg="black",font=("times",14),bg="white").place(x=80,y=200)
e2=Entry(root,bd=2,font=("times",20),width=15,textvariable=placeholderArray[0]).place(x=80,y=230)
a4=Label(root,text="company",fg="black",font=("times",14),bg="white").place(x=310,y=200)
e3=Entry(root,bd=2,font=("times",20),width=15,textvariable=placeholderArray[1]).place(x=310,y=230)

a5=Label(root,text="Category",fg="black",font=("times",14),bg="white").place(x=80,y=290)
e4=Entry(root,bd=2,font=("times",20),width=15,textvariable=placeholderArray[2]).place(x=80,y=320)
a6=Label(root,text="Quantity",fg="black",font=("times",14),bg="white").place(x=310,y=290)
e5=Entry(root,bd=2,font=("times",20),width=15,textvariable=placeholderArray[3]).place(x=310,y=320)

a7=Label(root,text="MRP",fg="black",font=("times",14),bg="white").place(x=80,y=380)
e6=Entry(root,bd=2,font=("times",20),width=15,textvariable=placeholderArray[4]).place(x=80,y=410)

a8=Label(root,text="CostPrice",fg="black",font=("times",14),bg="white").place(x=310,y=380)
e7=Entry(root,bd=2,font=("times",20),width=15,textvariable=placeholderArray[5]).place(x=310,y=410)

a9=Label(root,text="Vendor Phone NO",fg="black",font=("times",14),bg="white").place(x=80,y=470)
e8=Entry(root,bd=2,font=("times",20),width=15,textvariable=placeholderArray[6])
e8.place(x=80,y=500)
e8.insert(END,"+91")
btna23=Button(root,text="ADD",fg="white",bg="blue",width=9,font=("times",14),relief=RIDGE,command=adding,bd=0).place(x=80,y=580)
btna2=Button(root,text="SELECT",fg="white",bg="blue",width=9,font=("times",14),command=select,relief=RIDGE,bd=0).place(x=210,y=580)
btna2=Button(root,text="UPDATE ",fg="white",bg="blue",width=9,font=("times",14),command=update,relief=RIDGE,bd=0).place(x=330,y=580)
btna3=Button(root,text="DELETE",fg="white",bg="blue",width=9,font=("times",14),command=delete,relief=RIDGE,bd=0).place(x=450,y=580)
    
#@@@@@@@@@@@@@@@@@@@GUI FOR TREEVIEW-------------------------------------------------------------------------------------------------------------
af2=Frame(root,bd=2,relief=GROOVE)
af2.place(x=630,y=160)
mytree=ttk.Treeview(af2,show='headings',height=26)


mytree['columns']=('ProductId', 'ProductName', 'company', 'Catagory', 'In-stock', 'MRP', 'Cost price', 'Vendor no')
mytree.column("#0",width=0,stretch=NO)
mytree.column('ProductId',anchor=W,width=100)
mytree.column('ProductName',anchor=W,width=130)
mytree.column('company',anchor=S,width=130)
mytree.column('Catagory',anchor=S,width=130)
mytree.column('In-stock',anchor=W,width=70)
mytree.column('MRP',anchor=W,width=70)
mytree.column('Cost price',anchor=W,width=70)
mytree.column('Vendor no',anchor=W,width=130)


mytree.heading('ProductId',text='Product ID',anchor=W)
mytree.heading('ProductName',text='Name',anchor=W)
mytree.heading('company',text='Company',anchor=W)
mytree.heading('Catagory',text='Catogory',anchor=W)


mytree.heading('In-stock',text='In-stock',anchor=W)
mytree.heading('MRP',text='MRP',anchor=W)
mytree.heading('Cost price',text='Costprice',anchor=W)
mytree.heading('Vendor no',text='Vendor no',anchor=W)

scrol=Scrollbar(root,orient=VERTICAL)
scrol.place(x=1464,y=160,width=22,height=549)
scrol.configure(command=mytree.yview)

mytree.tag_configure('orow',background="blue")
mytree.configure(yscrollcommand=scrol.set)
mytree.configure(selectmode="extended")
mytree.pack(fill=X)
refresh()


if __name__ == '__main__':
    root.mainloop()

       


                   
                   

